import unittest
from main import remainder

class TestMath(unittest.TestCase):
    def test_remainder(self):
        self.assertEqual(remainder(10, 3), 1)   # 10 % 3 = 1
        self.assertEqual(remainder(20, 5), 0)   # 20 % 5 = 0
        self.assertEqual(remainder(7, 4), 3)    # 7 % 4 = 3
        self.assertEqual(remainder(15, 7), 1)   # 15 % 7 = 1
        self.assertEqual(remainder(-10, 3), 2)  # -10 % 3 = 2 (Python rule)
        self.assertEqual(remainder(10, -3), -2) # 10 % -3 = -2 (Python rule)
        self.assertEqual(remainder(-10, -3), -1) # -10 % -3 = -1 (Python rule)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            remainder(10, 0)

if __name__ == '__main__':
    unittest.main()
