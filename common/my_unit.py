# coding=utf-8

import unittest


class MyUnit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print "this is setupClass function"

    @classmethod
    def tearDownClass(cls):
        print "this is teardownclass function"

    def setUp(self):
        print "this is setup function"

    def tearDown(self):
        print "this is tearDown function"