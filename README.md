Trabajo Final DevOps – Aplicaciones Cloud Nativas / Prácticas Profesionalizantes I

Este proyecto es el trabajo final de la materia. Consiste en desarrollar una API mínima, pero completamente funcional, usando FastAPI, conectada a una base de datos PostgreSQL, y ejecutada dentro de contenedores Docker.
Además, tiene un pequeño set de tests automáticos y un workflow de CI en GitHub Actions, tal como vimos en clase.

La idea del trabajo fue demostrar que podemos armar un proyecto real “de punta a punta”, desde la API hasta el contenedor y la automatización.

🎯 Objetivo del trabajo

El objetivo principal fue:
-Crear una API simple con al menos dos endpoints (GET y POST)
-Validar datos con Pydantic
-Contenerizar todo con Docker
-Usar Docker Compose para levantar varios servicios juntos
-Conectar la API con una base de datos real
-Hacer tests automáticos básicos
-Configurar un pipeline de CI que ejecute los tests y construya la imagen
Y dejar todo bien documentado para que cualquier persona pueda ejecutar el proyecto desde cero

Segui y me base en todos los requisitos que pedia el profe en el trabajo.

📂 Estructura de mi proyecto

TPFinal-AppCloud/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── __init__.py
├── tests/
│   ├── test_app.py
│   └── __init__.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── .env.example
└── README.md

🧪 Endpoints que implemente

✔ GET /health

Lo use para verificar que la API está levantada.

✔ POST /products

Permite crear un producto nuevo.
Tiene validaciones de:

1-nombre
2-categoría
3-precio mayor a 0
4-descripción
5-y verificación de duplicados

✔ GET /products

Devuelve la lista de productos almacenados.

⚠️ Manejo de errores

Todos los errores de validación devuelven un JSON con este formato:

{
  "error": {
    "code": 422,
    "message": "Validation error"
  }
}


Si se intenta crear un producto repetido, la API devuelve:

409 Conflict

🐳 Cómo ejecutar el proyecto con Docker Compose

De esta forma podes correr todo:

1. Crear el archivo .env
cp .env.example .env

2. Levantar todo:
docker compose up --build

3. Endpoints disponibles:

http://localhost:8000/health

http://localhost:8000/products

Documentación Swagger: http://localhost:8000/docs

🧪 Tests automáticos

Para correr los tests de forma local:

pytest -q


Los tests revisan:

A. /health
B. creación correcta de productos
C. validaciones de precio
D. listado de productos

🔄 CI/CD con GitHub Actions

El repositorio tiene un workflow que corre automáticamente cada vez que se sube código. El pipeline se encarga de:

Instalar dependencias, Ejecutar los tests, Construir la imagen Docker y Si todo queda en verde, significa que el proyecto está correcto y reproducible.

🧱 Resumen de toda la arquitectura del proyecto

FastAPI como framework de la API
SQLAlchemy + PostgreSQL para manejo de datos
Dockerfile optimizado con dependencias mínimas
Docker Compose para levantar la API y la base juntas
Variables de entorno con .env
Tests automatizados con pytest
CI en GitHub Actions
Todo esto coincide con lo que hemos en clase durante el cuatrimestre.

📸 Evidencias para la entrega

El trabajo incluye capturas de:

-docker compose up funcionando
-Swagger en /docs
-/health operativo
-Creación de productos
-Resultado de los tests
-Pipeline de GitHub Actions en estado “success”

✨ Información final

Trabajo realizado por: Romina Ana Kiara Marin
Carrera: DevOps
Materia: Aplicaciones Cloud Nativas / Prácticas Profesionalizantes I
Profesor: Ale arraigada 