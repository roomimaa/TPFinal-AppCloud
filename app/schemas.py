from __future__ import annotations
from pydantic import BaseModel, Field, condecimal


class ProductBase(BaseModel):
    nombre: str = Field(min_length=1, max_length=100)
    categoria: str = Field(min_length=1, max_length=50)
    precio: condecimal(gt=0, max_digits=10, decimal_places=2)
    descripcion: str | None = Field(default=None, max_length=500)


class ProductCreate(ProductBase):
    """Schema para entrada en POST /products"""
    pass


class ProductOut(ProductBase):
    id: int

    model_config = {"from_attributes": True}


class ErrorResponse(BaseModel):
    error: dict
