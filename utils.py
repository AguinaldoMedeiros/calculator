import re

NUMBER_OR_DOT_REGEX = re.compile(r'^[0-9.]$')


def isNumOrNot(string: str):
    return bool(NUMBER_OR_DOT_REGEX.search(string)
                )


def isValidNum(string: str):
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        ...
    return valid


def isEmpty(string: str):
    return len(string) == 0
