#!/usr/bin/python3
"Unit tests for Rectangle class"
import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """Testing Square"""

    def test_initialization(self):
        """test of square init"""
        s = Square(10, 5, 3)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 3)
        s2 = Square(3, 8)
        self.assertEqual(s2.size, 3)
        self.assertEqual(s2.x, 8)

    def test_instance(self):
        """test input size correct standard """
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

        with self.assertRaises(TypeError):
            Square(5, "1")

        with self.assertRaises(TypeError):
            Square()

        with self.assertRaises(TypeError):
            Square("1")

        with self.assertRaises(ValueError):
            Square(-5, 3, 4)

        with self.assertRaises(TypeError):
            Square(1, 2, "3")

        with self.assertRaises(ValueError):
            Square(1, -2)

        with self.assertRaises(ValueError):
            Square(1, 2, -3)

        with self.assertRaises(ValueError):
            Square(0)

    def test_case_normal(self):
        """Test of Square(1, 2, 3, 4) exists"""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_area(self):
        """testing area"""
        s = Square(5)
        self.assertEqual(s.area(), 25)
        s = Square(1, 2)
        self.assertEqual(s.area(), 1)

    def test_string(self):
        """Test str"""
        s2 = Square(1, 2, 5, 12)
        self.assertEqual(str(s2), "[Square] (12) 2/5 - 1")

    def test_dictionary(self):
        """test dictionary for square"""
        s3 = Square(10, 2, 1, 12)
        s3_dic = s3.to_dictionary()
        self.assertEqual(s3_dic, {'id': 12,'size': 10, 'x': 2, 'y': 1})

if __name__ == "__main__":
    unittest.main()
