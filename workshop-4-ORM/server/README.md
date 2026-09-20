# Server

Backend of the WebShop application, built with **FastAPI** and **SQLAlchemy** (ORM).

---

## Data Models (`models.py`)

SQLAlchemy ORM models that map directly to MySQL tables. All models inherit from `Base` (declared in `database.py`).

### Entity-Relationship overview

```
Customer (1) ──────< Order (N)
                        │
                        └──< OrderItem (N) >── Product (1)
```

---

### `Customer` → table `customers`

Represents a registered buyer.

| Column | Type          | Constraints        |
|--------|---------------|--------------------|
| `id`   | `INTEGER`     | PK, auto-increment |
| `name` | `VARCHAR(100)`| NOT NULL           |
| `email`| `VARCHAR(150)`| NOT NULL, UNIQUE   |

**Relationships:**
- `orders` → list of `Order` *(one-to-many, cascade delete)*

---

### `Product` → table `products`

A sellable item with stock tracking.

| Column  | Type            | Constraints        |
|---------|-----------------|--------------------|
| `id`    | `INTEGER`       | PK, auto-increment |
| `name`  | `VARCHAR(120)`  | NOT NULL           |
| `price` | `NUMERIC(10,2)` | NOT NULL           |
| `stock` | `INTEGER`       | default `0`        |

**Relationships:**
- `order_items` → list of `OrderItem` *(one-to-many)*

---

### `Order` → table `orders`

A purchase made by a customer, containing one or more items.

| Column        | Type          | Constraints              |
|---------------|---------------|--------------------------|
| `id`          | `INTEGER`     | PK, auto-increment       |
| `order_date`  | `DATE`        | default today            |
| `status`      | `VARCHAR(30)` | default `"pending"`      |
| `customer_id` | `INTEGER`     | FK → `customers.id`      |

**Relationships:**
- `customer` → `Customer` *(many-to-one)*
- `items` → list of `OrderItem` *(one-to-many, cascade delete)*

---

### `OrderItem` → table `order_items`

A line item inside an order — links a product to an order with quantity and price at time of purchase.

| Column       | Type            | Constraints         |
|--------------|-----------------|---------------------|
| `id`         | `INTEGER`       | PK, auto-increment  |
| `quantity`   | `INTEGER`       | NOT NULL            |
| `unit_price` | `NUMERIC(10,2)` | NOT NULL            |
| `order_id`   | `INTEGER`       | FK → `orders.id`    |
| `product_id` | `INTEGER`       | FK → `products.id`  |

**Relationships:**
- `order` → `Order` *(many-to-one)*
- `product` → `Product` *(many-to-one)*

---

## Pydantic Schemas (`schemas.py`)

`schemas.py` defines the **data contracts** between the API and its consumers.
While `models.py` controls how data is *stored* in the database, schemas control what the API *accepts as input* and what it *returns as output*. This separation prevents accidentally exposing internal fields (e.g. passwords, FKs) and ensures all incoming data is validated before touching the database.

Each entity follows a 3-variant pattern:

| Variant   | Used in         | Purpose                                           |
|-----------|-----------------|---------------------------------------------------|
| `*Create` | `POST`          | Fields the client must send to create a resource  |
| `*Update` | `PATCH` / `PUT` | Same fields but all **optional** (partial update) |
| `*Response` | all responses | What the API returns; includes `id`, excludes internal fields |

> **`from_attributes=True`** in `*Response` schemas allows Pydantic to read SQLAlchemy ORM objects directly, without manual conversion to dicts.

### Customer schemas

| Class                        | Fields                              |
|------------------------------|-------------------------------------|
| `CustomerCreate`             | `name`, `email`                     |
| `CustomerUpdate`             | `name?`, `email?`                   |
| `CustomerResponse`           | `id`, `name`, `email`               |
| `CustomerWithOrdersResponse` | `id`, `name`, `email`, `orders[]`   |

### Product schemas

| Class             | Fields                       |
|-------------------|------------------------------|
| `ProductCreate`   | `name`, `price`, `stock`     |
| `ProductUpdate`   | `name?`, `price?`, `stock?`  |
| `ProductResponse` | `id`, `name`, `price`, `stock` |

### Order schemas

| Class               | Fields                                        |
|---------------------|-----------------------------------------------|
| `OrderCreate`       | `customer_id`, `items[]` (`OrderItemCreate`)  |
| `OrderResponse`     | `id`, `order_date`, `status`, `customer`, `items[]` |
| `OrderStatusUpdate` | `status`                                      |

### OrderItem schemas

| Class               | Fields                               |
|---------------------|--------------------------------------|
| `OrderItemCreate`   | `product_id`, `quantity`             |
| `OrderItemResponse` | `id`, `quantity`, `unit_price`, `product` |

