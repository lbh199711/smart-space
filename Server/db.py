import sqlalchemy
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker
from sqlalchemy import (
    JSON,
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    Float,
    String,
    func,
)


def connect_database(db_url):
    engine_connection = sqlalchemy.create_engine(db_url, pool_pre_ping=True, echo=False)
    engine_connection.dialect.description_encoding = None

    if engine_connection:
        print("Connected Successfully to Database")
    else:
        print("Database Connection has failed")
    return engine_connection


def init_db(db_url):
    # Import all modules here that might define models so that
    # they will be registered properly on the metadata.
    import models
    from models import Base
    db_engine = connect_database(db_url)
    db_session = scoped_session(
        sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=db_engine
        )
    )
    Base.metadata.create_all(bind=db_engine)
    Base.query = db_session.query_property()

    return db_engine, db_session
