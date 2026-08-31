import re
import string
from pathlib import Path

# Returns True if password is at least 8 characters
def check_length(password: str) -> bool:
    return len(password) >= 8

# Returns True if password contains at least 3 of 4 variety categories
def check_chars_variety(password: str) -> bool:
    counter: int = 0
    # add 1 to counter if password contains at least one lowercase
    if re.search(r"[a-z]", password):
        counter += 1
    # add 1 to counter if password contains at least one uppercase
    if re.search(r"[A-Z]", password):
        counter += 1
    # add 1 to counter if password contains at least one digit
    if re.search(r"[0-9]", password):
        counter += 1
    # add 1 to counter if password contains at least one special character
    if re.search(rf"[{re.escape(string.punctuation)}]", password):
        counter += 1
    return counter >= 3

# Returns True if password contains at least 3 of the same character in a row
def check_repeating_chars(password: str) -> bool:
    return bool(re.search(r"(.)\1\1", password))

# Returns True if password is found in the common_passwords.txt
def check_common_list(password: str) -> bool:
    with open(Path(__file__).resolve().parent /  'common_passwords.txt', 'r') as file:
        return password in set(file.read().splitlines())
