import unittest
from pwcheck.api import check_pwned
from unittest import TestCase
from unittest.mock import patch, Mock

class TestCheckPwned(TestCase):
    @patch('pwcheck.api.urllib.request.urlopen')
    def test_check_pwned(self, mock_check_pwned):
        mock_check_pwned.return_value.readlines.return_value = [b'1E4C9B93F3F0682250B6CF8331B7EE68FD8:52372427\r\n', b'1E4AB85875AA6B6E316963C7754A216FFBC:20\r\n', b'1E3687A61BFCE35F69B7408158101C8E414:1\r\n']
        self.assertTrue(check_pwned("password"))


if __name__ == "__main__":
    unittest.main()
