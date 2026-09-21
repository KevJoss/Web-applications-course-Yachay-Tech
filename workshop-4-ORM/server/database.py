from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


DATABASE_URL = (
    "mysql+pymysql://root:root@127.0.0.1:3306/webshop"
)


# Central point of communication between Python and MySQL Server
# echo=True -> shows the SQL queries on the console

engine = create_engine(
    DATABASE_URL,
    echo=True
)

# Session Maker is a factory which open Local Sessions for doing CRUD on the open engine

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


class Base(DeclarativeBase):
    pass


def get_db():

    db = SessionLocal() # Open new session

    try:
        yield db # Gives to the endpoint the session

    finally:
        db.close() # Close the session when ENDS de process.