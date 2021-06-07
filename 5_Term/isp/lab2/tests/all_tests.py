import pytest
from library.serializer.serializer_factory import create_serializer
from tests.data_for_tests import *


serializer_types = ['json', 'yaml', 'pickle']


class TestPrimitives:
    def test_invalid_serializer(self):
        try:
            invalid_serializer = create_serializer('* Something wrong *')
        except Exception as e:
            assert type(e) == ValueError

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_None(self, ser_type):
        serializer = create_serializer(ser_type)
        assert serializer.loads(serializer, serializer.dumps(serializer, example_None)) == example_None

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_invalid_format(self, ser_type):
        serializer = create_serializer(ser_type)
        invalid = {"field": "smth", "new_field": {"a", "b", "c"}}
        try:
            serializer.loads(serializer, invalid)
        except Exception as e:
            assert type(e) == ValueError

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_bool(self, ser_type):
        serializer = create_serializer(ser_type)
        assert serializer.loads(serializer, serializer.dumps(serializer, example_bool)) == example_bool

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_int(self, ser_type):
        serializer = create_serializer(ser_type)
        assert serializer.loads(serializer, serializer.dumps(serializer, example_int)) == example_int

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_float(self, ser_type):
        serializer = create_serializer(ser_type)
        assert serializer.loads(serializer, serializer.dumps(serializer, example_float)) == example_float

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_tuple(self, ser_type):
        serializer = create_serializer(ser_type)
        assert serializer.loads(serializer, serializer.dumps(serializer, example_tuple)) == example_tuple

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_string(self, ser_type):
        serializer = create_serializer(ser_type)
        assert serializer.loads(serializer, serializer.dumps(serializer, example_string)) == example_string

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_frozenset(self, ser_type):
        serializer = create_serializer(ser_type)
        assert serializer.loads(serializer, serializer.dumps(serializer, example_frozenset)) == example_frozenset

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_list(self, ser_type):
        serializer = create_serializer(ser_type)
        assert serializer.loads(serializer, serializer.dumps(serializer, example_list)) == example_list


    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_datetime(self, ser_type):
        serializer = create_serializer(ser_type)
        assert serializer.loads(serializer, serializer.dumps(serializer, example_datetime)) == example_datetime

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_set(self, ser_type):
        serializer = create_serializer(ser_type)
        assert serializer.loads(serializer, serializer.dumps(serializer, example_set)) == example_set

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_dict(self, ser_type):
        serializer = create_serializer(ser_type)
        print(serializer.loads(serializer, serializer.dumps(serializer, example_dict)), '\n ***\n', example_dict, '\n')
        assert serializer.loads(serializer, serializer.dumps(serializer, example_dict)) == example_dict


class TestFunctions:
    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_inner_func(self, ser_type):
        serializer = create_serializer(ser_type)
        assert serializer.loads(serializer, serializer.dumps(serializer, example_with_inner_func))(9) == example_with_inner_func(9)

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_lambda(self, ser_type):
        serializer = create_serializer(ser_type)
        assert serializer.loads(serializer, serializer.dumps(serializer, example_lambda))('$') == example_lambda('$')

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_simple_func(self, ser_type):
        serializer = create_serializer(ser_type)
        assert serializer.loads(serializer, serializer.dumps(serializer, example_func))(5) == example_func(5)

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_recursion_func(self, ser_type):
        serializer = create_serializer(ser_type)
        assert serializer.loads(serializer, serializer.dumps(serializer, example_recursion))(7) == example_recursion(7)

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_gen(self, ser_type):
        serializer = create_serializer(ser_type)
        res = serializer.loads(serializer, serializer.dumps(serializer, example_generator))
        assert [item for item in res(10)] == [item for item in example_generator(10)]

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_return_func(self, ser_type):
        serializer = create_serializer(ser_type)
        assert serializer.loads(serializer, serializer.dumps(serializer, example_func_return_func))()() == example_func_return_func()()
