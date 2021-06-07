from typing import Any
from serializers.base_serializer import BaseSerializer
from objects_packager.packer_unpacker import Packer, Unpacker
from pickle import dumps, loads


class PickleSerializer(BaseSerializer):
    base_dumps = dumps
    base_loads = loads

    # 'pack' parameter is useful when we use utility.
    def dump(self, obj: object, file: object = None, pack=True) -> None:        

        if pack:
            packed_obj = Packer().from_object_to_dictionary(obj)            
        else:
            packed_obj = obj        

        # Check if file exists.
        if file:
            with open(file, 'w') as file:
                file.write(PickleSerializer.base_dumps(packed_obj))
        else:
            raise ValueError("File transfer aborted")

    def dumps(self, obj: object) -> None:        
        packed_obj = Packer().from_object_to_dictionary(obj)
        return PickleSerializer.base_dumps(packed_obj)

    # 'unpack' parameter is useful when we use utility.
    def load(self, file: object, unpack=True) -> Any:
        if file:
            with open(file, 'r') as file:
                try:
                    raw_obj = PickleSerializer.base_loads(file.read())
                except Exception:
                    raise ValueError('Invalid pickle format...')

            if unpack:
                return Unpacker().from_dict_to_object(raw_obj)
            else:
                return raw_obj
        else:
            raise ValueError("File not found.")

    def loads(self, format_string: str) -> Any:        
        try:
            raw_obj = PickleSerializer.base_loads(format_string)
        except Exception:
            raise ValueError('Invalid pickle format...')

        unpacked_obj = Unpacker().from_dict_to_object(raw_obj)
        return unpacked_obj