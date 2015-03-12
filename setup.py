import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-model2extjs',
    version='0.1',
    packages=['model2extjs'],
    include_package_data=True,
    license='BSD License',  # example license
    description='Simple solution for generating Extjs code from Django models.',
    long_description=README,
    url='http://github.com/django-model2extjs/',
    author='Osvaldo Cobacho Aguilera',
    author_email='ocobacho@gmx.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2
        'Topic :: Extjs :: Dynamic Content :: Code generation',
    ],
)
