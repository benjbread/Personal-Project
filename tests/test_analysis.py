import unittest
from unittest import TestCase
from pwcheck.analysis import check_length, check_chars_variety, check_repeating_chars, check_common_list

# Test assertations for check_length function
class TestCheckLength(TestCase):
    def test_check_length(self):
        # input should return True as password is at least 8 characters
        self.assertTrue(check_length("12345678"))
        # input should return False as password is less than 8 characters
        self.assertFalse(check_length("1234567"))

# Test assertations for check_chars_variety function
class TestCheckCharsVariety(TestCase):
    def test_check_chars_variety(self):
        # input should return True as password contains all variety checks
        self.assertTrue(check_chars_variety("Aa1!"))
        # input should return True as password contains at least 3 of the variety checks
        self.assertTrue(check_chars_variety("Aa1"))
        # input should return False as password contains less than 3 variety checks
        self.assertFalse(check_chars_variety("password"))

# Test assertations for check_repeating_chars function
class TestCheckRepeatingChars(TestCase):
    def test_check_repeating_chars(self):
        # input should return True as password contains 3 (or more) of same character in a row
        self.assertTrue(check_repeating_chars("passsword"))
        # input should return False as password doesn't contain 3 (or more) of same character in a row
        self.assertFalse(check_repeating_chars("password"))

# Test assertations for check_common_list function
class TestCheckCommonList(TestCase):
    def test_check_common_list(self):
        # input should return True as password is in common list
        self.assertTrue(check_common_list("123456"))
        # input should return False as password is in common list
        self.assertFalse(check_common_list("EpicPass1!2@"))

if __name__ == "__main__":
    unittest.main()
