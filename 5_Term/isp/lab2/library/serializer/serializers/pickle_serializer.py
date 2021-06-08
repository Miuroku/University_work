from typing import Any
from library.serializer.serializers.base_serializer import BaseSerializer
from library.serializer.objects_packager.packer_unpacker import Packer, Unpacker
#from pickle import dumps, loads
from library.serializer.parsers.pickle_parser import PickleParser

class PickleSerializer(BaseSerializer):
    # base_dumps = dumps
    # base_loads = loads
    base_dumps = PickleParser().dumps
    base_loads = PickleParser().loads

    # 'pack' parameter is useful when we use utility.
    def dump(self, obj: object, file: object = None, pack=True) -> None:        
        PickleParser().dump(obj, file)

    def dumps(self, obj: object) -> None:        
        #packed_obj = Packer().from_object_to_dictionary(obj)
        return PickleParser().dumps(obj)

    # 'unpack' parameter is useful when we use utility.
    def load(self, file: object, unpack=True) -> Any:
        PickleParser().load(file)

    def loads(self, format_string: str) -> Any:        
        PickleParser().loads(format_string)