from typing import Annotated
from fastapi import APIRouter, Request, File
import base64
from bs4 import BeautifulSoup
import re

email_router = APIRouter(
    prefix='/email',
    tags=['Email']
)

@email_router.post('/parse')
async def parse_email(
    file: Annotated[bytes, File()],
    req: Request
):
    file_decode = file.decode("utf-8").encode('utf-8')
    file_str = base64.b64decode(file_decode).decode("utf-8")
    soup = BeautifulSoup(file_str, "html.parser") 
    print(soup)
    title_tag =  soup.find("title").text
    bienici_pattern_title = r'II3-\d{4}'
    bienici_matcher = re.findall(bienici_pattern_title, title_tag)
    if bienici_matcher:
        all_divs = soup.find_all("div")
        print(all_divs)
        for div in all_divs:
            print(div)
        user_info_block = soup.find("div", attrs={"style":"font-size:18px;line-height:22px;margin-bottom:5px"})
        user_detail = soup.find_all('strong')
        print(user_info_block, user_detail)
        return f"BienIci {title_tag}"
    return f"Seloger {file_str}"