from typing import Annotated
from fastapi import APIRouter, Request, File
import base64

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
    print(file_str)
    return 'ok'