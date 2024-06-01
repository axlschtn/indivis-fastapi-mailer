from typing import Annotated
from fastapi import APIRouter, File
import base64
from bs4 import BeautifulSoup
from .parsers.bienici import parser as bien_ici_parser

email_router = APIRouter(
    prefix='/email',
    tags=['Email']
)


def provider_match(provider: str):
    provider = provider.split('@')[1].split('.')[0]
    if provider == 'bienici':
        return ( False, True, False )
    return ( True, False, False )    

@email_router.post('/parse')
async def parse_email(
    provider: str,
    file: Annotated[bytes, File()] = None,
):
    if file:
        file_decode = file.decode("utf-8").encode('utf-8')
        file_str = base64.b64decode(file_decode).decode("utf-8")
        soup = BeautifulSoup(file_str, "html.parser") 
        vousamoi, bienici, seloger = provider_match(provider)
        if vousamoi:
            return bien_ici_parser(soup)
        elif bienici:
            return bien_ici_parser(soup)
        return bien_ici_parser(soup)