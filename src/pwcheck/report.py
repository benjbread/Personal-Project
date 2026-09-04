from pwcheck.analysis import (
    check_chars_variety,
    check_common_list,
    check_length,
    check_repeating_chars,
)
from pwcheck.api import check_pwned


# Creates dict with keys that will always exist
def small_check(password: str) -> dict:
    report: dict = {
        "length": check_length(password),
        "variety": check_chars_variety(password),
        "consecutive repeating characters": check_repeating_chars(password),
        "common list": check_common_list(password),
    }
    return report


# Creates dict from small_check but adds pwned check key
def full_check(password: str) -> dict:
    report = small_check(password).copy()
    report.update({"pwned": check_pwned(password)})
    return report


# Creates dict from small_check but adds keys for reason if failed
def small_report(password: str) -> dict:
    report = small_check(password).copy()

    if report["length"] is False:
        report.update({"length reason": "Password isn't 8 or more characters"})
    if report["variety"] is False:
        report.update(
            {
                "variety reason": "Your password must have at least 3 of the following: lowercase, uppercase, digit, special character"
            }
        )
    if report["consecutive repeating characters"] is True:
        report.update(
            {
                "repeating reason": "Your password contains at least 3 of the same character in a row"
            }
        )
    if report["common list"] is True:
        report.update(
            {
                "common list reason": "Your password was found in our common password list"
            }
        )
    return report


# Creates dict from small_report but adds key for pwned and reason if failed
def full_report(password: str) -> dict:
    report: dict = small_report(password).copy()
    report.update({"pwned": check_pwned(password)})
    if report["pwned"] is True:
        report.update(
            {"pwned reason": "Your password has appeared in a data breach"}
        )
    return report
