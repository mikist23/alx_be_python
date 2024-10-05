# import unittest
# from simple_calculator import SimpleCalculator

# class Test(unittest.TestCase):
    
#     def test_add(self):
#         self.assertEqual(SimpleCalculator.add(6, 4), 10)
#         self.assertEqual(SimpleCalculator.add(7, 4), 11)

#     def test_subtract(self):
#         self.assertEqual(SimpleCalculator.subtract(6, 4), 2)
#         self.assertEqual(SimpleCalculator.subtract(7, 4), 3)

#     def test_multiply(self):
#         self.assertEqual(SimpleCalculator.multiply(6, 4), 24)
#         self.assertEqual(SimpleCalculator.multiply(7, 4), 28)

#     def test_divide(self):
#         self.assertEqual(SimpleCalculator.divide(10, 5), 2)
#         self.assertEqual(SimpleCalculator.divide(24, 4), 6)

# if __name__ == '__main__':
#     unittest.main()


import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(6, 4), 2)
        self.assertEqual(self.calc.subtract(7, 4), 3)

    def test_multiplication(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(6, 4), 24)
        self.assertEqual(self.calc.multiply(7, 4), 28)

    def test_division(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(24, 4), 6)
        
        """Test for division by zero."""
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10,0)
