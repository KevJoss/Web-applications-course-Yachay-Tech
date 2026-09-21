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

@app.post(
    "/customers",
    response_model=schemas.CustomerResponse
)
def create_customer(
    data: schemas.CustomerCreate,
    db: Session = Depends(get_db)
):
    customer = models.Customer(
        name = data.name,
        email = data.email
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

@app.post(
    "/orders",
    response_model=schemas.OrderResponse
)
def create_order(
    data: schemas.OrderCreate,
    db: Session = Depends(get_db)
):
    customer = db.get(
        models.Customer,
        data.customer_id
    )

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    order = models.Order(
        customer=customer,
        status="pending"
    )

    for item_data in data.items:
        product = db.get(
            models.Product,
            item_data.product_id
        )

        if product is None:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        item = models.OrderItem(
            product=product,
            quantity=item_data.quantity,
            unit_price=product.price
        )

        order.items.append(item)

    db.add(order)
    db.commit()
    db.refresh(order)

    return order

@app.get("/orders/{order_id}", response_model=schemas.OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.get(models.Order, order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@app.get("/customers/{customer_id}/orders", response_model=schemas.CustomerWithOrdersResponse)
def get_customer_orders(customer_id: int, db: Session = Depends(get_db)):
    customer = db.get(models.Customer, customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@app.put("/orders/{order_id}/status", response_model=schemas.OrderResponse)
def update_order_status(order_id: int, data: schemas.OrderStatusUpdate, db: Session = Depends(get_db)):
    order = db.get(models.Order, order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    order.status = data.status
    db.commit()
    db.refresh(order)
    return order

@app.delete("/orders/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    order = db.get(models.Order, order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(order)
    db.commit()
    return {"message": "Order deleted", "id": order_id}