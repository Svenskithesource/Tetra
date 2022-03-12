import unittest
import tetra

class TestTetra(unittest.TestCase):
    def test_all(self):
        self.assertEqual(tetra.Interpreter("1 + 2 * 3").run(), 7)

    def test_div(self):
        self.assertEqual(tetra.Interpreter("1 / 2").run(), 0) # will be 0 because of floor division