# Password Checker

This program can verify whether a password is secure via multiple checks.

## Program Features

- Checks if a password is long enough
- Checks if a password has enough variety
- Checks if a password has 3 or more of a character repeated in a row
- Checks if a password is in a common list of passwords
- Checks if it has appeared in known data breaches

## Installation

### 1. Requires Python version above 3.13

### 2. Install `uv` (ver. 0.12.7-0.13.0)

Install prebuilt binaries via shell script:

```
curl --proto '=https' --tlsv1.2 -LsSf https://releases.astral.sh/github/uv/releases/download/0.12.9/uv-installer.sh | sh
```

Install prebuilt binaries via powershell script:

```
powershell -ExecutionPolicy Bypass -c "irm https://releases.astral.sh/github/uv/releases/download/0.12.9/uv-installer.ps1 | iex"
```

### 3. Project Build Steps

a. Run:

```
git clone https://github.com/benjbread/Personal-Project.git
```

b. From the project root run:

```
uv sync
```

c. To confirm it all worked run:

```
uv run pwcheck
```

It should then ask for a password.

## CLI Usage

To run the program in its default mode, use this from the project's root directory:

```
uv run pwcheck
```

Optional flags:

- `--no-pwned`: Runs the program without the data breach check (the only part that makes a network call).
- `-v`, `--verbose`: Returns the password check with reasons for any failed checks.

## Project Structure

```
project_dir/
├── .venv/
├── src/
│   └── pwcheck/
│       ├── __pycache__/
│       ├── __init__.py
│       ├── analysis.py          # calculator functions
│       ├── api.py               # messenger functions
│       ├── common_passwords.txt
│       ├── main.py
│       └── report.py            # orchestrator functions
├── tests/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── test_analysis.py         # unittest for analysis.py
│   ├── test_api.py              # unittest for api.py
│   └── test_report.py           # unittest for report.py
├── .python-version
├── pyproject.toml
├── README.md
└── uv.lock
```

## Security Design Notes

- No passwords are stored; `getpass()` is used so the password never appears in shell history
- SHA-1 hashing + k-anonymity splitting is used for the HaveIBeenPwned check, so only a 5-character hash prefix is ever sent over the network
- Logging excludes secrets (no passwords or full hashes are ever logged)

## Running Tests

Contains basic test coverage for functions in `analysis.py`, `api.py`, and `report.py`, including:

### `analysis.py`

- Test assertions for `check_length`
- Test assertions for `check_chars_variety`
- Test assertions for `check_repeating_chars`
- Test assertions for `check_common_list`
- Test assertions for `hash_password`
- Test assertions for `hash_first_five`
- Test assertions for `hash_last_thirty_five`

### `api.py`

- Test assertions for `check_pwned`

### `report.py`

- Test assertions for `full_check`
- Test assertions for `full_report`
- Test assertions for `small_check`
- Test assertions for `small_report`

To run the tests, use this command from the project root:

```
uv run -m unittest discover
```

## Wordlist Source

https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/100k-most-used-passwords-NCSC.txt
