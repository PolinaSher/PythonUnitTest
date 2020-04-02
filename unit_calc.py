import unittest
from youtube.calc import Calculator


class TestCalc(unittest.TestCase):

   def test_add(self):
       calculator = Calculator()
       result = calculator.add(operanda=2, operandb=3)
       self.assertEqual(result, 5, "Addition failed")
       
   def test_subtract(self):
        calculator = Calculator()
        result = calculator.subtract(5, 3)
        self.assertEqual(result, 2)