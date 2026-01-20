from sqlalchemy import Column, Integer, Float, DateTime, JSON
from datetime import datetime
from app.core.database import Base

class Simulation(Base):
    __tablename__ = "simulations"

    id = Column(Integer, primary_key=True, index=True)
    monto = Column(Float, nullable=False)
    tasa_anual = Column(Float, nullable=False)
    plazo_meses = Column(Integer, nullable=False)
    tabla = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    