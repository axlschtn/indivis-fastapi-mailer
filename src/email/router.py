from fastapi import APIRouter, Request
from pydantic import BaseModel

email_router = APIRouter(
    prefix='/email',
    tags=['Email']
)

class EmailContent(BaseModel):
    html: str

@email_router.post('/parse')
async def parse_email(
    email: EmailContent,
    req: Request
):
    print(email)
    return 'ok'