import unittest
import tetra

class TestTetra(unittest.TestCase):
    def test_all(self):
        self.assertEqual(tetra.Interpreter("1 + 2 * 3").run(), 7)

    def test_div(self):
        self.assertEqual(tetra.Interpreter("1 / 2").run(), 0) # will be 0 because of floor division

    def test_mul(self):
        self.assertEqual(tetra.Interpreter("1 * 2").run(), 2)
        self.assertEqual(tetra.Interpreter("1 * 2 * 3").run(), 6)
    
    def test_add(self):
        self.assertEqual(tetra.Interpreter("1 + 2").run(), 3)
        self.assertEqual(tetra.Interpreter("1 + 2 + 3").run(), 6)
    
    def test_sub(self):
        self.assertEqual(tetra.Interpreter("1 - 2").run(), -1)
        self.assertEqual(tetra.Interpreter("1 - 2 - 3").run(), -4)

    def test_paran(self):
        self.assertEqual(tetra.Interpreter("(1) + (2)").run(), 3)
        self.assertEqual(tetra.Interpreter("(1 + 2) * 3").run(), 9)
    
    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            tetra.Interpreter("1 / 0").run()

    def test_var(self):
        interpreter = tetra.Interpreter("a = 1")
        interpreter.run()
        self.assertEqual(interpreter.heap[0], 1)
        self.assertEqual(interpreter.code.vars[0], "a")
    
    def test_mutliline(self):
        interpreter = tetra.Interpreter("1+ 1\n4*5")
        result = interpreter.run()
        self.assertEqual(result, 20)
        self.assertEqual(interpreter.stack[-1], 2) # It will be the last element of the stack since the top element will already be popped off the stack after the program is executed
    
    def test_var_loading(self):
        interpreter = tetra.Interpreter("a = 1 + 1\na")
        result = interpreter.run()
        self.assertEqual(result, 2)

        interpreter = tetra.Interpreter("a = 1 + 1\nb")
        with self.assertRaises(SyntaxError):
            interpreter.run()

    def test_var_overwrite(self):
        self.assertEqual(tetra.Interpreter("a = 1\na = 2\na").run(), 2)