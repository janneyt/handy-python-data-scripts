import unittest
from Est_Mem_R_Load import *



class StripInputTests(unittest.TestCase):

    '''
    ############################################################################
    Strip_Input Tests
    ############################################################################
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

    def test_remove_tab_strip_input(self):
        self.assertEqual(strip_input('-h\t'),'-h')


    '''
    ############################################################################
    Recursive_Remove_Escape Tests
    ############################################################################

    There's a specific order in which escape sequences are tested:
    ESCAPE_SEQUENCES = ['\a','\\','\'','\b','\f','\n','\r','\t']

    So, if there's a '\r' in the string, the function should in fact output '-h\ r'
    if the esc_seq parameter is before the '\r' character.


    '''
    def test_remove_escape(self):
        self.assertEqual(recursive_remove_escape('-h', None), '-h')

    def test_remove_escape_with_none(self):
        self.assertEqual(recursive_remove_escape(repr('-h\r'), None), repr('-h\r'))

    def test_remove_car_in_array_escape(self):
        self.assertEqual(recursive_remove_escape(repr('-h\r'), '\r'), '-h')

    def test_remove_car_early_array_escape(self):
        self.assertEqual(recursive_remove_escape(repr('-h\r'), '\a'), '-h')

    def test_remove_car_late_array_escape(self):
        self.assertEqual(recursive_remove_escape(repr('-h\r'), '\t'), '-h')

    def test_escseq_not_in_array(self):
        self.assertEqual(recursive_remove_escape(repr('-h\r'), '\d'), '-h')
