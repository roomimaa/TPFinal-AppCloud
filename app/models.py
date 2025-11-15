from __future__ import annotations
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import Integer, String, Numeric, Text

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    categoria: Mapped[str] = mapped_column(String(50), nullable=False)
    precio: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    descripcion: Mapped[str | None] = mapped_column(Text, nullable=True)
