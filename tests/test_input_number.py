__author__ = 'f.zesch'

# test cases for validation function: success, failure, sanity

from lagesonum.input_number import get_numbers
from unittest import TestCase

#http://www.diveintopython.net/unit_testing/testing_for_success.html
class InputTests(TestCase):

    def input_two_different_on_one_line(self):
        input_num = "A123 B123"
        result = get_numbers(input_num)

        self.assertEqual(["A123", "B123"], result)

    def input_three_on_three_lines(self):

        input_num = "A123\nB123\nC1223"
        result = list(get_numbers(input_num))

        self.assertEqual(["A123", "B123", "C123"], result)

InputTests.input_three_on_three_lines()
InputTests.input_two_different_on_one_line()

