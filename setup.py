from setuptools import find_packages,setup

from typing import List


Hypen_e_dot='-e.'

# going through each items in the requirements.txt to get the items to be installed 
def get_requirements(filepath: str)-> List[str]:

    requirements=[]

    with open(filepath) as file_obj:
        requirements=file_obj.readlines()

        requirements=[req.replace("\n","") for req in requirements ]

        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)
    requirements.remove('-e .')
    print(requirements)
    return requirements 

# this will create packages of my project like any package in python , this will get automatically get triggered due to -e. in requiremets.txt 
setup(
    name='End-To-End-Machine-Learning-Project',
    version='0.0.1',
    author='Anirudh1731',
    author_email='anirudhsanthosh1729@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)