import unittest
from currency import convert, function1

class Test_Convert(unittest.TestCase):

    def test_convert(self):
        self.assertEqual(950<=convert(10,"USD", "RUB")<=1000,True)

    def test_self_convert(self):
        self.assertEqual(convert(5,"RUB", "RUB"),5)

    def test_exit(self):
        self.assertEqual(function1("Q"), 0)


if __name__ == '__main__':
    unittest.main()
