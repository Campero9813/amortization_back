from pydantic import BaseModel
from typing import List, Dict

class AmortizationPeriod(BaseModel):
    periodo: int
    cuota: float
    interes: float
    capital: float
    saldo: float

class SimulationRequest(BaseModel):
    monto: float
    tasa_anual: float
    plazo_meses: int

class SimulationResponse(BaseModel):
    tabla: List[AmortizationPeriod]

