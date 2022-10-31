from setuptools import setup, find_namespace_packages

setup(
    name='sort_folder',
    version='1.0.0',
    description='Sort files in a folder',
    author='Vitalii Kyivskyi',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['sort=sort_folder.sort:start_program']}
)
