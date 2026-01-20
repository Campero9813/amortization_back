from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from app.schemas.simulation_schema import SimulationRequest, SimulationResponse
from app.services.amortization_service import calcular_tabla_frances
from app.services.audit_service import enviar_auditoria
from app.repositories.simulation_repository import save_simulation
from app.core.database import SessionLocal

router = APIRouter()

def get_db():
    if SessionLocal is None:
        raise RuntimeError("Database no inicializada")

    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
@router.post("/simulate", response_model=SimulationResponse)
def simulate(
    data: SimulationRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    tabla = calcular_tabla_frances(
        data.monto,
        data.tasa_anual,
        data.plazo_meses
    )
    sim = save_simulation(
        db,
        data.monto,
        data.tasa_anual,
        data.plazo_meses,
        tabla
    )

    #Auditoria Asincrona
    background_tasks.add_task(enviar_auditoria, sim.id)

    return {"tabla": tabla}