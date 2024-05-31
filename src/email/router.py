from typing import Annotated
from fastapi import APIRouter, Request, File
import base64
from bs4 import BeautifulSoup
import re
import json

email_router = APIRouter(
    prefix='/email',
    tags=['Email']
)

regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
regex_phone = r'^([\s\d]+)$'
regex_bienici_id = r'II3-\d{4}'

@email_router.post('/parse')
async def parse_email(
    req: Request,
    file: Annotated[bytes, File()] = None,
):
    if file:
        file_decode = file.decode("utf-8").encode('utf-8')
        file_str = base64.b64decode(file_decode).decode("utf-8")
        soup = BeautifulSoup(file_str, "html.parser") 
        title_tag =  soup.find("title").text
        bienici_matcher = re.findall(regex_bienici_id, title_tag)
        if bienici_matcher:
            bienici_dict = {"provider": "bienici", "user": "", "email": "", "phone":"", "link_annonce":""}
            strong_tags = soup.find_all('strong')[1:5]
            for strong_tag in strong_tags:
                if strong_tag.find('a'):
                    bienici_dict.update({"link_annonce": strong_tag.find('a').get("href")})
                if re.match(regex_phone, strong_tag.text):
                    bienici_dict.update({"phone": strong_tag.text})
                if re.match(regex_email, strong_tag.text):
                    bienici_dict.update({"email": strong_tag.text})
                bienici_dict.update({"user": strong_tag.text})
            return bienici_dict
        return f"Seloger {file_str}"