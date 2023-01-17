# pylint: disable=missing-docstring
from setuptools import setup
from hyrule_builder_plus.__version__ import VERSION

with open("README.md", "r") as readme:
    LONG = readme.read()


setup(
    name='hyrule_builder_plus',
    version=VERSION,
    author='SDarkMagic',
    author_email='TheSDarkMagic@gmail.com',
    description='A modified version of the hyrule_builder package to serve as an advanced module in other projects.',
    long_description=LONG,
    long_description_content_type='text/markdown',
    url='https://github.com/Relics-Of-The-Past/Hyrule-Builder',
    include_package_data=True,
    packages=['hyrule_builder_plus'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3 :: Only'
    ],
    python_requires='>=3.7',
    install_requires=[
        'botw-utils>=0.2.3',
        'oead~=1.2.0',
        'pymsyt>=0.3.2,<0.4.0',
        'rstb>=1.2.1',
        'xxhash~=1.4.3'
    ]
)
