import logging
from fastapi import FastAPI, Body
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from typing import List, Optional

from http import HTTPStatus

import uvicorn
import pickle
import configparser
from db import init_db
from models import User, Room
from httplib2 import Response
from query import get_rooms_by_user_id, get_room_by_room_id, get_user_by_username


## APP setup
# FastApi
app = FastAPI()
with open('classifier.pkl', 'rb') as fid:
    classifier = pickle.load(fid)

config = configparser.ConfigParser()
config.read('config.ini')
db_url = config.get('ALL', 'DATABASE_URL')

# init db
db_engine, db_session = init_db(db_url)
    
## Routing
@app.get("/")
def home():
    return 200


@app.get('/room')
def login_and_get_rooms(username: str = ''):
    if username == '':
        return Response("username empty"), 201

    user = get_user_by_username(username, db_session=db_session)
    # if first time login
    if user is None: 
        user = User(username=username)
        db_session.add(user)
        db_session.commit()
        return Response({"user_id": user.id, "rooms": []})

    # else user exist
    rooms = get_rooms_by_user_id(user_id=user.id, db_session=db_session)
    output_list = []
    for room in rooms:
        output_list.append(room.to_dict())
    return Response({"user_id": user.id, "rooms": output_list})


@app.post('/room')
def create_room(user_id: int = Body(..., embed=True),
                room_name: str = Body(..., embed=True)):
    room = Room(user_id=user_id, name=room_name)
    db_session.add(room)
    db_session.commit()
    return Response({"rooms": [room.to_dict()]})


@app.put("/room")
def update_room(co2: float = Body(..., embed=True),
            humidity: float = Body(..., embed=True),
            light: float = Body(..., embed=True),
            temp: float = Body(..., embed=True),
            room_id: int = Body(..., embed=True)):

    room = get_room_by_room_id(room_id, db_session=db_session)
    prediction = classifier.predict([[co2, humidity, light, temp]])[0]

    room.co2 = co2
    room.light = light
    room.hum = humidity
    room.temp = temp
    room.occupied = bool(prediction)
    db_session.commit()

    return Response({"rooms": [room.to_dict()]})


@app.delete("/room")
def update_room(room_id: int = Body(..., embed=True)):
    room = get_room_by_room_id(room_id, db_session=db_session)
    if room:
        db_session.delete(room)
        db_session.commit()
    return 200


## Run App
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
