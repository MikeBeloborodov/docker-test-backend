from models import Message

def handle_message(db, message):
    message_to_save = Message(**message.dict())
    db.add(message_to_save)
    db.commit()
    db.refresh(message_to_save)
    return message_to_save
