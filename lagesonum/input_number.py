__author__ = 'f.zesch'

import re

MALICIOUS_EXPRESSIONS = ["DROP", "TABLE", "DELETE"]
LAGESO_pattern = re.compile("^[a-zA-Z]{1,1}[0-9]+$")


def is_valid_number(number, pattern=LAGESO_pattern, min_len=0, max_len=99):
    """
    Checks, whether a number is in a valid format for a pattern given for a location
    To be run before insertion into db
    :param number: number to be checked
    :param pattern: regular expression
    :return: boolean
    """

    if re.findall(pattern, number):
        return True
    else:
        return False


def is_ok_with_db(number):
    """
    Checks, that a number to be inserted is generally no attack on database
    :param number:
    :return: boolean
    """

    # TODO: Very basic security check, please enhance, maybe with library, escaping, anything
    if sum([1 for e in MALICIOUS_EXPRESSIONS if e in number])>0:
        return False
    else:
        return True

def is_valid_user(username="Helper", location="Lageso", db_con="SQLite"):
    """
    Checks whether a user is entitled for writing to the database
    :param username: username to be validated
    :param location: location where user wants to write to
    :param db_con: database connection for passing SQL command
    :return:
    """

    #TODO: Implement user management to validate this. For now, always return true.
    return True
