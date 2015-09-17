# coding: utf-8

# TODO: refactor: create one function "validate" for general validation, easier for external calling
import re
import hashlib

MALICIOUS_EXPRESSIONS = ["DROP", "TABLE", "DELETE"]
SEPARATORS = (",", ";", ".", " ", "\n")


# default parameters for checking validity of number. In the future, other patterns might be possible (get from db)
LAGESO_pattern = re.compile("^[a-zA-Z][0-9]+$")
LAGESO_min = 0
LAGESO_max = 99


def parse_numbers(input_string, first_only=False):
    r = re.compile(r'[a-z]\s*[0-9]+', re.IGNORECASE)
    input_string = input_string.upper()

    numbers = []
    if first_only:
        numbers += r.search(input_string).groups()
    else:
        numbers += r.findall(input_string)

    return [''.join(num.split()) for num in numbers]


# TODO: fetch validation pattern, min and max from database, based on location argument (for multi-location scalability)
def is_valid_number(number, pattern=LAGESO_pattern):
    """
    Checks, whether a number is in a valid format for a pattern given for a location
    To be run before insertion into db
    :param number: number to be checked
    :param pattern: regular expression
    :return: boolean
    """
    if re.findall(pattern, number):
        return not any(map(lambda expr: expr in number, MALICIOUS_EXPRESSIONS))
    else:
        return False


def get_fingerprint(request):
    usr_agent = str(request.environ.get('HTTP_USER_AGENT', ''))
    usr_lang = str(request.environ.get('HTTP_ACCEPT_LANGUAGE', ''))
    usr_ip = str(request.remote_addr)

    usr_fingerprint = u'{}{}{}'.format(usr_agent, usr_lang, usr_ip)

    return hashlib.md5(usr_fingerprint.encode("utf-8")).hexdigest()
