#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test for an ordered list of integers."""
        ordered_numbers = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered_numbers), 4)

    def test_unordered_list(self):
        """Test for an unordered list of integers."""
        unordered_numbers = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered_numbers), 4)

    def test_max_at_beginning(self):
        """Test for a list with a maximum value at the beginning."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Test for an empty list."""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_one_element_list(self):
        """Test for a list with a single element."""
        one_element_list = [7]
        self.assertEqual(max_integer(one_element_list), 7)

    def test_floats(self):
        """Test for a list of floating-point numbers."""
        float_numbers = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(float_numbers), 15.2)

    def test_ints_and_floats(self):
        """Test for a list of integers and floating-point numbers."""
        mixed_numbers = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(mixed_numbers), 15.5)

    def test_string(self):
        """Test for a string."""
        string_value = "Ehoneah"
        self.assertEqual(max_integer(string_value), 'r')

    def test_list_of_strings(self):
        """Test for a list of strings."""
        string_list = ["Ehoneah", "is", "my", "name"]
        self.assertEqual(max_integer(string_list), "name")

    def test_empty_string(self):
        """Test for an empty string."""
        self.assertEqual(max_integer(""), None)

    def test_module_docstring(self):
        """Test for the module docstring."""
        module_docstring = __import__('6-max_integer').__doc__
        self.assertTrue(len(module_docstring) > 1)

    def test_function_docstring(self):
        """Test for the function docstring."""
        function_docstring = max_integer.__doc__
        self.assertTrue(len(function_docstring) > 1)

    def test_empty_list_alt(self):
        """Test for an empty list []"""
        empty_list_alt = []
        self.assertIsNone(max_integer(empty_list_alt))

    def test_no_args(self):
        """Test for no arguments passed to the function"""
        self.assertIsNone(max_integer())

    def test_one_element_alt(self):
        """Test for only one number in the list"""
        one_element_alt = [1]
        self.assertEqual(max_integer(one_element_alt), 1)

    def test_positive_end(self):
        """Test for all positive numbers with the maximum at the end"""
        positive_end = [2, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(positive_end), 50)

    def test_positive_middle(self):
        """Test for all positive numbers with the maximum in the middle"""
        positive_middle = [2, 10, 8, 360, 14, 50]
        self.assertEqual(max_integer(positive_middle), 360)

    def test_positive_beginning(self):
        """Test for all positive numbers with the maximum at the beginning"""
        positive_beginning = [200, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(positive_beginning), 200)

    def test_one_negative(self):
        """Test for a list with one negative number"""
        one_negative = [200, 10, 8, -36, 14, 50]
        self.assertEqual(max_integer(one_negative), 200)

    def test_all_negative(self):
        """Test for a list with all negative numbers"""
        all_negative = [-6, -50, -75, -1, -100]
        self.assertEqual(max_integer(all_negative), -1)

    def test_none(self):
        """Test for passing None as an argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        """Test for a non-integer type in the list"""
        non_int_arg = [1, 2, "Hello", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(non_int_arg)


if __name__ == '__main__':
    unittest.main()
