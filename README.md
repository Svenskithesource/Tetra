# Tetra
### Introduction
A basic interpreted language, written in Python!
### Installation
You can clone the repo and then install it locally.
```bash
git clone https://github.com/Svenskithesource/Tetra
cd Tetra
pip3 install -e .
```
### Usage
```
$ tetra -h
An interpreter for the tetra language.

positional arguments:
  filepath    The source file to run.

optional arguments:
  -h, --help  show this help message and exit
  -d, --dump  Print the top item on the stack after execution.
 ```
### Unitests
To run the unitests do:

`python -m unittest tests.test_tetra`
