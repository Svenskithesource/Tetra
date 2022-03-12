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