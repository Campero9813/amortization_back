from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL no está definida. Revisa el archivo .env"
    )
print("Database_URL = ", DATABASE_URL)

engine = create_engine(
    DATABASE_URL,
    echo=True,    #log SQL
    future=True  
)
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
    )

Base = declarative_base() 