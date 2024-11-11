from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e.'
def get_requirements(filePath:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirement=[]
    
    with open(filePath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlProject',
    version='0.0.1',
    author='Rohit',
    author_email='rohitmotwani102@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)