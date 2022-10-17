import unittest

import calculator

class Testing(unittest.TestCase):
    calc = calculator.Calculator()

    def test_add1(self):
        self.assertEqual(self.calc.add(6, 7), 13)
    
    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(3, 5), 15)

    def test_add2(self):
        self.assertEqual(self.calc.add(1, 1), 3)
    
    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(5, 0), 10)

if __name__ == '__main__':
    unittest.main()
