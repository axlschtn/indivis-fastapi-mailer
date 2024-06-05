from typing import Annotated
from fastapi import APIRouter, File, Depends
import base64
from bs4 import BeautifulSoup
from src.core.regex import extract_domain_email
from src.core.schema import ResponseParser
from src.core.parsers.bienici import ImplBieniciParser
from src.core.parsers.vousamoi import ImplVousAmoiParser
from src.mock.bienici import soup_mock
from src.mock.vousamoi import text_1, text_2, text_3

email_router = APIRouter(
    prefix='/email',
    tags=['Email']
)

@email_router.post(
    '/parse',
    response_model=ResponseParser
)
async def parse_email(
    email: str = Depends(extract_domain_email),
    file: Annotated[bytes, File()] = None,
):  
    if file:
        file_decode = file.decode("utf-8").encode('utf-8')
        file_str = base64.b64decode(file_decode).decode("utf-8")
        try:
            if email == 'bienici':
                print(ImplBieniciParser(soup=file_str).execute())
                return ImplBieniciParser(soup=file_str).execute()
            if email == 'vousamoi' or email == 'ambrabbyhub':
                print(ImplVousAmoiParser(soup=file_str).execute())
                return ImplVousAmoiParser(soup=file_str).execute()
        except ValueError as error:
            print(str(error))
    else:
        if email == 'bienici':
            print(ImplBieniciParser(soup=soup_mock).execute())
        if email == 'vousamoi' or email == 'ambrabbyhub':
            print(ImplVousAmoiParser(soup=text_3).execute())
            print(ImplVousAmoiParser(soup=text_2).execute())
            print(ImplVousAmoiParser(soup=text_1).execute())
        return  ResponseParser() 
        # if vousamoi:
        #     return ImplBieniciParser(soup)
        # elif bienici:
        #     return bien_ici_parser(soup)
        # return bien_ici_parser(soup)