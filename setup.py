from setuptools import setup, find_packages

setup(
    name='free_verify_proxy',
    version='1.1.5',
    author='Mominur Rahman',
    author_email='mominurr518@email.com',
    description='A simple package to provide http and https working proxy lists.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mominurr/free_verify_proxy',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
