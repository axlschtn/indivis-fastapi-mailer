from bs4.formatter import HTMLFormatter
from src.email.regex import regex_result
from src.email.schema import ResponseParser

def parser(soup: HTMLFormatter):
    response = ResponseParser()
    strong_tags = soup.find_all('strong')[1:5]
    print(strong_tags)
    for strong_tag in strong_tags:
        print(strong_tag)
        if strong_tag.find('a'):
            if strong_tag.find('a').get('href').startswith('mailto:'):
                response.email = strong_tag.find('a').text    
            else:
                response.link_annonce = strong_tag.find('a').get("href")
        elif regex_result('phone', strong_tag.text):
            response.phone = strong_tag.text
        else:
            response.user = strong_tag.text
    response.provider = 'bienici'
    print(response)
    return response