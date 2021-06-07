import builtins
import inspect
import re
from inspect import getsourcelines
from abc import ABC


class ClassCreator(ABC):
    @staticmethod
    def create(name, mro):
        globals().update({el.__name__: el for el in mro[0]})
        if len(mro[0]) != 0:
            bases = ','.join([base.__name__ for base in mro[0]])
        else:
            bases = ''

        if mro[1]:
            globals().update({mro[1].__name__: mro[1]})
            meta = 'metaclass=' + mro[1].__name__
        else:
            meta = ''

        if bases != '':
            str_ = bases + ", " + meta
        else:
            str_ = meta
        exec(f"class {name}({str_}):\n\tpass")
        return eval(f"{name}")


def set_class_attrs(cls, attributes=None):
    if attributes is None:
        return cls

    for attr in attributes:
        if attr[1] != None:
            try:
                if attr[2] == "static method":
                    setattr(cls, attr[0], staticmethod(attr[1]))
                elif attr[2] == "class method":
                    setattr(cls, attr[0], classmethod(attr[1]))
                else:
                    setattr(cls, attr[0], attr[1])
            except AttributeError:
                continue
    return cls


def create_class(name, mro=None, attributes=None):
    template = ClassCreator.create(name, mro)
    if attributes is None:
        return template

    return set_class_attrs(template, attributes)


def create_instance(type_of_instance, our_fields):
    new_instance = type_of_instance.__new__(type_of_instance)
    for field_element in our_fields:
        setattr(new_instance, field_element, our_fields[field_element])

    return new_instance


def cell_factory(el):
    inner_el = el
    def inner():
        return inner_el

    return inner.__closure__[0]


def get_code(obj):
    lines = getsourcelines(obj)[0]
    indent = len(lines[0]) - len(lines[0].lstrip())

    new_lines = []
    for line in lines:
        if len(line) >= indent:
            line = line[indent:]

        new_lines.append(line)
    return '\n'.join(new_lines)


# Objects inspector functions
def is_primitive(obj: object) -> bool:
    return type(obj) in [int, float, bool, str]


def is_basetype(obj: object) -> bool:
    for el in [int, float, bool, str, dict, list, tuple, set]:
        if el.__name__ == obj.__name__:
            return True

    return False


def is_magicmarked(s: str) -> bool:
    return re.match("^__(?:\w+)__$", s) != None


def is_instance(obj):
    if not hasattr(obj, '__dict__') or inspect.isroutine(obj) or inspect.isclass(obj):
        return False

    return True


def fetch_type_references(cls):
    if inspect.isclass(cls):
        mro = inspect.getmro(cls)
        metamro = inspect.getmro(type(cls))
        metamro = tuple(cls for cls in metamro if cls not in (type, object))
        class_bases = mro
        if not type in mro and len(metamro) != 0:
            return class_bases[1:-1], metamro[0]
        else:
            return class_bases[1:-1], None


def fetch_func_references(func: object):
    if inspect.ismethod(func):
        func = func.__func__

    if not inspect.isfunction(func):
        raise TypeError("{!r} is not a Python function".format(func))

    code = func.__code__
    if func.__closure__ is None:
        nonlocal_vars = {}
    else:
        nonlocal_vars = {
            var: cell.cell_contents
            for var, cell in zip(code.co_freevars, func.__closure__)
        }

    global_ns = func.__globals__
    builtin_ns = global_ns.get("__builtins__", builtins.__dict__)
    if inspect.ismodule(builtin_ns):
        builtin_ns = builtin_ns.__dict__
    global_vars = {}
    builtin_vars = {}
    unbound_names = set()
    for name in code.co_names:
        if name in ("None", "True", "False"):
            continue
        try:
            global_vars[name] = global_ns[name]
        except KeyError:
            try:
                builtin_vars[name] = builtin_ns[name]
            except KeyError:
                unbound_names.add(name)

    return (nonlocal_vars, global_vars,
            builtin_vars, unbound_names)


def deconstruct_class(cls):
    attributes = inspect.classify_class_attrs(cls)
    deconstructed = []
    for attr in attributes:
        if attr.defining_class != object and attr.defining_class != type and \
            attr.name not in ["__dict__", "__weakref__"]:
            deconstructed.append((attr.name, attr.object, attr.kind))

    return deconstructed


def deconstruct_func(func):
    code = {el: getattr(func.__code__, el) for el in func.__code__.__dir__() if not is_magicmarked(el) and "co" in el}

    refs = fetch_func_references(func)
    defaults = func.__defaults__
    return {'.name': func.__name__, '.code': code, '.references': refs, '.defaults': defaults}


def getfields(obj):
    members = inspect.getmembers(obj)

    cls = type(obj)
    type_attrnames = [el.name for el in inspect.classify_class_attrs(cls)]

    result = {}

    for member in members:
        if not member[0] in type_attrnames:
            result[member[0]] = member[1]

    return result


def deconstruct_instance(obj):
    type_ = type(obj)
    fields = getfields(obj)

    return (type_, fields)