from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .email.router import email_router

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(email_router)

@app.get('/')
async def welcome():
    return 'ok'
