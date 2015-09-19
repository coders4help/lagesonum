# coding: utf-8

# test cases for validation function: success, failure, sanity

from input_number import parse_numbers, is_valid_number
from unittest import TestCase

class TestInput(TestCase):
    """Test case for checking whether input in form differing from well formatted line by line input is accepted."""

    def test_input_two_different_on_one_line(self):
        input_num = "A123 B123"
        result = parse_numbers(input_num)
        self.assertEqual({"A123", "B123"}, set(result))

    def test_input_three_on_three_lines(self):
        input_num = "A123\nB123\nC123"
        result = parse_numbers(input_num)
        self.assertEqual({"A123", "B123", "C123"}, set(result))

    def test_input_three_times_three_lines_mixed(self):
        input_num = "A123 A234 A345\nB123 B234 B345 \nC123 C234 C345"
        result = parse_numbers(input_num)
        self.assertEqual({"A123", "B123", "C123", "A234", "B234", "C234", "A345", "B345", "C345"}, set(result))

    def test_multiple_delimiters_on_three_lines_mixed(self):
        input_num = "A123, A234; A345,\nB123. B234 B345. \nC123   C234  C345"
        result = parse_numbers(input_num)
        self.assertEqual({"A123", "B123", "C123", "A234", "B234", "C234", "A345", "B345", "C345"}, set(result))

    def test_malformed_numbers(self):
        input_num = "a123, a234; a345,\nB123. B234 B345. \nC123   C234  C345"
        result = parse_numbers(input_num)
        self.assertEqual({"A123", "B123", "C123", "A234", "B234", "C234", "A345", "B345", "C345"}, set(result))

    def test_fail_numbers(self):
        input_num = "A 123, A 234; A345,\nB123. B234 B345. \nC123   C234  C345"
        result = parse_numbers(input_num)
        self.assertEqual({"B123", "C123", "B234", "C234", "A345", "B345", "C345"}, set(result))

    def test_empty_input(self):
        input_num = "   "
        result = parse_numbers(input_num)
        self.assertEqual(set(), set(result))

    def test_drop_table_parse(self):
        input_num = "DROP TABLE NUMBERS"
        result = parse_numbers(input_num)
        self.assertEqual(set(), set(result))

    def test_drop_table_valid(self):
        input_num = "DROP TABLE NUMBERS"
        result = is_valid_number(input_num)
        self.assertEqual(False, set(result))

    def test_valid_pos(self):
        input_num = "A1234\nB234"
        result = is_valid_number(input_num)
        self.assertEqual({"A1234", "B234"}, set(result))
