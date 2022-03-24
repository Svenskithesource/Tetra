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
To run the REPL
```
$ tetra
No file specified. Starting REPL.
>>>
 ```
### Unitests
To run the unitests do:

`python -m unittest tests.test_tetra`

## Syntax
### Typing
Tetra is a dynamically typed language so you don't need to specify what type a variable is. For now there's also not an option to show what type a var is.

### Expressions
Expressions can contain math, variables. You can assign expressions to variables.

Math example:

```
1 + 1
```

Parentheses are also supported:

```
(1 + 1)*3
```

When you want to save an expression in a variable you can do like so:

```
a = 1 + 1
```

Because expressions can contain variables you can do

```
a = 1 + 1
b = a + 3
````
