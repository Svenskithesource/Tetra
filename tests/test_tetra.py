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
        self.assertEqual(tetra.Interpreter("1 + 20").run(), 21)
    
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

        interpreter = tetra.Interpreter('a = "hello"')
        interpreter.run()
        self.assertEqual(interpreter.heap[0], "hello")
        self.assertEqual(interpreter.code.vars[0], "a")
    
    def test_mutliline(self):
        interpreter = tetra.Interpreter("1+ 1\n4*5")
        result = interpreter.run()
        self.assertEqual(result, 20)
        self.assertEqual(interpreter.stack[-1], 2) # It will be the last element of the stack since the top element will already be popped off the stack after the program is executed
    
    def test_var_storing(self):
        interpreter = tetra.Interpreter("a = 1 + 1")
        interpreter.run()
        self.assertEqual(interpreter.heap[0], 2)
        self.assertEqual(interpreter.code.vars[0], "a")

    def test_var_loading(self):
        interpreter = tetra.Interpreter("a = 1 + 1\na")
        result = interpreter.run()
        self.assertEqual(result, 2)

        interpreter = tetra.Interpreter('a = "hello"\na')
        result = interpreter.run()
        self.assertEqual(result, "hello")

        interpreter = tetra.Interpreter("a = 1 + 1\nb")
        with self.assertRaises(SystemExit):
            interpreter.run()

        interpreter = tetra.Interpreter("a = 1 + 1\na = b + 3")
        with self.assertRaises(SystemExit):
            interpreter.run()

    def test_var_overwrite(self):
        self.assertEqual(tetra.Interpreter("a = 1\na = 2\na").run(), 2)
        self.assertEqual(tetra.Interpreter('a = "hello"\na = "hi"\na').run(), "hi")

    def test_var_with_var(self):
        self.assertEqual(tetra.Interpreter("a = 1\na = a + 2\na").run(), 3)

    def test_empty_input(self):
        with self.assertRaises(SystemExit):
            tetra.Interpreter("").run()

    def test_load_string(self):
        self.assertEqual(tetra.Interpreter("\"Hello\"").run(), "Hello")
    def test_braces(self):
        self.assertEqual(tetra.Interpreter("if (0+1) {1 + 1}").run(), 2)