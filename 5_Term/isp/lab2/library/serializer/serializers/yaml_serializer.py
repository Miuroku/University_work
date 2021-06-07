#import warnings
from yaml import dump, load
from objects_packager.packer_unpacker import Packer, Unpacker
from serializers.base_serializer import BaseSerializer

#warnings.filterwarnings("ignore")

class YamlSerializer(BaseSerializer):
    base_dumps = dump
    base_loads = load

    def dump(self, obj: object, file: object = None, pack=True):        
        if pack:
            packed_obj = Packer().from_object_to_dictionary(obj)
        else:
            packed_obj = obj

        if file:
            with open(file, 'w') as file:
                file.write(YamlSerializer.base_dumps(packed_obj))
        else:
            raise ValueError("File isn't correct.")


    def dumps(self, obj: object):        
        packed_obj = Packer().from_object_to_dictionary(obj)
        return YamlSerializer.base_dumps(packed_obj)

    def load(self, file: object, unpack=True):
        if file:
            with open(file, 'r') as file:
                try:
                    raw_obj = YamlSerializer.base_loads(file.read())
                except Exception:
                    raise ValueError('Invalid yaml format...')

            if unpack:
                return Unpacker().from_dict_to_object(raw_obj)
            else:
                return raw_obj
        else:
            raise ValueError("File isn't correct.")


    def loads(self, yaml: str):        
        try:
            raw_obj = YamlSerializer.base_loads(yaml)
        except Exception:
            raise ValueError('Invalid yaml format...')

        unpacked_obj = Unpacker().from_dict_to_object(raw_obj)
        return unpacked_obj