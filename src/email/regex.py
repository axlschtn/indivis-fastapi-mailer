import re

regex_config = {
    'phone_regex': r'^([\s\d]+)$',
    'email_regex': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
}


def regex_result(pattern: str, element: str):
    return re.match(regex_config.get(f"{pattern}_regex"), element)