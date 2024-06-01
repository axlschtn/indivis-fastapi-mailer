from bs4.formatter import HTMLFormatter
from src.email.regex import regex_result
from src.email.schema import ResponseParser

def parser(soup: HTMLFormatter):
    response = ResponseParser()
    strong_tags = soup.find_all('strong')[1:5]
    for strong_tag in strong_tags:
        if not strong_tag.find('a').get('href').startswith('mailto:'):
            response.link_annonce = strong_tag.find('a').get("href")
        elif regex_result('phone', strong_tag.text):
             response.phone = strong_tag.text
        elif regex_result('email', strong_tag.text):
            response.email = strong_tag.find('a').text
        else:
            response.user = strong_tag.text
    response.provider = 'bienici'
    return response