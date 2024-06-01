from pydantic import BaseModel, Field

class ResponseParser(BaseModel):
    provider: str = Field(None)
    email: str = Field(None)
    phone: str = Field(None)
    user: str = Field(None)
    link_annonce: str = Field(None)