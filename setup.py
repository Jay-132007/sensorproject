from setuptools import find_packages,setup
from typing import List

"""
trigger setup.py using req.txt : write -e. in req.txt ---> run req.txt

hence -e. is not a package : when we run setup.py it should be removed 
"""

hypen_e= '-e.' # variable 


def get_requirements(file_path:str)->List[str]:
    requirements =[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]

    if hypen_e in requirements:
        requirements.remove(hypen_e)
    return requirements


setup(
name='fault detection',
version='0.0.1',
author='jay nadkarni',
author_email='nadkarnijay14@gmail.com',
install_requires=get_requirements('requirements.txt'),
packages=find_packages()
)