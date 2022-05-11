import unittest
from Logic import *


class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(one(6), 21)

        with self.assertRaises(TypeError):
            one('string')
            one(4.5)

        with self.assertRaises(ValueError):
            one(0)
            one(-1)

    def test_two(self):
        self.assertEqual(two(2, 3), 8)

        with self.assertRaises(TypeError):
            two(2, 'string')
            two('string', 3)
            two('string', 'string')
            two(2.5, 3)
            two(2, 3.5)
            two(2.5, 3.5)

        with self.assertRaises(ValueError):
            two(0, 3)
            two(2, 0)
            two(0, 0)
            two(-2, 3)
            two(2, -3)
            two(-2, -3)

    def test_three(self):
        self.assertEqual(three(10), 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)

        with self.assertRaises(TypeError):
            three('string')
            three(4.5)

        with self.assertRaises(ValueError):
            three(0)
            three(-5)
