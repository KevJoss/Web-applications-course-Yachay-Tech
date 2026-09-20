from fastapi import (
    FastAPI,
    Depends,
    HTTPException
)

from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import (
    engine,
    Base,
    get_db
)

from . import models
from . import schemas


Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.get("/")
def root():

    return {
        "message": "ORM Workshop API"
    }