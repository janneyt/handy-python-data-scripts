
import unittest
from Est_Mem_R_Load import *

TITLE = "R Memory Estimator"
MESSAGE = "\nUse with caution.\n"

LOADING_SCREEN_test = ("\n\n\n"
                +TITLE
                +"\n\n\n"
                +MESSAGE
                +"\n\n\n"
                +INITIAL_MSG
                +"\n\n\n")



class StripInputTests(unittest.TestCase):
    maxDiff = None

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

    '''
    ############################################################################
    Get_Input Tests
    ############################################################################

    '''
    def test_options_get_input(self):
        self.assertEqual(get_input('-o'), evaluate_for_options('-o'))

    def test_integer_get_input(self):
        self.assertEqual(get_input(1), LOADING_SCREEN)

    def test_blank_get_input(self):
        self.assertEqual(get_input(None), loading_screen(MSG_REENTER))



    '''
    ############################################################################
    Loading Screen Tests
    ############################################################################

    '''

    def test_loading_screen(self):
       self.assertEqual(loading_screen(INITIAL_MSG), LOADING_SCREEN_test)
