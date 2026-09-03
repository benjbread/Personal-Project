from pwcheck.analysis import (
    check_chars_variety,
    check_common_list,
    check_length,
    check_repeating_chars,
)
from pwcheck.api import check_pwned


def full_check(password: str) -> dict:
    report = small_check(password).copy()
    report.update({'pwned': check_pwned(password)})
    return report


def small_check(password: str) -> dict:
    report: dict = {
        'length': check_length(password),
        'variety': check_chars_variety(password),
        'consecutive repeating characters': check_repeating_chars(password),
        'common list': check_common_list(password),
    }
    return report


def full_report_dict(password: str) -> dict:
    report: dict = small_report_dict(password).copy()
    report.update({'pwned': check_pwned(password)})
    if report['pwned'] is True:
        report.update(
            {'pwned reason': "Your password has appeared in a data breach"}
        )
    return report


def small_report_dict(password: str) -> dict:
    report = small_check(password).copy()

    if report['length'] is False:
        report.update({'length reason': "Password isn't 8 or more characters"})
    if report['variety'] is False:
        report.update(
            {
                'variety reason': "Your password must have at least 3 of the following: lowercase, uppercase, digit, special character"
            }
        )
    if report['consecutive repeating characters'] is True:
        report.update(
            {
                'repeating reason': "Your password contains at least 3 of the same character in a row"
            }
        )
    if report['common list'] is True:
        report.update(
            {
                'common list reason': "Your password was found in our common password list"
            }
        )
    return report

def print_report(report: dict) -> None:
    print("==== Password Report ====")

    if report['length'] is True:
        print("\nLength Test: PASSED")
    if report['length'] is False:
        print("\nLength Test: FAILED")
        if 'length reason' in report:
            print(f"Reason: {report['length reason']}")

    if report['variety'] is True:
        print("\nVariety Test: PASSED")
    if report['variety'] is False:
        print("\nVariety Test: FAILED")
        if 'variety reason' in report:
            print(f"Reason: {report['variety reason']}")

    if report['consecutive repeating characters'] is False:
        print("\nNo Repeating Characters Test: PASSED")
    if report['consecutive repeating characters'] is True:
        print("\nNo Repeating Characters Test: FAILED")
        if 'repeating reason' in report:
            print(f"Reason: {report['repeating reason']}")

    if report['common list'] is False:
        print("\nCommon Password List Test: PASSED")
    if report['common list'] is True:
        print("\nCommon Password List Test: FAILED")
        if 'common list reason' in report:
            print(f"Reason: {report['common list reason']}")

    if 'pwned' in report:
        if report['pwned'] is False:
            print("\nHaveIBeenPwned Test: PASSED")
        if report['pwned'] is True:
            print("\nHaveIBeenPwned Tes: FAILED")
            if 'pwned reason' in report:
                print(f"Reason: {report['pwned reason']}")
