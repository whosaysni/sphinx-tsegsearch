"""Sphinx extension to split searchword with TinySegmenter',
"""
from setuptools import setup, find_packages
from codecs import open
from os import path
import sys


setup(
    name='sphinx-tsegsearch',
    version='1.1',
    description='Sphinx extension to split searchword with TinySegmenter',
    long_description=sys.modules['__main__'].__doc__,
    url='https://github.com/whosaysni/sphinx-tsegsearch',
    author='Yasushi Masuda',
    author_email='whosaysni@gmail.com',
    license='MIT',
    platforms='any',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation :: Sphinx',
    ],
    keywords='sphinx, japanese, word segmentation, search',
    packages=['sphinx_tsegsearch'],
    package_dir={'sphinx_tsegsearch': 'sphinx_tsegsearch'},
    package_data={
        'sphinx_tsegsearch': ['static/*', 'templates/*'],
    },
    install_requires=['docutils', 'sphinx']
)
