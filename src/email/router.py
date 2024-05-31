from typing import Annotated
from fastapi import APIRouter, Request, File

email_router = APIRouter(
    prefix='/email',
    tags=['Email']
)

@email_router.post('/parse')
async def parse_email(
    file: Annotated[bytes, File()],
    req: Request
):
    print(file)
    return 'ok'