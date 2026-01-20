import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("DATABASE_URL")

engine = None
SessionLocal = None
if DATABASE_URL:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(bind = engine)
else:
    raise RuntimeError(
        "DATABASE_URL no está definida. Configura el DATABASE_URL"
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