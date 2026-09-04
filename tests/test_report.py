import unittest
from unittest import TestCase
from unittest.mock import patch

from pwcheck.report import full_check, full_report, small_check, small_report


# Test assertations for full_check function
class TestFullCheck(TestCase):
    @patch("pwcheck.api.urllib.request.urlopen")
    def test_full_check(self, mock_check_pwned):
        mock_check_pwned.return_value.readlines.return_value = [
            b"1E4C9B93F3F0682250B6CF8331B7EE68FD8:52372427\r\n",
            b"1E4AB85875AA6B6E316963C7754A216FFBC:20\r\n",
            b"1E3687A61BFCE35F69B7408158101C8E414:1\r\n",
        ]
        self.assertDictEqual(
            full_check("password"),
            {
                "length": True,
                "variety": False,
                "consecutive repeating characters": False,
                "common list": True,
                "pwned": True,
            },
        )


# Test assertations for full_report function
class TestFullReport(TestCase):
    @patch("pwcheck.api.urllib.request.urlopen")
    def test_full_report(self, mock_check_pwned):
        mock_check_pwned.return_value.readlines.return_value = [
            b"1E4C9B93F3F0682250B6CF8331B7EE68FD8:52372427\r\n",
            b"1E4AB85875AA6B6E316963C7754A216FFBC:20\r\n",
            b"1E3687A61BFCE35F69B7408158101C8E414:1\r\n",
        ]
        self.assertDictEqual(
            full_report("password"),
            {
                "length": True,
                "variety": False,
                "consecutive repeating characters": False,
                "common list": True,
                "variety reason": "Your password must have at least 3 of the following: lowercase, uppercase, digit, special character",
                "common list reason": "Your password was found in our common password list",
                "pwned": True,
                "pwned reason": "Your password has appeared in a data breach",
            },
        )


# Test assertations for small_check function
class TestSmallCheck(TestCase):
    def test_small_check(self):
        self.assertDictEqual(
            small_check("password"),
            {
                "length": True,
                "variety": False,
                "consecutive repeating characters": False,
                "common list": True,
            },
        )


# Test assertations for small_report function
class TestSmallReport(TestCase):
    def test_small_report(self):
        self.assertDictEqual(
            small_report("password"),
            {
                "length": True,
                "variety": False,
                "consecutive repeating characters": False,
                "common list": True,
                "variety reason": "Your password must have at least 3 of the following: lowercase, uppercase, digit, special character",
                "common list reason": "Your password was found in our common password list",
            },
        )


if __name__ == "__main__":
    unittest.main()
