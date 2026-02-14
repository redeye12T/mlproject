from setuptools import find_packages,setup
from typing import List

hip="-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    Docstring for get_requirements
    
    :param file_path: Description
    :type file_path: str
    :return: Description
    :rtype: List[str]
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if hip in requirements:
            requirements.remove(hip)
    return requirements




setup(
name='mlproject',
version='0.0.1',
author='Thaheer',
author_email='noornayako@gmail.com',
packages=find_packages(),
install_requires=get_requirements("requirements.txt")



)