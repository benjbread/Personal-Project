import unittest
from unittest import TestCase
from unittest.mock import patch

from pwcheck.api import check_pwned


# Test assertations for check_pwned function
class TestCheckPwned(TestCase):
    # Patches the urlopen function in pwcheck when TestCheckPwned is called
    @patch("pwcheck.api.urllib.request.urlopen")
    def test_check_pwned(self, mock_check_pwned):
        # Mocks list of hash endings and counts returned from API call
        mock_check_pwned.return_value.readlines.return_value = [
            b"1E4C9B93F3F0682250B6CF8331B7EE68FD8:52372427\r\n",
            b"1E4AB85875AA6B6E316963C7754A216FFBC:20\r\n",
            b"1E3687A61BFCE35F69B7408158101C8E414:1\r\n",
        ]
        # input should return True as passwords hash ending appears in the list
        self.assertTrue(check_pwned("password"))


if __name__ == "__main__":
    unittest.main()
