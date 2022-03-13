"""
An interpreted language

Created by: svenskithesource (https://github.com/Svenskithesource), Jaxp (https://github.com/jaxp2)
"""

import argparse, os
from .tetra import Interpreter

def file_exists(file_path):
    if not os.path.isfile(file_path):
        raise argparse.ArgumentTypeError(f"{file_path} does not exist.")
    elif not file_path.endswith(".tet"):
        raise argparse.ArgumentTypeError(f"{file_path} is not a .tet file.")
    return file_path

def main():
    parser = argparse.ArgumentParser(description='An interpreter for the tetra language.')
    parser.add_argument('filepath', type=file_exists, help='The source file to run.')
    parser.add_argument('-d', "--dump", action="store_true", help="Print the top item on the stack after execution.")
    args = parser.parse_args()
    with open(args.filepath, "r") as f:
        source = f.read()
        interpreter = Interpreter(source.strip())
        result = interpreter.run()
        if args.dump:
            print(result)
