from pwcheck.analysis import (
    check_chars_variety,
    check_common_list,
    check_length,
    check_repeating_chars,
)
from pwcheck.api import check_pwned


def full_check(password: str) -> dict:
    report = small_check(password).copy()
    report.update({"pwned": check_pwned(password)})
    return report


def small_check(password: str) -> dict:
    report: dict = {
        "length": check_length(password),
        "variety": check_chars_variety(password),
        "consecutive repeating characters": check_repeating_chars(password),
        "common list": check_common_list(password),
    }
    return report


def full_report_dict(password: str) -> dict:
    report: dict = small_report_dict(password).copy()
    report.update({"pwned": check_pwned(password)})
    if report["pwned"] is True:
        report.update(
            {"pwned reason": "Your password has appeared in a data breach"}
        )
    return report


def small_report_dict(password: str) -> dict:
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


# Prints the report dict in a more human readable format
def print_report(report: dict) -> None:
    print("==== Password Report ====\n")

    # Length Test Report Output
    print("-" * 25)
    if report["length"] is True:
        print("Length Test: PASSED")
    if report["length"] is False:
        print("Length Test: FAILED")
        if "length reason" in report:
            print(f"Reason: {report['length reason']}")
    print("-" * 25 + "\n")

    # Variety Test Report Output
    print("-" * 25)
    if report["variety"] is True:
        print("Variety Test: PASSED")
    if report["variety"] is False:
        print("Variety Test: FAILED")
        if "variety reason" in report:
            print(f"Reason: {report['variety reason']}")
    print("-" * 25 + "\n")

    # Repeating Character Test Report Output
    print("-" * 25)
    if report["consecutive repeating characters"] is False:
        print("No Repeating Characters Test: PASSED")
    if report["consecutive repeating characters"] is True:
        print("No Repeating Characters Test: FAILED")
        if "repeating reason" in report:
            print(f"Reason: {report['repeating reason']}")
    print("-" * 25 + "\n")

    # Common List Test Report Output
    print("-" * 25)
    if report["common list"] is False:
        print("Common Password List Test: PASSED")
    if report["common list"] is True:
        print("Common Password List Test: FAILED")
        if "common list reason" in report:
            print(f"Reason: {report['common list reason']}")
    print("-" * 25 + "\n")

    # Pwned Test Report Output
    print("-" * 25)
    if "pwned" in report:
        if report["pwned"] is False:
            print("HaveIBeenPwned Test: PASSED")
        if report["pwned"] is True:
            print("HaveIBeenPwned Test: FAILED")
            if "pwned reason" in report:
                print(f"Reason: {report['pwned reason']}")
    print("-" * 25 + "\n")
