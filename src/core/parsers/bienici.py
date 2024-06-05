from bs4.formatter import HTMLFormatter
from bs4 import BeautifulSoup
from src.core.schema import ResponseParser, BienIciParser

class ImplBieniciParser():
    
    def __init__(self, soup: HTMLFormatter):
        self.soup = BeautifulSoup(soup, 'html.parser')
    
    def execute(self):
        strong_tags = self.soup.find_all('strong')[1:5]
        return ResponseParser(
            provider='bienici',
            data=BienIciParser(
                phone=strong_tags[2].text,
                email=strong_tags[3].text,
                user=strong_tags[1].text,
                link_annonce=strong_tags[0].find('a').get("href"),
            ),
        )