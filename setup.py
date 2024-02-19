from setuptools import find_packages, setup

# local installation code
setup(
    name = 'wasteDetection',
    version = '0.0.0',
    author = 'Piyush',
    author_email='',
    packages = find_packages(),
    # find_pack will find the const file in every folder.
    # try to install that pack as the local folder.
    install_requires = []
)