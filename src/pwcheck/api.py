import logging
from urllib.error import URLError
from urllib.request import urlopen

from pwcheck.analysis import hash_first_five, hash_last_thirty_five

# Create module-level logger
mylogger = logging.getLogger(__name__)


# returns if password has been "pwned"
def check_pwned(password: str) -> bool | None:
    # Try to open url with first five of hash
    try:
        with urlopen(
            f"https://api.pwnedpasswords.com/range/{hash_first_five(password)}",
            timeout=5,
        ) as f:
            end_of_hash: str = hash_last_thirty_five(password)
            for line in f.readlines():
                pwned_hash = str(line, "utf-8").strip().split(":")[0]
                if end_of_hash == pwned_hash:
                    return True
            return False
    except URLError as err:
        mylogger.warning(
            f"Could not connect to PwnedPassword API. Reason: {err.reason}"
        )
        return None
