from dotenv import load_dotenv
load_dotenv()
from app.core.database import engine, Base
from app.models.simulation_model import Simulation

print("Creando tablas...")

Base.metadata.create_all(bind=engine)

print(type(engine))

print("Tablas creadas correctamente ✅")
