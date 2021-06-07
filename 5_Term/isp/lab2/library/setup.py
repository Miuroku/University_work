from setuptools import setup, find_packages

setup(
    name='serializer_lib',
    packages=find_packages(),
    version='0.1.0',
    description='Library for serialization/deserialization',
    author='Miuroku Turoma',
    license='MIT',
    install_requires=['pyyaml', 'toml'],
    python_requires='>=3.8',
)