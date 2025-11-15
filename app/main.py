from __future__ import annotations
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.orm import Session

from app.database import engine, get_db
from app.models import Base, Product
from app import schemas

# Crear tablas al iniciar la app
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Products API", version="1.0.0")


# --------- Manejo estándar de errores en JSON --------- #

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_, exc: RequestValidationError):
    """
    Handler global para errores de validación (422).
    Para el TP no necesitamos exponer todo el detalle interno de Pydantic,
    solo devolver un error consistente con código y mensaje.
    """
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": {
                "code": 422,
                "message": "Validation error",
            }
        },
    )


# ---------------- Endpoints ---------------- #

@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post(
    "/products",
    response_model=schemas.ProductOut,
    status_code=status.HTTP_201_CREATED,
    responses={409: {"model": schemas.ErrorResponse}},
)
def create_product(
    payload: schemas.ProductCreate,
    db: Session = Depends(get_db),
):
    # Validación de unicidad por nombre + categoría
    exists = (
        db.query(Product)
        .filter(
            Product.nombre == payload.nombre,
            Product.categoria == payload.categoria,
        )
        .first()
    )
    if exists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Product with same name and category already exists",
        )

    product = Product(
        nombre=payload.nombre,
        categoria=payload.categoria,
        precio=float(payload.precio),
        descripcion=payload.descripcion,
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


@app.get(
    "/products",
    response_model=list[schemas.ProductOut],
)
def list_products(db: Session = Depends(get_db)):
    return db.query(Product).order_by(Product.id.asc()).all()

