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

    def test_init(self):
        """test with given properties"""
        r = Rectangle(10, 5, 2, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)
        
    def test_notInteger(self):
        """test when args are not ints"""
        self.assertRaisesRegex(
            TypeError, "width must be an integer", Rectangle, "1", 2)
        self.assertRaisesRegex(
            TypeError, "height must be an integer", Rectangle, 1, "2")
        self.assertRaisesRegex(
            TypeError, "x must be an integer", Rectangle, 1, 2, "3")
        self.assertRaisesRegex(
            TypeError, "y must be an integer", Rectangle, 1, 2, 3, "4")

    def test_valueError(self):
        """tests when is int but no valid values"""
        self.assertRaisesRegex(
            ValueError, "width must be > 0", Rectangle, -5, 9)
        self.assertRaisesRegex(
            ValueError, "height must be > 0", Rectangle, 5, -9)
        self.assertRaisesRegex(
            ValueError, "width must be > 0", Rectangle, 0, 9)
        self.assertRaisesRegex(
            ValueError, "height must be > 0", Rectangle, 5, 0)
        self.assertRaisesRegex(
            ValueError, "x must be >= 0", Rectangle, 1, 2, -3)
        self.assertRaisesRegex(
            ValueError, "y must be >= 0", Rectangle, 1, 2, 3, -4)
