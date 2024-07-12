#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle

"""Testing Rectangle class with unittest
"""

class TestRectangleClass(unittest.TestCase):

    def setUp(self):
        self.r1 = Rectangle(0, 0)
        self.r2 = Rectangle(-1, -2)
        self.r3 = Rectangle(100, 100, 50, 50, 30)
        self.r4 = Rectangle(104, 104, 90, 90, 777)
        self.B5 = Base(90)

    def test_inheritance(self):
        self.assertIsInstance(self.r1, Base)
        self.assertIsInstance(self.r2, Rectangle)
        self.assertTrue(issubclass(Rectangle, Base))

    def test_id(self):
        self.assertEqual(self.r1.id, 1)
        self.assertTrue(self.r2.id == 2)
        self.assertNotEqual(self.r3.id, 3)
        self.assertEqual(self.r4.id, 777)
        self.assertEqual(self.B5.id, 90)

    def test_widheightxy(self):
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r2.width, -1)
        self.assertEqual(self.r3.x, 50)
        self.assertEqual(self.r3.y, 50)
        self.assertEqual(self.r3.width, 100)
        self.assertEqual(self.r3.height, 100)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRectangleClass)
    unittest.TextTestRunner(verbosity=2).run(suite)
