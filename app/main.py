from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.simulate_endpoint import router as simulate_router
from app.core.database import engine
from app.models.simulation_model import Simulation

app = FastAPI(title="Tabla de Amortizacion Microservicio")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://amortization-front-prueba.vercel.app", 
        "http://localhost:5173",
        "http://192.168.4.32", 
        "http://192.168.4.254",
        "https://amortization-front-prueba-q2xfjc2a9-alejandro-camperos-projects.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    if engine:
        Simulation.__table__.create(bind=engine, checkfirst=True)
        print("✅ Tabla simulations verificada/creada")
    else:
        print("⚠️ Engine no disponible en startup")



app.include_router(simulate_router)