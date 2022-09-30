import pydrawio
from setuptools import setup, find_packages

DESCRIPTION = 'pydrawio: manage draw.io file'
NAME = 'pydrawio'
AUTHOR = 'Naoto Kageyama'
AUTHOR_EMAIL = 'rencker3@gmail.com'
URL = 'https://github.com/capybara-alt/pydrawio'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/capybara-alt/pydrawio'
VERSION = pydrawio.__version__
PYTHON_REQUIRES = '>=3.7'

PACKAGES = [
    'core',
    'pydrawio'
]

CLASSIFIERS = [
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
]

with open('README.md', 'r') as fp:
    readme = fp.read()
long_description = readme

setup(
      name=NAME,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=AUTHOR,
      maintainer_email=AUTHOR_EMAIL,
      description=DESCRIPTION,
      long_description=long_description,
      long_description_content_type='text/markdown',
      license=LICENSE,
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      python_requires=PYTHON_REQUIRES,
      packages=PACKAGES,
      classifiers=CLASSIFIERS
)
