from bs4 import BeautifulSoup
from bs4.formatter import HTMLFormatter
from src.core.schema import ResponseParser, ResponseScrapped
from src.core.regex import findall_regex

class ImplVousAmoiParser():
    
    def __init__(self, soup: HTMLFormatter):
        self.soup = BeautifulSoup(soup, 'html.parser')
    
    def execute(self):
        divs = self.soup.find_all('div', { 'align': 'left' })
        for div in divs:
            if div.get('style') == 'font-family:Open sans,arial,sans-serif;font-size:16px;line-height:25px;text-align:left;color:#363a41':
                text_content = div
        if text_content:
            phone = findall_regex('phone_regex', text_content.text.strip())
            email = findall_regex('email_regex', text_content.text.strip())
            name = text_content.find_all(string=lambda t: 'Nom :' in t or 'Nom' in t)
            prenom = text_content.find_all(string=lambda t: 'Prenom :' in t or 'Prénom' in t)
            user = None            
            if not name and not prenom:
                user = email[0].split('@')[0].replace('.', ' ')
            elif not name and prenom:
                user = prenom[0].split(":")[-1]
            elif not prenom and name:
                user = name[0].split(':')[-1]
            else:
                user = f"{name[0].split(':')[-1]} {prenom[0].split(':')[-1]}"
        return ResponseParser(
            provider='vousamoi',
            data=ResponseScrapped(
                user=user,
                phone=phone[0],
                email=email[0]
            )
        )