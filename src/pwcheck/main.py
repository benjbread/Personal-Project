import argparse
from getpass import getpass

from pwcheck.report import (
    full_check,
    full_report,
    small_check,
    small_report,
)

# Create the ArgurmentParser object with short description
parser = argparse.ArgumentParser(
    description="This is a password strength check sample program"
)

# add CLI arguements to not check pwned and/or give more verbose report
parser.add_argument(
    "--no-pwned",
    action="store_false",
    default=True,
    dest="run_pwned",
    help="Opt out of pwned check.",
)
parser.add_argument(
    "-v",
    "--verbose",
    action="store_true",
    default=False,
    dest="verbose_output",
    help="Provide most detailed password report.",
)

args = parser.parse_args()


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


def main():
    # pwned, verbose
    if (args.run_pwned and args.verbose_output) is True:
        print_report(full_report(getpass()))
    # verbose
    elif (args.run_pwned is False) and (args.verbose_output is True):
        print_report(small_report(getpass()))
    # pwned
    elif (args.run_pwned is True) and (args.verbose_output is False):
        print_report(full_check(getpass()))
    # no args
    else:
        print_report(small_check(getpass()))


if __name__ == "__main__":
    main()
