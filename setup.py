"""Install packages as defined in this file into the Python environment."""
from setuptools import setup, find_packages

setup(
    name="diploma_nm-s",
    author="andinoriel",
    author_email="simonnikolaj20@gmail.com",
    url="https://github.com/andinoriel/diploma_nm-s",
    description="simple web server for diploma module:network",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "setuptools>=45.0",
        "falcon>=3.0.0",
        "requests>=2.25.1",
    ],
    entry_points={
        "console_scripts": [
            "diploma_nm-s=diploma_nm-s.__main__:main",
        ]
    },
)
