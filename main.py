from fastapi import FastAPI, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database_logic import get_db
from schemas import MessageRequest, MessageResponse
from handles import handle_message

app = FastAPI()


# main page
@app.get("/", status_code=status.HTTP_200_OK)
def root() -> dict:
    return {"message" : "Welcome from container!"}


@app.post("/message", status_code=status.HTTP_201_CREATED, response_model=MessageResponse)
def get_message(message: MessageRequest,
    db: Session = Depends(get_db)):
    return handle_message(db, message)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
