from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n',"") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='Unsupervised_end_to_end_Project',
    version='1.0',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    author='Samrat Kumar Dev Sharma',
    author_email='samratdev151@gamil.com',
    description='A short description of your project',
    url='https://github.com/samrat1699/Unsupervised_end_to_end_Project',
)
