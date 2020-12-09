
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="xml_to_dict",
    version="0.1.6",
    author="Ezequiel M. Iglesias",
    author_email="ezequiel.m.iglesias@gmail.com",
    description="A simple Python XML to Dictionary parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xthehatterx/xml_to_dict",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT',
    python_requires='>=3.6'
)
