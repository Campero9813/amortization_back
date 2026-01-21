
# Amortization Microservice (FastAPI + PostgreSQL)

Este proyecto es un **microservicio backend** que permite simular **tablas de amortización (sistema francés)**, persistir cada simulación en una base de datos **PostgreSQL** y ejecutar un proceso de **auditoría asíncrona** que no bloquea la respuesta al usuario.

El proyecto está diseñado con **arquitectura realista de microservicios**, ideal para:
- Portafolio profesional
- Pruebas técnicas
- Proyectos fintech
- Aprendizaje de backend moderno

---

## 🧠 Características principales

- ✅ API REST con **FastAPI**
- ✅ Cálculo de amortización (sistema francés)
- ✅ Persistencia en **PostgreSQL**
- ✅ Endpoint POST `/simulate`
- ✅ Auditoría asíncrona (background tasks)
- ✅ Simulación de microservicio externo (mock de scoring)
- ✅ Arquitectura por capas
- ✅ Listo para despliegue en **Railway**
- ✅ Conexión con frontend (React/Vite)

---

## 🏗️ Arquitectura del proyecto

```
amortization-api/
│
├── app/
│   ├── main.py
│   │
│   ├── core/
│   │   └── database.py
│   │
│   ├── models/
│   │   └── simulation_model.py
│   │
│   ├── schemas/
│   │   └── simulation_schema.py
│   │
│   ├── repositories/
│   │   └── simulation_repository.py
│   │
│   ├── services/
│   │   ├── amortization_service.py
│   │   └── audit_service.py
│   │
│   └── api/
│       └── simulate_endpoint.py
│
├── requirements.txt
├── Procfile
└── README.md
```

---

## 🚀 Endpoint principal

### `POST /simulate`

Simula una tabla de amortización y guarda el resultado.

### Request body (JSON)

```json
{
  "monto": 100000,
  "tasa_anual": 12,
  "plazo_meses": 24
}
```

### Response (JSON)

```json
{
  "tabla": [
    {
      "periodo": 1,
      "cuota": 4707.35,
      "interes": 1000.0,
      "capital": 3707.35,
      "saldo": 96292.65
    }
  ]
}
```

⏱️ Tiempo de respuesta promedio: **< 200ms**  
🧵 Auditoría ejecutándose en segundo plano

---

## 🔄 Auditoría asíncrona (Mock)

Cada simulación dispara un proceso que:
- ⏳ Tarda entre **1 y 3 segundos**
- ❌ Tiene **10% de probabilidad de fallar**
- 🔥 No bloquea la respuesta al usuario

Esto simula la comunicación con un **servicio externo de scoring**.

---

## 🗄️ Persistencia (PostgreSQL)

Cada simulación se guarda con:
- Monto
- Tasa anual
- Plazo
- Tabla de amortización completa (JSON)
- Timestamp

Tabla principal:

```sql
simulations
```

---

## ⚙️ Variables de entorno

### Local
```env
DATABASE_URL=postgresql://user:password@localhost:5432/amortization_db
```

### Producción (Railway)
```env
DATABASE_URL=${{Postgres.DATABASE_URL}}
```

---

## 🧪 Pruebas locales

### Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate
```

### Instalar dependencias
```bash
pip install -r requirements.txt
```

### Levantar servidor
```bash
uvicorn app.main:app --reload
```

Swagger:
```
http://127.0.0.1:8000/docs
```

---

## 🌐 Despliegue en Railway

1. Subir proyecto a GitHub
2. Crear proyecto en Railway
3. Conectar repositorio
4. Agregar servicio PostgreSQL
5. Configurar variable `DATABASE_URL`
6. Redeploy

El backend queda disponible en una URL pública.

---

## ⚛️ Conexión con Frontend (React)

Ejemplo con Axios:

```js
import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL
});

export const simulate = async (payload) => {
  const { data } = await api.post("/simulate", payload);
  return data;
};
```

---

## 👨‍💻 Autor

Proyecto desarrollado como ejemplo de **backend profesional con Python y FastAPI**.

---
