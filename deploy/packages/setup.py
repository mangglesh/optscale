import setuptools
from setuptools import setup
import version
from pathlib import Path

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#") and not "."]

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_requires = parse_requirements("./requirements.txt")

print(Path(__name__).resolve().parent.name)

name = Path(__name__).resolve().parent.name

setup(
   name=name,
   version=version.__VERSION__,
   author='pollux',
   author_email='nudgebee@pollux.in',
   #packages=['Watermarkd'],
   install_requires=[str(ir.req) for ir in install_requires],
   python_requires='>=3.6'
)