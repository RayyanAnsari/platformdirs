#!/usr/bin/env python
import os
import ast
from setuptools import setup


def read(fname):
    inf = open(os.path.join(os.path.dirname(__file__), fname), encoding='utf8')
    out = "\n" + inf.read().replace("\r\n", "\n")
    inf.close()
    return out


# Do not import `platformdirs` yet, lest we import some random version on sys.path.
for line in read("platformdirs.py").splitlines():
    if line.startswith("__version__"):
        version = ast.literal_eval(line.split("=", 1)[1].strip())
        break


setup(
    name='platformdirs',
    version=version,
    description='A small Python module for determining appropriate ' + \
        'platform-specific dirs, e.g. a "user data dir".',
    long_description=read('README.rst') + '\n' + read('CHANGES.rst'),
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='application directory log cache user',
    author='Trent Mick',
    author_email='trentm@gmail.com',
    maintainer='Jeff Rouse',
    maintainer_email='jr@its.to',
    url='https://github.com/platformdirs/platformdirs',
    license='MIT',
    py_modules=["platformdirs"],
)
