from setuptools import find_packages, setup

setup(name='ballpark-fixed',
    description='Better human-readable numbers. Forked and fixed from Stijn',
    long_description=open('README.rst').read(),
    author='Endlessz',
    author_email='lckrep@protonmail.com',
    url='https://github.com/Endlesszombiez/python-ballpark',
    version='1.4.0',
    license='ISC',
    packages=find_packages(),
    keywords='human numbers format notation scientific engineering',
    install_requires=[],
    test_suite='ballpark.tests',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.10'
        ],
    )
