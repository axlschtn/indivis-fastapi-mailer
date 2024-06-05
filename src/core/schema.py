from typing import Annotated, Union
from pydantic import BaseModel, Field

class BienIciParser(BaseModel):
    email: str = Field(None)
    phone: str = Field(None)
    user: str = Field(None)
    link_annonce: str = Field(None)
    
class VousAMoiParser(BaseModel):
    email: str = Field(None)
    user: str = Field(None)
    phone: str = Field(None)
    
    link_annonce: str = Field(None)
    
class ResponseParser(BaseModel):
    provider: str = Field(None)
    data: Union[
        Annotated[VousAMoiParser, None],
        Annotated[BienIciParser, None]
    ] = Field(None)