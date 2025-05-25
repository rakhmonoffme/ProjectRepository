from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path:str) -> list[str]:
    """
    This function reads a requirements file and returns a list of packages.
    """
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  # read lines from the fil
        requirements = [req.replace('\n',"") for req in requirements]  # Remove any whitespace characters like `\n` at the end of each line
        if HYPEN_E_DOT in requirements:  # if '-e .' is in the requirements, remove it
            requirements.remove(HYPEN_E_DOT)
        
    return requirements  #  return the list of packages
    
HYPEN_E_DOT = '-e .'
setup (
    name = "VirtualEnvironmentCreation",
    version = "0.1.0",
    author = "rakhmonoff",
    author_email = "boburshakh1998@gmail.com",
    description = "A simple script to create a virtual environment and install packages",

    packages = find_packages(),
    # install_requires = ['pandas', 'numpy', 'scikit-learn', 'matplotlib', 'seaborn'],
    install_requires = get_requirements('requirements.txt'),
    
) 