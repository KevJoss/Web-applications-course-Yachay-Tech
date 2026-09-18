from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


# Conexión a MySQL
# Tu docker-compose usa: MYSQL_ROOT_PASSWORD=root, MYSQL_DATABASE=webshop
DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/webshop"


# Crear el engine (motor que conecta a la DB)
engine = create_engine(
    DATABASE_URL,
    echo=True  # Muestra todos los SQL generados por SQLAlchemy
)


# Crear sesiones (para transacciones)
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


# Clase base para los modelos ORM
class Base(DeclarativeBase):
    pass


# Función para obtener la sesión en las rutas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()