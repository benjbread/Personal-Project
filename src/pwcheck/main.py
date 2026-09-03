import argparse
from getpass import getpass

from pwcheck.report import (
    full_check,
    full_report_dict,
    small_check,
    small_report_dict,
    print_report,
)

parser = argparse.ArgumentParser(
    description="This is a password strength check sample program"
)

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

def main():
    if (args.run_pwned and args.verbose_output) is True:
        report = full_report_dict(getpass()).copy()
        print_report(report)
    elif (args.run_pwned is False) and (args.verbose_output is True):
        report = small_report_dict(getpass()).copy()
        print_report(report)
    elif (args.run_pwned is True) and (args.verbose_output is False):
        report = full_check(getpass()).copy()
        print_report(report)
    else:
        report = small_check(getpass()).copy()
        print_report(report)


if __name__ == "__main__":
    main()
