import urllib.request

from pwcheck.analysis import hash_first_five, hash_last_thirty_five


# returns if password has been "pwned"
def check_pwned(password: str) -> bool:
    f = urllib.request.urlopen(
        f"https://api.pwnedpasswords.com/range/{hash_first_five(password)}"
    )
    password_hash: str = hash_last_thirty_five(password)
    for line in f.readlines():
        searched_hash = str(line, "utf-8").strip().split(":")[0]
        if password_hash == searched_hash:
            return True
    return False
