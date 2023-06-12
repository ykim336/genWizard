
from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='genMake',
    version='0.0.1',
    description='genMake allows for versatile usage of openAI generation and prompting management.',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
    url='https://github.com/ykim336/genMake',
    license='MIT',
    classifiers=classifiers,
    keywords='machine learning',
    author='Isaac Moon',
    author_email='ykim336@ucr.com',
    packages=find_packages(),
    install_requires=['List your dependencies here']
)

