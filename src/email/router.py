from fastapi import APIRouter

email_router = APIRouter(
    prefix='/email',
    tags=['Email']
)

@email_router.post('/parse')
async def parse_email(
    email_content: str
):
    print(email_content)
    return 'ok'