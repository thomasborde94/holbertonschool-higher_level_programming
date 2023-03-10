#!/usr/bin/python3
"Unit tests for Rectangle class"
import unittest
from models.rectangle import Rectangle
from io import StringIO
from contextlib import redirect_stdout
import os


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

    def test_area(self):
        """test of area function"""
        r = Rectangle(10, 10)
        self.assertEqual(r.area(), 100)

    def test_str(self):
        """test of str func"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_display(self):
        """test of display func"""
        r1 = Rectangle(3, 2)
        expected_output = '###\n###\n'
        with StringIO() as buffer, redirect_stdout(buffer):
            r1.display()
            result = buffer.getvalue()
        self.assertEqual(result, expected_output)

        r2 = Rectangle(3, 2, 1, 1)
        expected_output = '\n ###\n ###\n'
        with StringIO() as buffer, redirect_stdout(buffer):
            r2.display()
            result = buffer.getvalue()
        self.assertEqual(result, expected_output)

        r5 = Rectangle(3, 2, 1, 1, 89)
        expected_output = '\n ###\n ###\n'
        with StringIO() as buffer, redirect_stdout(buffer):
            r5.display()
            result = buffer.getvalue()
        self.assertEqual(result, expected_output)

    def test_update(self):
        """Tests if Rectangle's update() exists and updates the right args"""
        r = Rectangle(10, 20, 30, 40, 50)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_dictionary(self):
        """test to dictionary func for rectangle"""
        s1 = Rectangle(10, 2, 1, 9)
        s1_dict = s1.to_dictionary()
        self.assertEqual(s1_dict, {'x': 1, 'y': 9, 'id': 5,
                                   'height': 2, 'width': 10})
        s2 = Rectangle(1, 2)
        s2_dict = s2.to_dictionary()
        self.assertEqual(s2_dict, {'x': 0, 'y': 0, 'id': 6,
                                   'height': 2, 'width': 1})

    def test_create_rectangle(self):
        """test of create function for rectangle"""
        r = Rectangle.create(**{"id": 89, "width": 10, "height": 12, "x": 2, "y":3})
        r2 = Rectangle(10, 12, 2, 3, 89)
        self.assertEqual(str(r), str(r2))

    def test_save_to_file(self):
        r5 = Rectangle(5, 3, 2, 3, 50)
        r6 = Rectangle(2, 4)
        Rectangle.save_to_file([r5, r6])
        with open("Rectangle.json", "r") as f:
            r8 = f.read()
        r7 = '[{"id": 50, "width": 5, "height": 3, "x": 2, "y": 3}, \
{"id": 11, "width": 2, "height": 4, "x": 0, "y": 0}]'
        self.assertEqual(r7, r8)

    def test_save_to_file(self):
        """
        Test save file
        """
        r = Rectangle(2, 4, 0, 0, 18)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            data_read = f.read()
        expect_output = '[{"id": 18, "width": 2, "height": 4, "x": 0, "y": 0}]'
        self.assertEqual(data_read, expect_output)
        os.remove("Rectangle.json")

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            data_read = f.read()
        expect_output = '[]'
        self.assertEqual(data_read, expect_output)
        os.remove("Rectangle.json")

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            data_read = f.read()
        expect_output = '[]'
        self.assertEqual(data_read, expect_output)
        os.remove("Rectangle.json")

    def test_load_from_file(self):
        """
        Test load file
        """
        r1 = Rectangle(4, 6)
        Rectangle.save_to_file([r1])
        rectangles = Rectangle.load_from_file()
        self.assertIsInstance(rectangles[0], Rectangle)
        self.assertEqual(rectangles[0].width, 4)
        self.assertEqual(rectangles[0].height, 6)
        os.remove("Rectangle.json")

        r = Rectangle.load_from_file()
        self.assertTrue(isinstance(r, list))
        self.assertEqual(r, [])
