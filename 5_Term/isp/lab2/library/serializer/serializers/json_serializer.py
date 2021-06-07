from typing import Any
from serializers.base_serializer import BaseSerializer
from objects_packager.packer_unpacker import Packer, Unpacker
from json import dumps, loads


class JsonSerializer(BaseSerializer):
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
                file.write(JsonSerializer.base_dumps(packed_obj))
        else:
            raise ValueError("File transfer aborted")

    def dumps(self, obj: object) -> None:        
        packed_obj = Packer().from_object_to_dictionary(obj)
        return JsonSerializer.base_dumps(packed_obj)

    # 'unpack' parameter is useful when we use utility.
    def load(self, file: object, unpack=True) -> Any:
        if file:
            with open(file, 'r') as file:
                try:
                    raw_obj = JsonSerializer.base_loads(file.read())
                except Exception:
                    raise ValueError('Invalid json format...')

            if unpack:
                return Unpacker().from_dict_to_object(raw_obj)
            else:
                return raw_obj
        else:
            raise ValueError("File not found.")

    def loads(self, json: str) -> Any:        
        try:
            raw_obj = JsonSerializer.base_loads(json)
        except Exception:
            raise ValueError('Invalid json format...')

        unpacked_obj = Unpacker().from_dict_to_object(raw_obj)
        return unpacked_obj