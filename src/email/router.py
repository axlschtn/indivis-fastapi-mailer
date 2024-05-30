from fastapi import APIRouter, Request

email_router = APIRouter(
    prefix='/email',
    tags=['Email']
)

@email_router.post('/parse')
async def parse_email(
    req: Request
):
    print(req.body)
    return 'ok'