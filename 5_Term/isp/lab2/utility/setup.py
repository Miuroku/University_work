from setuptools import setup, find_packages

setup(
    name='make_convertion',
    # packages=[
    #     'serializer_lib.objects_packager', 
    #     'serializer_lib.factory',
    #     'serializer_lib.serializers',
    # ],
    packages=find_packages(exclude=['tests']),
    version='0.2.0',
    description='Console serializer',
    author='Miuroku Turoma',
    install_requires=[],
    scripts=['bin/make_conversion']
)