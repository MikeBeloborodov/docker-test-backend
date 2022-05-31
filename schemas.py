from pydantic import BaseModel

class MessageRequest(BaseModel):
    message: str

class MessageResponse(BaseModel):
    msg_id: int
    message: str

    class Config:
        orm_mode = True