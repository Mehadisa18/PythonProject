import unittest
from Unittests import circle_area
from math import pi
"""
run this file by the following command:
python -m unittest filename
"""
class Testcirclearea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(0),0)
        self.assertAlmostEqual(circle_area(1),pi)
    def test_value(self):
        self.assertRaises(ValueError,circle_area,-2)
    def test_type(self):
        self.assertRaises(TypeError,circle_area,3+4j)
        self.assertRaises(TypeError,circle_area,True)
        self.assertRaises(TypeError,circle_area,"radius")