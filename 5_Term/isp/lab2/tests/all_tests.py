import pytest
from library.serializer.serializer_factory import create_serializer
from tests.data_for_tests import *


serializer_types = ['json', 'yaml', 'pickle', 'toml']


class TestPrimitives:
    def test_invalid_serializer(self):
        try:
            invalid_serializer = create_serializer('* Something wrong *')
        except Exception as e:
            assert type(e) == ValueError

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_None(self, ser_type):
        serializer = create_serializer(ser_type)
        serializer = create_serializer('json')
        strin = serializer.dumps(serializer, example_None)
        print(f'Our string : {strin} **********************')
        obj = serializer.loads(serializer, strin)
        print(f'Our object : {obj} ************************')
        assert serializer.loads(serializer, serializer.dumps(serializer, example_None)) == example_None

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_invalid_format(self, ser_type):
        serializer = create_serializer(ser_type)
        invalid = {"field": "smth", "new_field": {"a", "b", "c"}}
        serializer = create_serializer('json')
        try:
            serializer.loads(serializer, invalid)
        except Exception as e:
            assert type(e) == ValueError

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_bool(self, ser_type):
        serializer = create_serializer(ser_type)
        serializer = create_serializer('json')
        assert serializer.loads(serializer, serializer.dumps(serializer, example_bool)) == example_bool

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_int(self, ser_type):
        serializer = create_serializer(ser_type)
        serializer = create_serializer('json')
        assert serializer.loads(serializer, serializer.dumps(serializer, example_int)) == example_int
    
    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_float(self, ser_type):
        serializer = create_serializer('json')
        assert serializer.loads(serializer, serializer.dumps(serializer, example_float)) == example_float

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_tuple(self, ser_type):
        serializer = create_serializer('json')
        assert serializer.loads(serializer, serializer.dumps(serializer, example_tuple)) == example_tuple

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_string(self, ser_type):
        serializer = create_serializer('json')
        assert serializer.loads(serializer, serializer.dumps(serializer, example_string)) == example_string

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_frozenset(self, ser_type):
        serializer = create_serializer('json')
        assert serializer.loads(serializer, serializer.dumps(serializer, example_frozenset)) == example_frozenset

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_list(self, ser_type):
        serializer = create_serializer(ser_type)
        serializer = create_serializer('json')
        assert serializer.loads(serializer, serializer.dumps(serializer, example_list)) == example_list

    
    def test_datetime(self, ser_type='json'):
        serializer = create_serializer(ser_type)
        assert serializer.loads(serializer, serializer.dumps(serializer, example_datetime)) == example_datetime

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_set(self, ser_type):
        serializer = create_serializer('json')
        assert serializer.loads(serializer, serializer.dumps(serializer, example_set)) == example_set

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_dict(self, ser_type):
        serializer = create_serializer('json')
        print(serializer.loads(serializer, serializer.dumps(serializer, example_dict)), '\n ***\n', example_dict, '\n')
        assert serializer.loads(serializer, serializer.dumps(serializer, example_dict)) == example_dict


class TestFunctions:
    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_inner_func(self, ser_type):
        serializer = create_serializer('json')
        assert serializer.loads(serializer, serializer.dumps(serializer, example_with_inner_func))(9) == example_with_inner_func(9)

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_lambda(self, ser_type):
        serializer = create_serializer('json')
        assert serializer.loads(serializer, serializer.dumps(serializer, example_lambda))('$') == example_lambda('$')

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_simple_func(self, ser_type):
        serializer = create_serializer('json')
        assert serializer.loads(serializer, serializer.dumps(serializer, example_func))(5) == example_func(5)

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_recursion_func(self, ser_type):
        serializer = create_serializer('json')
        assert serializer.loads(serializer, serializer.dumps(serializer, example_recursion))(7) == example_recursion(7)

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_gen(self, ser_type):
        serializer = create_serializer('json')
        res = serializer.loads(serializer, serializer.dumps(serializer, example_generator))
        assert [item for item in res(10)] == [item for item in example_generator(10)]

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_return_func(self, ser_type):
        serializer = create_serializer('json')
        assert serializer.loads(serializer, serializer.dumps(serializer, example_func_return_func))()() == example_func_return_func()()


