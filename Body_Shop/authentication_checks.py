from re import match
from json import loads


def checking_password_policies(password: str):  # TODO re-write with regex
    """checks if the password meets the criteria and if not returns the corresponding error message"""
    error = ""

    if len(password) < 8:
        error = "The password must be at least 8 characters long."

    else:
        contains_letters = False
        contains_digits = False
        contains_special_chars = False
        other = False
        for char in password:
            if char.isalpha():
                contains_letters = True
            elif char.isdigit() or char.isnumeric():
                contains_digits = True
            elif char.isascii():
                contains_special_chars = True
            else:
                other = True

        if not contains_letters:
            error = "The password must contain at least 1 letter"
        elif not contains_digits:
            error = "The password must contain at least 1 digit"
        elif not contains_special_chars:
            error = "The password must contain at least one special character"
        elif other:
            error = "The password may only contain characters found at https://theasciicode.com.ar/"  # TODO make the link work.

    if error:
        return error


def username_is_valid(username: str) -> bool:
    regex_pattern = r"\A[\w\-.]{3,}\Z"
    return match(regex_pattern, username) is not None


def user_already_exists(user: str, database: list):
    for line in database:
        line = loads(line)
        if user == line["username"]:
            return True

    return False


def user_name_matches_password(username, password, database):
    for line in database:
        line = loads(line)
        if line.get("username") == username:
            if password == line.get("password"):
                return True

    return False


