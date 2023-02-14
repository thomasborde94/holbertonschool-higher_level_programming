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
        self.assertEqual(baseTest.id, 2)

if __name__ == "__main__":
    unittest.main()
