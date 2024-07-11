from unittest import TestCase
from models.base import Base


class TestBaseClass(TestCase):

    def setUp(self):
        self.b1 = Base()
        self.b2 = Base(90)
        self.b3 = Base(-1)
        self.b4 = Base(0)
        self.b5 = Base(100)
        self.b6 = Base()

    def test_id(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 90)
        self.assertEqual(self.b3.id, -1)
        self.assertEqual(self.b4.id, 0)
        self.assertEqual(self.b5.id, 100)
        self.assertEqual(self.b6.id, 2)
