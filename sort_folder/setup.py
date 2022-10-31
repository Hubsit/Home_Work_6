from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0.0',
    description='Sort files in a folder',
    author='Vitalii Kyivskyi',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': [
        'clean-folder=sort_folder.sort:start_program']}
)
