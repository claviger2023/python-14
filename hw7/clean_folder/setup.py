from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1',
    description='Very useful code',
    url='https://github.com/claviger2023/python-14',
    author='Artem Tykhonov',
    author_email='claviger2006@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
)