"""The REPL (read-eval-print loop) for Tetra. It's an interactive shell where you can run code in the same enivronment."""
from .tetra import Interpreter
import traceback

class Repl:
    def __init__(self):
        self.interpreter = Interpreter("", True)
    
    def run(self):
        while True:
            code = input(">>> ")

            if not code:
                continue
            self.interpreter.source = code
            try:
                result = self.interpreter.run()
                print(result)
            except Exception :
                print(traceback.format_exc())