from bs4.formatter import HTMLFormatter
from src.email.regex import regex_result
from src.email.schema import ResponseParser, BienIciParser

def parser(soup: HTMLFormatter):
    response = ResponseParser()
    parser = BienIciParser()
    strong_tags = soup.find_all('strong')[1:5]
    parser.link_annonce = strong_tags[0].find('a').get("href")
    parser.user = strong_tags[1].text
    parser.phone = strong_tags[2].text
    parser.email = strong_tags[3].text
    response.provider = 'bienici'
    response.bienIci = parser
    return response