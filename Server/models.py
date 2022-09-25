from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker
from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    Float,
    String
)

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)

    def __repr__(self):
        return "<User(id='%s', username='%s')>" % (
            self.id,
            self.username
        )


class Room(Base):
    __tablename__ = "room"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    name = Column(String(255))
    co2 = Column(Float, default=0.0)
    light = Column(Float, default=0.0)
    hum = Column(Float, default=0.0) # humidity
    temp = Column(Float, default=0.0)
    occupied = Column(Boolean, default=False)

    def __repr__(self):
        return "<Room(id='%s', user='%s')>" % (
            self.id,
            self.user_id
        )

    def to_dict(self):
         return  {"id":self.id, 
            "user_id": self.user_id, 
            "room_name": self.name,
            "co2": self.co2, 
            "light": self.light, 
            "temp": self.temp, 
            "hum": self.hum, 
            "occupied": self.occupied}


