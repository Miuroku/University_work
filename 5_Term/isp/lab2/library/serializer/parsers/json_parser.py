from abc import ABC
import re


def is_bool(s: str) -> bool:
    if s == 'true' or s == "false":
        return True

    return False


def to_bool(s: str) -> bool:
    if not is_bool(s):
        raise TypeError(f"String '{s}' cannot be converted to 'bool'")

    if s == 'true':
        return True
    else:
        return False


def is_number(s: str) -> bool:
    match = re.match('\d+\.?\d*', s)
    if match is None or match.group() != s:
        return False
    else:
        return True


def to_number(s: str):
    if not is_number(s):
        raise TypeError(f"String '{s}' cannot be converted to 'int' or 'float'")

    if s.find('.') == -1:
        return int(s)
    else:
        return float(s)


def is_str(s: str) -> bool:
    if s[0] == '"' and s[-1] == '"':
        return True

    return False


def is_arr(s: str) -> bool:
    if s[0] == '[' and s[-1] == ']':
        return True

    return False


def is_dict(s: str) -> bool:
    if s[0] == '{' and s[-1] == '}':
        return True

    return False


def matches(ch1, ch2) -> bool:
    if ch1 == '{' and ch2 == '}' or ch1 == '[' and ch2 == ']':
        return True

    return False


def manage_brackets(ch: str, brackets: list):
    if ch == '{' or ch == '[':
        brackets.append(ch)
    if ch == '}' or ch == ']':
        bracket = brackets.pop()
        if not matches(bracket, ch):
            raise Exception(f"Invalid JSON format! Brackets {bracket} and {ch} doesn't match")


def split_arr(s: str):
    s = s[1:-1]
    elements = []
    brackets = []
    start_i = 0

    for i in range(len(s)):
        manage_brackets(s[i], brackets)

        if s[i] == ',' and len(brackets) == 0:
            elements.append(s[start_i:i])
            start_i = i + 2

    if len(s):
        elements.append(s[start_i:])

    return elements


def split_dict(s: str):
    s = s[1:-1]
    elements = []
    brackets = []

    key, value = None, None
    out_expr = True
    start_i = 0

    for i in range(len(s)):
        manage_brackets(s[i], brackets)

        if s[i] == '"':
            out_expr = not out_expr

        if s[i] == ':' and out_expr and len(brackets) == 0:
            key = s[start_i:i]
            start_i = i + 2

        if s[i] == ',' and out_expr and len(brackets) == 0:
            value = s[start_i:i]
            start_i = i + 2
            elements.append((key, value))

    if len(s):
        value = s[start_i:]
        elements.append((key, value))

    return elements


# --------------------------------------------------------------------------------
class JsonParser(ABC):
    @staticmethod
    def dumps(obj):
        if obj is None:
            return 'null'

        obj_type = type(obj)
        if obj_type is bool:
            return f'{str(obj).lower()}'

        if obj_type is int or obj_type is float:
            return f'{obj}'

        if obj_type is str:
            return f'"{obj}"'

        if obj_type is tuple or obj_type is list:
            res = ''
            for i in range(len(obj)):
                res += ', ' + JsonParser.dumps(obj[i])

            return '[' + res[2:] + ']'

        if obj_type is dict:
            res = ''
            for key in obj:
                key_ = JsonParser.dumps(key)
                value_ = JsonParser.dumps(obj[key])
                if key_[0] != '"':
                    key_ = f'"{key_}"'

                res += f', {key_}: {value_}'

            return '{' + res[2:] + '}'

        raise TypeError(f'Object of type {obj_type.__name__} is not JSON serializable')

    @staticmethod
    def dump(obj, fp):
        with open(fp, 'w') as file:
            file.write(JsonParser.dumps(obj))

    @staticmethod
    def loads(s):
        if s == 'null':
            return None

        if is_bool(s):
            return to_bool(s)

        if is_number(s):
            return to_number(s)

        if is_str(s):
            return s[1:-1]

        if is_arr(s):
            arr = []
            split = split_arr(s)
            for i in range(len(split)):
                arr.append(JsonParser.loads(split[i]))

            return arr

        if is_dict(s):
            d = {}
            split = split_dict(s)
            for i in range(len(split)):
                key = JsonParser.loads(split[i][0])
                if isinstance(key, list):
                    key = tuple(key)

                d[key] = JsonParser.loads(split[i][1])

            return d

        raise TypeError(f"{s} cannot be converted to an object")

    @staticmethod
    def load(fp):
        with open(fp, 'r') as file:
            return JsonParser.loads(file.read())