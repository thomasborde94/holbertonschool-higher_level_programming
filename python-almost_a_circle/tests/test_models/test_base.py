#!/usr/bin/python3
"Unit tests for Base class"
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """tests for class Base"""

    def test_correctId(self):
        """assigns the correct id when it is given"""
        baseTest = Base(10)
        self.assertEqual(baseTest.id, 10)

    def test_autoId(self):
        """assigns an id automatically when id is not given"""
        baseTest = Base()
        self.assertEqual(baseTest.id, 1)

        baseTest2 = Base()
        self.assertEqual(baseTest2.id, 2)

    def test_to_json_string(self):
        """test of to_json_string func"""
        dic = {"id": 1, "x": 2, "y": 3, "width": 4, "height": 5}
        json_dic = Base.to_json_string([dic])
        self.assertTrue(isinstance(dic, dict))
        self.assertTrue(isinstance(json_dic, str))

if __name__ == "__main__":
    unittest.main()
