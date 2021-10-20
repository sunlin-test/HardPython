# coding=utf-8

import unittest


class SampleTest(unittest.TestCase):
    def test_isstring(self):
        a = 'sdf'
        self.assertEqual(isinstance(a, str), True)


if __name__ == "main":
    unittest.main()
