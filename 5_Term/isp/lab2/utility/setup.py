from setuptools import setup, find_packages

setup(
    name='make_convertion',
    packages=[
        'objects_packager', 
        'factory',
        'serializers',
    ],
    version='0.2.0',
    description='Console serializer',
    author='Miuroku Turoma',
    install_requires=[],
    scripts=['bin/make_convertion']
)