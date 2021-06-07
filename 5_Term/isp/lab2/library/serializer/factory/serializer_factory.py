from serializers.json_serializer import JsonSerializer
from serializers.yaml_serializer import YamlSerializer
from serializers.pickle_serializer import PickleSerializer
from serializers.toml_serializer import TomlSerializer

serializers = {
    'json': JsonSerializer,
    'yaml': YamlSerializer,
    "pickle": PickleSerializer,
    'toml': TomlSerializer
}

def create_serializer(format_of_file):
    '''
    Main function wich returns a serializer depends on file format that was as argument.
    '''
    parser = serializers.get(format_of_file.lower(), None)
    if parser is None:
        raise ValueError(f'That file format "{format_of_file}" could not be parsed .')

    return parser