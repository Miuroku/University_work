from datetime import datetime
from library.serializer.objects_packager.basic_functions import is_magicmarked


# Test primitives.
example_string = 'Some\' str'
example_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
example_frozenset = {1, 2, 3, 4}
example_set = {1, 2, 4, 5}
example_list = ['Some string', True, None, (None, False, 'sdee')]
example_float = 0.12345
example_None = None
example_int = 343
example_datetime = datetime(2001, 11, 14)
example_bool = True
example_dict = {'56': [5, 23, 6], 'key': (5, 'iewr', 3), '0.331': 68}


# Test complex objects.
class example_class_1():
    a = 2
    def __init__(self):
        self.b = 10


example_instance_1 = example_class_1()
example_class_1.c = 'added new field to the class'
example_instance_1.d = 'new field'


class example_class_2(example_class_1):
    def __init__(self, s):
        super().__init__()
        self.e = str(s) + self.c

    def some_class_func(self):
        one = 'i\'m doing something...'
        two = 'other string'
        return one + two

class example_class_3():
    @staticmethod
    def static_method():
        return 'From static method'

    @classmethod
    def class_method(cls):
        return 'From class method'


class example_class_4():
    __val = 0
    @property
    def Value(self):
        return self.__val

    @Value.setter
    def Value(self, value):
        self.__val = value

class example_Metaclass_1(type):

    def __new__(cls, name, bases, dct):
        attrs = {}
        for name, val in dct.items():
            if is_magicmarked(name):
                attrs[name] = val
            else:
                attrs[name.upper()] = val

        return super(example_Metaclass_1, cls).__new__(cls, name, bases, attrs)


class example_Metaclass_2(metaclass=example_Metaclass_1):
    some_field = 'some_field'


# Test functions.
def example_func(val: int):
    return val + 532


example_lambda = lambda s: f'Lambda function {s}'


def example_recursion(val: int):
    if val == 0:
        return 0

    return example_recursion(val - 1) + 1


def example_generator(val: int):
    for i in range(val):
        yield i


def example_func_return_func():
    def inner_func():
        return 'Just a random string'

    return inner_func

def example_with_inner_func(val: int):
    def inner_func(val):
        return -1 * val

    return inner_func(val - inner_func(val))