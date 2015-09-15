__author__ = 'f.zesch'

from bottle import request, route
import re
import hashlib

MALICIOUS_EXPRESSIONS = ["DROP", "TABLE", "DELETE"]

# default parameters for checking validity of number
LAGESO_pattern = re.compile("^[a-zA-Z]{1,1}[0-9]+$")
LAGESO_min = 0
LAGESO_max = 99


def is_valid_number(number, pattern=LAGESO_pattern, min_len=LAGESO_min, max_len=LAGESO_max):
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
    Checks whether a user is entitled for writing to the database. Currently, only double entries are impossible
    through user_id-check
    :param username: username to be validated
    :param location: location where user wants to write to
    :param db_con: database connection for passing SQL command
    :return:
    """

    return True

def get_user_id():
    """
    Returns an identification hash of the user
    :return:
    """

    user_agent = request.environ.get("HTTP_USER_AGENT")
    user_ip = request.environ.get('HTTP_X_FORWARDED_FOR')

    #todo: get user os or other means for refining browser fingerprint

    return hashlib.md5(user_agent+user_ip)
