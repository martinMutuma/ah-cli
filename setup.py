from setuptools import setup, find_packages

setup(
    name="Ah Cli app",
    version="1.0",
    py_modules=find_packages(),
    install_requires=[
        'click',
        'requests',
        'coveralls',
        'pytest-cov'

    ],
    entry_points={
        'console_scripts': ['ah = src.index:ah']
    }
)
