import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="tetra",
    version="0.0.1",
    author="svenskithesorce & jaxp",
    author_email="nan",
    description="An interpreter for the tetra language.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Svenskithesource/Tetra",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU GPLv3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points = {
        'console_scripts': ['tetra=tetra.cli:main'],
    }
)