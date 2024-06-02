from bs4.formatter import HTMLFormatter
from src.email.regex import regex_result
from src.email.schema import ResponseParser

def parser(soup: HTMLFormatter):
    response = ResponseParser()
    strong_tags = soup.find_all('strong')[1:5]
    print(strong_tags)
    response.link_annonce = strong_tags[0].find('a').get("href")
    response.user = strong_tags[1].text
    response.phone = strong_tags[2].text
    response.email = strong_tags[3].text
    response.provider = 'bienici'
    print(response)
    return response