class TestClass:
    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_class_1(self, ser_type):
        serializer = create_serializer('json')
        res = serializer.loads(serializer, serializer.dumps(serializer, example_class_1))
        assert dir(res) == dir(example_class_1)
        assert res.a == example_class_1.a
        assert res.c == example_class_1.c

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_instance_1(self, ser_type):
        serializer = create_serializer('json')
        res = serializer.loads(serializer, serializer.dumps(serializer, example_instance_1))
        assert dir(res) == dir(example_instance_1)
        assert res.a == example_instance_1.a
        assert res.b == example_instance_1.b
        assert res.c == example_instance_1.c
        assert res.d == example_instance_1.d
        assert isinstance(res, example_class_1)

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_class_2(self, ser_type):
        serializer = create_serializer('json')
        res = serializer.loads(serializer, serializer.dumps(serializer, example_class_2))
        assert dir(res) == dir(example_class_2)
        assert res.a == example_class_2.a
        assert res.c == example_class_2.c

        #instances comparison
        assert isinstance(res('~$~'), example_class_2)
        assert res.some_class_func(res) == example_class_2.some_class_func(example_class_2)
        assert res('$').some_class_func() == example_class_2('$').some_class_func()
        assert res('a string').e == example_class_2('a string').e

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_class_3(self, ser_type):
        serializer = create_serializer('json')
        res = serializer.loads(serializer, serializer.dumps(serializer, example_class_3))
        assert dir(res) == dir(example_class_3)
        assert res.static_method() == example_class_3.static_method()
        assert res.class_method() == example_class_3.class_method()

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_class_4(self, ser_type):
        serializer = create_serializer('json')
        res = serializer.loads(serializer, serializer.dumps(serializer, example_class_4))
        assert dir(res) == dir(example_class_4)

    # @pytest.mark.parametrize('ser_type', yaml)
    # def test_Metaclass_1(self, ser_type):
    #     serializer = create_serializer(ser_type)
    #     res = serializer.loads(serializer, serializer.dumps(serializer, example_Metaclass_1))
    #     assert dir(res) == dir(example_Metaclass_1)

    #     # instances comparison
    #     res_instance = res('Name', (), {'field': 'just a field'})
    #     res_instance = serializer.loads(serializer, serializer.dumps(serializer, res_instance))
    #     assert dir(res_instance) == dir(example_Metaclass_1('Name', (), {'field': 'just a field'}))

    # @pytest.mark.parametrize('ser_type', yaml)
    # def test_Metaclass_2(self, ser_type):
    #     serializer = create_serializer(ser_type)
    #     res = serializer.loads(serializer, serializer.dumps(serializer, example_Metaclass_2))
    #     assert dir(res) == dir(example_Metaclass_2)

    #     # instances comparison
    #     res_instance = res()
    #     res_instance = serializer.loads(serializer, serializer.dumps(serializer, res_instance))
    #     assert dir(res_instance) == dir(example_Metaclass_2())


class TestWithFile():
    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_class_1(self, ser_type):
        ser_type='json'
        serializer = create_serializer(ser_type)
        serializer.dump(serializer, example_class_1, f'results/class_1.{ser_type}')
        res = serializer.load(serializer, f'results/class_1.{ser_type}')
        assert dir(res) == dir(example_class_1)
        assert res.a == example_class_1.a
        assert res.c == example_class_1.c

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_instance_1(self, ser_type):
        ser_type='json'
        serializer = create_serializer(ser_type)
        serializer.dump(serializer, example_instance_1, f'results/instance_1.{ser_type}')
        res = serializer.load(serializer, f'results/instance_1.{ser_type}')
        assert dir(res) == dir(example_instance_1)
        assert res.a == example_instance_1.a
        assert res.b == example_instance_1.b
        assert res.c == example_instance_1.c
        assert res.d == example_instance_1.d
        assert isinstance(res, example_class_1)

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_class_2(self, ser_type):
        ser_type='json'
        serializer = create_serializer(ser_type)
        serializer.dump(serializer, example_class_2, f'results/class_2.{ser_type}')
        res = serializer.load(serializer, f'results/class_2.{ser_type}')
        assert dir(res) == dir(example_class_2)
        assert res.a == example_class_2.a
        assert res.c == example_class_2.c
        # instances comparison
        assert isinstance(res('~$~'), example_class_2)
        assert res.some_class_func(res) == example_class_2.some_class_func(example_class_2)
        assert res('$').some_class_func() == example_class_2('$').some_class_func()
        assert res('a string').e == example_class_2('a string').e

    @pytest.mark.parametrize('ser_type', serializer_types)
    def test_convert_format(self, ser_type):
        json_serializer = create_serializer('json')
        yaml_serializer = create_serializer('json')

        res = json_serializer.load(json_serializer, 'results/class_2.json', False)
        yaml_serializer.dump(yaml_serializer, res, 'results/converted_class_2.yaml', False)

        res = yaml_serializer.load(yaml_serializer, 'results/class_2.json', False)
        json_serializer.dump(json_serializer, res, 'results/converted_class_2.json', False)

        obj1 = json_serializer.load(json_serializer, 'results/converted_class_2.json')
        obj2 = yaml_serializer.load(yaml_serializer, 'results/converted_class_2.json')

        assert dir(obj1) == dir(obj2)