---

## Application Entry Point (`main.py`)

`main.py` is the root of the FastAPI application. It wires together the database, models, and schemas to expose HTTP endpoints.

### Responsibilities

| Responsibility | How |
|---|---|
| Creates all DB tables | `Base.metadata.create_all(bind=engine)` runs on startup |
| Initializes the FastAPI app | `app = FastAPI()` |
| Declares HTTP routes | `@app.get()`, `@app.post()`, etc. |
| Injects DB sessions | `Depends(get_db)` passes a session to each endpoint |

### Auto table creation

```python
Base.metadata.create_all(bind=engine)
```

This line runs **once at startup**. It inspects all models registered under `Base` and creates the corresponding tables in MySQL if they do not exist yet. This means the database schema is always in sync with `models.py` without running manual SQL.

### Dependency injection — `Depends(get_db)`

Each endpoint that needs the database receives a session via FastAPI's dependency system:

```python
@app.get("/customers/{id}")
def get_customer(id: int, db: Session = Depends(get_db)):
    ...
```

`get_db` (defined in `database.py`) opens a session, yields it to the endpoint, and closes it automatically when the request finishes — even if an error occurs.

### Current endpoints

#### Health check

| Method | Path | Description |
|--------|------|-------------|
| `GET`  | `/`  | Health check — returns `{"message": "ORM Workshop API"}` |

#### Customers (`/customers`)

| Method   | Path                      | Request body            | Response                   | Description                          |
|----------|---------------------------|-------------------------|----------------------------|--------------------------------------|
| `POST`   | `/customers`              | `CustomerCreate`        | `CustomerResponse`         | Creates a new customer               |
| `GET`    | `/customers`              | —                       | `list[CustomerResponse]`   | Returns all customers                |
| `GET`    | `/customers/{id}`         | —                       | `CustomerResponse`         | Returns a single customer by ID      |
| `PUT`    | `/customers/{id}`         | `CustomerUpdate`        | `CustomerResponse`         | Partially updates a customer (name and/or email) |
| `DELETE` | `/customers/{id}`         | —                       | `{"message": ..., "id": ...}` | Deletes a customer by ID          |

> **404 behaviour:** `GET`, `PUT`, and `DELETE` by ID raise `HTTP 404 – Customer not found` if the customer does not exist.

#### Products (`/products`)

| Method   | Path                    | Request body      | Response                      | Description                              |
|----------|-------------------------|-------------------|-------------------------------|------------------------------------------|
| `POST`   | `/products`             | `ProductCreate`   | `ProductResponse`             | Creates a new product                    |
| `GET`    | `/products`             | —                 | `list[ProductResponse]`       | Returns all products                     |
| `GET`    | `/products/{id}`        | —                 | `ProductResponse`             | Returns a single product by ID           |
| `PUT`    | `/products/{id}`        | `ProductUpdate`   | `ProductResponse`             | Partially updates a product (name, price and/or stock) |
| `DELETE` | `/products/{id}`        | —                 | `{"message": ..., "id": ...}` | Deletes a product by ID                  |

> **404 behaviour:** `GET`, `PUT`, and `DELETE` by ID raise `HTTP 404 – Product not found` if the product does not exist.

#### Orders (`/orders`)

| Method | Path      | Request body   | Response        | Description                                        |
|--------|-----------|----------------|-----------------|----------------------------------------------------|
| `POST` | `/orders` | `OrderCreate`  | `OrderResponse` | Creates a new order with one or more items         |

**Request body — `OrderCreate`:**

```json
{
  "customer_id": 1,
  "items": [
    { "product_id": 3, "quantity": 2 },
    { "product_id": 7, "quantity": 1 }
  ]
}
```

**Nested insert behaviour:**

1. Validates that `customer_id` exists → `404 – Customer not found` if not.
2. For each item in `items`, validates that `product_id` exists → `404 – Product not found` if not.
3. Captures `unit_price` from `product.price` **at the time of the request** (price snapshot).
4. Appends each `OrderItem` to the `Order` and persists everything in a single `db.commit()`.
5. Returns the full order with nested `customer` and `items[].product` via `OrderResponse`.

### Running the server

From the **project root** (`workshop-4-ORM/`) with the virtual environment active:

```bash
uvicorn server.main:app --host 0.0.0.0 --port 8000 --reload
```

| Flag | Purpose |
|------|---------|
| `server.main:app` | Python module path to the FastAPI instance |
| `--host 0.0.0.0` | Accepts connections from any network interface |
| `--port 8000` | Port to listen on |
| `--reload` | Auto-restarts on file changes (development only) |

The interactive API docs are available at: <http://localhost:8000/docs>
