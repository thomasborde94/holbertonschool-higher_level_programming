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

    def test_update(self):
        """test update func for square"""
        s4 = Square(10, 3, 5, 30)
        s4.update(20, 25, 30, 35)
        self.assertEqual(s4.id, 20)
        self.assertEqual(s4.size, 25)
        self.assertEqual(s4.x, 30)
        self.assertEqual(s4.y, 35)

    def test_create_square(self):
        """test of create func for square"""
        s5 = Square.create(**{"id": 55, "size": 12, "x": 3, "y": 5})
        s6 = Square(12, 3, 5, 55)
        self.assertEqual(str(s5), str(s6))

    def test_save_to_file(self):
        """
        Test save file
        """
        s = Square(8, 0, 0, 18)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            data_read = f.read()
        expect_output = '[{"id": 18, "size": 8, "x": 0, "y": 0}]'
        self.assertEqual(data_read, expect_output)
        os.remove("Square.json")

        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            data_read = f.read()
        expect_output = '[]'
        self.assertEqual(data_read, expect_output)
        os.remove("Square.json")

        Square.save_to_file([])
        with open("Square.json", "r") as f:
            data_read = f.read()
        expect_output = '[]'
        self.assertEqual(data_read, expect_output)
        os.remove("Square.json")


    def test_load_to_file(self):
        """
        Test load file
        """
        s1 = Square(8)
        Square.save_to_file([s1])
        squares = Square.load_from_file()
        self.assertIsInstance(squares[0], Square)
        self.assertEqual(squares[0].width, 8)
        os.remove("Square.json")

        s = Square.load_from_file()
        self.assertTrue(isinstance(s, list))
        self.assertEqual(s, [])

if __name__ == "__main__":
    unittest.main()
