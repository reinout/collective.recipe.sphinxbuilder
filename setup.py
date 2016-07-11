# -*- coding: utf-8 -*-
"""
This module contains the tool of collective.recipe.sphinxbuilder
"""
import codecs
import os
from setuptools import setup, find_packages


def read(*rnames):
    filename = os.path.join(os.path.dirname(__file__), *rnames)
    try:
        with codecs.open(filename, encoding='utf-8') as f:
            return unicode(f.read())
    except NameError:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()


version = '1.0'

long_description = u'\n\n'.join([
    read('README.rst'),
    'Detailed Documentation\n' +
    '**********************\n',
    read('src', 'collective', 'recipe', 'sphinxbuilder', 'docs', 'about_sphinx.rst'),
    read('src', 'collective', 'recipe', 'sphinxbuilder', 'docs', 'quick_start.rst'),
    read('src', 'collective', 'recipe', 'sphinxbuilder', 'docs', 'options.rst'),
    read('src', 'collective', 'recipe', 'sphinxbuilder', 'docs', 'usage.rst'),
    read('src', 'collective', 'recipe', 'sphinxbuilder', 'docs', 'contributors.rst'),
    read('src', 'collective', 'recipe', 'sphinxbuilder', 'docs', 'history.rst')
    ])


setup(name='collective.recipe.sphinxbuilder',
      version=version,
      description="ZC.buildout recipe to generate and build Sphinx-based documentation in the buildout.",
      long_description=long_description,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Zope Public License',
        ],
      keywords='buildout sphinx',
      author='Tarek Ziade',
      author_email='tarek@ziade.org',
      url='https://github.com/sdouche/collective.recipe.sphinxbuilder',
      license='ZPL',
      packages = find_packages('src', exclude=['ez_setup']),
      package_dir = {'':'src'},
      namespace_packages=['collective', 'collective.recipe'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
            'setuptools',
            'zc.buildout',
            'zc.recipe.egg',
            'docutils',
            'Sphinx>=1.1'],
      tests_require=['zope.testing', 'zc.buildout', 'manuel'],
      extras_require=dict(tests=['zope.testing', 'zc.buildout', 'manuel']),
      test_suite = 'collective.recipe.sphinxbuilder.tests.test_docs.test_suite',
      entry_points = {"zc.buildout": ["default = collective.recipe.sphinxbuilder:Recipe"]}
      )

# python setup.py --long-description | rst2html.py > /dev/null
