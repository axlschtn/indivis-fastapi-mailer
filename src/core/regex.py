import re

regex_config = {
    'vousamoi': {
        'phone_regex': r'\b\d{10}\b|\b(?:\d{2} ?){4}\d{2}\b',
        'email_regex': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    },
    'phone_regex': r'^([\s\d]+)$',
    'email_regex': r'@([a-zA-Z0-9.-]+)\.'
}


def extract_domain_email(email: str):
    match = re.search(regex_config.get('email_regex'), email)
    if match:
        domain_parts = match.group(1).split('.')
        return domain_parts[-1]
    return None

def regex_result(pattern: str, element: str):
    return re.match(regex_config.get(f"{pattern}_regex"), element)

def findall_regex(pattern: str, text: str):
    return re.findall(regex_config.get('vousamoi').get(pattern), text)