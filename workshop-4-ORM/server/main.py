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


# =========================================================
# CUSTOMER CRUD
# =========================================================

@app.post(
    "/customers",
    response_model=schemas.CustomerResponse
)
def create_customer(
    data: schemas.CustomerCreate,
    db: Session = Depends(get_db)
):

    customer = models.Customer(
        name=data.name,
        email=data.email
    )

    db.add(customer)
    db.commit()
    db.refresh(customer)

    return customer


@app.get(
    "/customers",
    response_model=list[schemas.CustomerResponse]
)
def list_customers(
    db: Session = Depends(get_db)
):

    result = db.execute(
        select(models.Customer)
    )

    return result.scalars().all()


@app.get(
    "/customers/{customer_id}",
    response_model=schemas.CustomerResponse
)
def get_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):

    customer = db.get(
        models.Customer,
        customer_id
    )

    if customer is None:

        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer


@app.put(
    "/customers/{customer_id}",
    response_model=schemas.CustomerResponse
)
def update_customer(
    customer_id: int,
    data: schemas.CustomerUpdate,
    db: Session = Depends(get_db)
):

    customer = db.get(
        models.Customer,
        customer_id
    )

    if customer is None:

        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    if data.name is not None:
        customer.name = data.name

    if data.email is not None:
        customer.email = data.email

    db.commit()
    db.refresh(customer)

    return customer


@app.delete("/customers/{customer_id}")
def delete_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):

    customer = db.get(
        models.Customer,
        customer_id
    )

    if customer is None:

        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    db.delete(customer)
    db.commit()

    return {
        "message": "Customer deleted",
        "id": customer_id
    }