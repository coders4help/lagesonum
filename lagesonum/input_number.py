#todo: refactor: create one function "validate" for general validation, easier for external calling
from bottle import request
import re
import hashlib

MALICIOUS_EXPRESSIONS = ["DROP", "TABLE", "DELETE"]
SEPARATORS = (",", ";", ".", " ", "\n")


# default parameters for checking validity of number
LAGESO_pattern = re.compile("^[a-zA-Z]{1,1}[0-9]+$")
LAGESO_min = 0
LAGESO_max = 99


#todo: fetch validation pattern, min and max from database, based on location argument (for multi-location scalability)
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

def get_numbers(numstr_list, sep=" "):
    """
    generator returning all input numbers, not regarding the way they are input over multiple lines
    """
    number_set = []

    for numstr in numstr_list:
        for i, s in enumerate(SEPARATORS):

            if len(list(numstr.split(s))) > len(numstr_list):
                number_set.append(numstr.split(s)) and number_set.append(get_numbers(numstr), SEPARATORS[i])
            else:
                if is_valid_number(numstr):
                    number_set.append(numstr)

    final_set = [[n for n in n2] for n2 in number_set]
    return final_set

print(get_numbers(["A123\nB123\nC1223"]))
print(get_numbers(["A123 B123, C1223"]))
print(get_numbers(["A123,\n; B123, C1223"]))
print(get_numbers(["A123 B123"]))

