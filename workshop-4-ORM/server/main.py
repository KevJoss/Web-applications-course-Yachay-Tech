from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from server import models, schemas
from server.database import engine, get_db

# =====================================================================
#                      CREATE TABLES
# =====================================================================
# Crea las tablas automáticamente cuando se inicia la app
models.Base.metadata.create_all(bind=engine)

# =====================================================================
#                      INITIALIZE APP
# =====================================================================
app = FastAPI()


# =====================================================================
#              SECTION 1: CUSTOMER CRUD
# =====================================================================

@app.post(
    "/customers",
    response_model=schemas.CustomerResponse
)
def create_customer(
    data: schemas.CustomerCreate,
    db: Session = Depends(get_db)
):
    """Create a new customer"""
    
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
    """Get all customers"""
    
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
    """Get a specific customer by ID"""
    
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
    """Update a customer"""
    
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


@app.delete(
    "/customers/{customer_id}"
)
def delete_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):
    """Delete a customer"""
    
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


# =====================================================================
#              SECTION 2: PRODUCT CRUD
# =====================================================================

@app.post(
    "/products",
    response_model=schemas.ProductResponse
)
def create_product(
    data: schemas.ProductCreate,
    db: Session = Depends(get_db)
):
    """Create a new product"""
    
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
    """Get all products"""
    
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
    """Get a specific product by ID"""
    
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
    """Update a product"""
    
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


@app.delete(
    "/products/{product_id}"
)
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    """Delete a product"""
    
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


# =====================================================================
#              SECTION 3: ORDER CRUD WITH TRANSACTIONS
#              ⭐ THIS IS CRITICAL FOR PERSONA C (SECTION 8)
# =====================================================================

@app.post(
    "/orders",
    response_model=schemas.OrderResponse
)
def create_order(
    data: schemas.OrderCreate,
    db: Session = Depends(get_db)
):
    """
    Create an order with multiple items.
    
    This endpoint demonstrates:
    - Nested inserts (order with multiple items)
    - Inventory management (stock -= quantity)
    - Transactions (commit/rollback)
    - Atomicity (all or nothing)
    """
    
    # Step 1: Verify customer exists
    customer = db.get(
        models.Customer,
        data.customer_id
    )

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    # Step 2: Create order object
    order = models.Order(
        customer=customer,
        status="pending"
    )

    try:
        # Step 3: Process each item in the order
        for item_data in data.items:
            
            # Get the product
            product = db.get(
                models.Product,
                item_data.product_id
            )

            if product is None:
                raise HTTPException(
                    status_code=404,
                    detail="Product not found"
                )

            # Check if stock is available (CRITICAL FOR SECTION 8)
            if product.stock < item_data.quantity:
                raise HTTPException(
                    status_code=400,
                    detail=f"Insufficient stock for {product.name}"
                )

            # Decrease inventory
            # This is part of the transaction!
            product.stock -= item_data.quantity

            # Create order item
            item = models.OrderItem(
                product=product,
                quantity=item_data.quantity,
                unit_price=product.price
            )

            # Add item to order
            order.items.append(item)

        # Step 4: Add order to session and commit
        # If any error occurs BEFORE this, nothing is saved
        db.add(order)
        db.commit()
        db.refresh(order)

        return order

    except HTTPException:
        # Re-raise HTTP exceptions (404, 400, etc)
        db.rollback()
        raise
    
    except Exception:
        # Rollback on any other error
        # This ensures inventory is NOT decreased if order fails
        db.rollback()
        raise


@app.get(
    "/orders/{order_id}",
    response_model=schemas.OrderResponse
)
def get_order(
    order_id: int,
    db: Session = Depends(get_db)
):
    """Get a specific order with its items and customer"""
    
    order = db.get(
        models.Order,
        order_id
    )

    if order is None:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return order


@app.get(
    "/orders"
)
def list_orders(
    db: Session = Depends(get_db)
):
    """Get all orders"""
    
    result = db.execute(
        select(models.Order)
    )

    return result.scalars().all()


# =====================================================================
#              SECTION 4: NESTED QUERIES
#              (Orders by customer)
# =====================================================================

@app.get(
    "/customers/{customer_id}/orders",
    response_model=schemas.CustomerWithOrdersResponse
)
def get_customer_orders(
    customer_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a customer with all their orders and items.
    
    This demonstrates nested object retrieval:
    Customer → Order → OrderItem → Product
    """
    
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


# =====================================================================
#              SECTION 5: UPDATE ORDER STATUS
#              (For demonstrating UPDATE in Section 7)
# =====================================================================

@app.put(
    "/orders/{order_id}/status",
    response_model=schemas.OrderResponse
)
def update_order_status(
    order_id: int,
    data: schemas.OrderStatusUpdate,
    db: Session = Depends(get_db)
):
    """
    Update the status of an order.
    
    This demonstrates how modifying an ORM object
    generates an UPDATE SQL statement.
    """
    
    order = db.get(
        models.Order,
        order_id
    )

    if order is None:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    # Modify the object
    order.status = data.status

    # Commit (generates UPDATE statement)
    db.commit()
    db.refresh(order)

    return order


# =====================================================================
#              SECTION 6: DELETE ORDER (Cascade Delete)
#              (For demonstrating cascade in Section 7)
# =====================================================================

@app.delete(
    "/orders/{order_id}"
)
def delete_order(
    order_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete an order.
    
    This demonstrates cascade delete:
    - Order is deleted
    - OrderItems are automatically deleted (cascade="all, delete-orphan")
    - Products are NOT deleted (no cascade)
    """
    
    order = db.get(
        models.Order,
        order_id
    )

    if order is None:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    db.delete(order)
    db.commit()

    return {
        "message": "Order deleted",
        "id": order_id
    }


# =====================================================================
#              SECTION 7: FINAL EXERCISE (Persona C)
#              GET /products/{product_id}/customers
# =====================================================================

@app.get(
    "/products/{product_id}/customers"
)
def get_product_customers(
    product_id: int,
    db: Session = Depends(get_db)
):
    """
    Get all customers who purchased a specific product.
    
    This demonstrates:
    - Complex joins (Customer → Order → OrderItem → Product)
    - Distinct (avoid duplicates if customer bought product multiple times)
    - Advanced SQLAlchemy querying
    """
    
    # Verify product exists
    product = db.get(
        models.Product,
        product_id
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    # Query: Find all customers who bought this product
    statement = (
        select(models.Customer)
        .join(models.Customer.orders)          # Customer → Orders
        .join(models.Order.items)              # Orders → OrderItems
        .where(
            models.OrderItem.product_id == product_id
        )
        .distinct()                             # Remove duplicates
    )

    customers = db.scalars(statement).all()

    # Return as list of CustomerResponse
    return [
        schemas.CustomerResponse(
            id=c.id,
            name=c.name,
            email=c.email
        )
        for c in customers
    ]


# =====================================================================
#              HEALTH CHECK
# =====================================================================

@app.get(
    "/health"
)
def health_check():
    """Simple health check endpoint"""
    return {
        "status": "ok",
        "message": "Workshop 4 API is running"
    }