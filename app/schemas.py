from pydantic import BaseModel, Field

"""
SCHEMAS PRODUCT
"""

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, json_schema_extra={"example": "Product Name"})
    category: str = Field(..., min_length=2, max_length=100, json_schema_extra={"example": "Category Name"})
    price: float = Field(..., gt=0, json_schema_extra={"example": 19.99})
    stock: int = Field(..., ge=0, json_schema_extra={"example": 100})
    available: bool | None = None



class Product(ProductCreate):
    id: int 

class ProductUpdate(BaseModel):
    name: str | None = Field(None, min_length=2, max_length=100, json_schema_extra={"example": "Updated Product Name"})
    category: str | None = Field(None, min_length=2, max_length=100, json_schema_extra={"example": "Updated Category Name"})
    price: float | None = Field(None, gt=0, json_schema_extra={"example": 29.99})
    stock: int | None = Field(None, ge=0, json_schema_extra={"example": 50})
    available: bool | None = None

"""
SCHEMAS CATEGORY
"""
class CategoryCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, json_schema_extra={"example": "Laptoops"})
    description: str | None = Field(None,max_length=200, json_schema_extra={"example": "Computadora portátil."})
    active : bool | None = None

class Category(CategoryCreate):
    id: int

class CategoryUpdate(BaseModel):
    name: str | None = Field(None, min_length=3, max_length=50, json_schema_extra={"example": "Nombre de la categoria acutualizado"})
    description : str | None = Field(None,max_length=200, json_schema_extra={"example": "Descripcion de la categria actualizado"})
    active : bool | None = None