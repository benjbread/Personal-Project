import unittest
from unittest import TestCase
from pwcheck.analysis import (check_length,
    check_chars_variety,
    check_repeating_chars,
    check_common_list,
    hash_password,
    hash_first_five,
    hash_last_thirty_five)

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

# Test assertations for hash_password function
class TestHashPassword(TestCase):
    def test_hash_password(self):
        expected = "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8"
        # input should return True as "password" hash matches expected
        self.assertTrue(hash_password("password") == expected)
        # input should return False as "pass" hash doesnt match expected
        self.assertFalse(hash_password("pass") == expected)

# Test assertations for hash_first_five function
class TestHashFirstFive(TestCase):
    def test_hash_first_five(self):
        expected = "5BAA6"
        # input should return True as "password" hash first five characters matches expected
        self.assertTrue(hash_first_five("password") == expected)
        # input should return False as "pass" hash first five characters doesnt match expected
        self.assertFalse(hash_first_five("pass") == expected)

# Test assertations for hash_last_thirty_five function
class TestHashLastThirtyFive(TestCase):
    def test_hash_last_thirty_five(self):
        expected = "1E4C9B93F3F0682250B6CF8331B7EE68FD8"
        # input should return True as "password" hash's last thirty-five characters matches expected
        self.assertTrue(hash_last_thirty_five("password") == expected)
        # input should return False as "pass" hash last thirty-five characters doesnt match expected
        self.assertFalse(hash_last_thirty_five("pass") == expected)


if __name__ == "__main__":
    unittest.main()
