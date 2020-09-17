import unittest
from Est_Mem_R_Load import *

LEAD_SPACE = " -h"

class MyFirstTests(unittest.TestCase):

    '''
    Test to make sure it returns a well formed argument correctly.
    '''
    def test_strip_input(self):
        self.assertEqual(strip_input('-h'), '-h')

    '''
    Test to make sure it removes carriage returns
    '''
    def test_carriage_strip_input(self):
        self.assertEqual(strip_input('-h\r'),'-h')

    def test_remove_lead_space_strip_input(self):
        self.assertEqual(strip_input(' -h'),'-h')
