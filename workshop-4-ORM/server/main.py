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


# =========================================================
# PRODUCT CRUD
# =========================================================

@app.post(
    "/products",
    response_model=schemas.ProductResponse
)
def create_product(
    data: schemas.ProductCreate,
    db: Session = Depends(get_db)
):

    product = models.Product(
        name=data.name,
        price=data.price,
        stock=data.stock
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


@app.get(
    "/products",
    response_model=list[schemas.ProductResponse]
)
def list_products(
    db: Session = Depends(get_db)
):

    result = db.execute(
        select(models.Product)
    )

    return result.scalars().all()


@app.get(
    "/products/{product_id}",
    response_model=schemas.ProductResponse
)
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = db.get(
        models.Product,
        product_id
    )

    if product is None:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


@app.put(
    "/products/{product_id}",
    response_model=schemas.ProductResponse
)
def update_product(
    product_id: int,
    data: schemas.ProductUpdate,
    db: Session = Depends(get_db)
):

    product = db.get(
        models.Product,
        product_id
    )

    if product is None:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    if data.name is not None:
        product.name = data.name

    if data.price is not None:
        product.price = data.price

    if data.stock is not None:
        product.stock = data.stock

    db.commit()
    db.refresh(product)

    return product


@app.delete("/products/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = db.get(
        models.Product,
        product_id
    )

    if product is None:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    db.delete(product)
    db.commit()

    return {
        "message": "Product deleted",
        "id": product_id
    }