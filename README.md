# 📊 Amortization Frontend

**amortization-frontend** es una **Single Page Application (SPA)** desarrollada con **React, TypeScript y Vite**, que permite calcular y visualizar **tablas de amortización** a partir de los datos ingresados por el usuario, consumiendo una **API REST** como backend.

---

## 🚀 Descripción del Proyecto

Esta aplicación permite a los usuarios:

- Ingresar el **monto del préstamo**
- Definir la **tasa de interés**
- Establecer el **plazo**
- Calcular la **tabla de amortización**
- Visualizar los resultados en una **tabla clara y dinámica**

El frontend se comunica con una API REST encargada de realizar los cálculos financieros.

---

## 🖥️ Tipo de Aplicación

- **Single Page Application (SPA)**

---

## 🛠️ Tecnologías Utilizadas

- **React**
- **TypeScript**
- **Vite**
- **CSS**

---

## 📂 Estructura del Proyecto

```
src/
├── assets/        # Recursos estáticos (imágenes, íconos, etc.)
├── components/    # Componentes reutilizables de la UI
├── services/      # Servicios para consumo de la API REST
├── App.css        # Estilos globales
├── App.tsx        # Componente principal
├── index.css      # Estilos base
└── main.tsx       # Punto de entrada
```

---

## 🔌 Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto:

```
VITE_API_URL=http://localhost:8080
```

---

## 📦 Scripts Disponibles

```
npm install
npm run dev
npm run build
npm run preview
npm run lint
```

---

## 🔗 Comunicación con Backend

- Consumo de API REST
- Lógica de comunicación ubicada en `services`
- URL configurable mediante variables de entorno

---

## 🎯 Objetivo del Proyecto

SPA moderna orientada a buenas prácticas de desarrollo frontend y consumo de servicios REST, pensada como parte de un portafolio profesional.

---

## 📌 Próximas Mejoras

- Validaciones avanzadas
- Manejo de loading y errores
- Mejoras visuales
- Pruebas unitarias
- Deploy en Vercel o Netlify
