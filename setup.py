from setuptools import setup, find_packages
from typing import List

def get_requirements(filename:str) -> List[str]:
    requirements = []

    with open(filename) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")
        
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author='Faith Bamidele',
    author_email='bamidelefaith10@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements("requirements.txt")
)