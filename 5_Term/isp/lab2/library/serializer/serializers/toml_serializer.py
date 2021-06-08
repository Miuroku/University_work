from typing import Any
from library.serializer.serializers.base_serializer import BaseSerializer
from library.serializer.objects_packager.packer_unpacker import Packer, Unpacker
#from toml import dumps, loads
from library.serializer.parsers.toml_parser import dump, dumps, load, loads

class TomlSerializer(BaseSerializer):
    base_dumps = dumps
    base_loads = loads

    # 'pack' parameter is useful when we use utility.
    def dump(self, obj: object, file: object = None, pack=True) -> None:        
        dump(obj, file)

    def dumps(self, obj: object) -> None:        
        dumps(obj)

    # 'unpack' parameter is useful when we use utility.
    def load(self, file: object, unpack=True) -> Any:
        load(file)

    def loads(self, format_string: str) -> Any:        
        loads(temp_str)