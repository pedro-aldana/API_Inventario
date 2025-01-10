from pydantic import BaseModel
from typing import Optional


# Esquema para crear productos
class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    category_id: int  # Solo este campo es requerido (el user_id lo obtienes de la autenticación)


# Esquema para actualizar productos
class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = ""
    price: Optional[float] = None
    category_id: Optional[int] = None  # Todos los campos son opcionales para mayor flexibilidad


# Esquema para salida de productos
class ProductOut(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    category_id: int
    user_id: int  # Esto lo puedes devolver al cliente

    class Config:
        orm_mode = True
