import setuptools
from setuptools import setup
from pathlib import Path

from importlib.machinery import SourceFileLoader

def parse_requirements(filename):
    try:
        """ load requirements from a pip requirements file """
        lineiter = (line.strip() for line in open(filename))
        return [line for line in lineiter if line and not line.startswith("#") and not "."]
    except:
        print("requirements not found")
        return []

name = None
for s in Path(__name__).parent.glob("./*"):
    ss = str(s)
    if ss != "setup.py" and ".egg-info" not in ss:
        name = ss
        break
    
print("installing module", name)

version = SourceFileLoader(f"{name}_version", name+"/version.py").load_module()

print("module version >>", version.__VERSION__)

install_requires = parse_requirements(f"./{name}/requirements.txt")

setup(
   name=name,
   version=version.__VERSION__,
   author='pollux',
   author_email='nudgebee@pollux.in',
   #package_dir={name: "../"+name},
   packages=[name],
   install_requires=[str(ir.req) for ir in install_requires],
   python_requires='>=3.6'
)