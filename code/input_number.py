__author__ = 'f.zesch'

MALICIOUS_EXPRESSIONS = ["DROP", "TABLE"]

# logic for adding numbers to database

def is_valid_number(number, pattern, min_len=0, max_len=99):
    """
    Checks, whether a number is in a valid format for a pattern given for a location
    To be run before insertion into db
    :param number: number to be checked
    :param pattern: regular expression
    :return: boolean
    """

    return False


def is_ok_with_db(number):
    """
    Checks, that a number to be inserted is no attack on database
    :param number:
    :return: boolean
    """

    # TODO: Very basic security check, please enhance, maybe with library
    if sum([1 for e in MALICIOUS_EXPRESSIONS if e in number])>0:
        return True
    else:
        return False

def is_valid_user(username, location, db_con):
    """
    Checks whether a user is entitled for writing to the database
    :param username: username to be validated
    :param location: location where user wants to write to
    :param db_con: database connection for passing SQL command
    :return:
    """
    return False
