from solutions.CHK import checkout_solution
import unittest

class TestSum(unittest.TestCase):
    def test_add(self):
        self.assertEqual(checkout_solution.checkout("A"), 50)

