from sqlalchemy.orm import Session
from app.models.simulation_model import Simulation

def save_simulation(db: Session, monto, tasa, plazo, tabla):
    sim = Simulation(
        monto = monto,
        tasa_anual = tasa,
        plazo_meses =  plazo,
        tabla = tabla
    )
    db.add(sim)
    db.commit()
    db.refresh(sim)

    return sim