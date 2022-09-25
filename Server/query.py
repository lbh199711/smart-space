from typing import List
from models import User, Room



def get_rooms_by_user_id(user_id, db_session) -> List[Room]:
    """Given an account returns all products that user has access to"""
    rooms = (
        db_session.query(Room).filter(Room.user_id == user_id).all()
    )

    return rooms


def get_user_by_username(username, db_session) -> User:
    """Given an account returns all products that user has access to"""
    user = db_session.query(User).filter(User.username== username).first()

    return user


def get_room_by_room_id(room_id, db_session) -> Room:
    room = db_session.query(Room).filter(Room.id == room_id).first()

    return room