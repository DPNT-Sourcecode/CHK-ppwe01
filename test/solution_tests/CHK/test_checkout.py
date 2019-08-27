from solutions.CHK import checkout_solution
import unittest

class TestSum(unittest.TestCase):
    def test_add(self):
        self.assertEqual(checkout_solution.checkout("A"), 50)
        self.assertEqual(checkout_solution.checkout("A,B"), 80)
        self.assertEqual(checkout_solution.checkout("A,B,C"), 100)


