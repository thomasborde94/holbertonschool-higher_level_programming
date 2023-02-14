#!/usr/bin/python3
"Unit tests for Rectangle class"
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """tests for class rectangle"""

    def test_initialization(self):
        """test of rectangle with default init"""
        r = Rectangle(10, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        r2 = Rectangle(10, 5, 0, 0, 8)
        self.assertEqual(r2.id, 8)
