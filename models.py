from database_logic import Base
from sqlalchemy import Column, Integer, String


class Message(Base):
    __tablename__ = "messages"

    msg_id = Column(Integer, primary_key=True, nullable=False)
    message = Column(String, nullable=False)
    