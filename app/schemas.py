from pydantic import BaseModel, Field

"""
SCHEMAS PRODUCT
"""

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=80, json_schema_extra={"example": "Teclado mecánico"})
    price: float = Field(..., gt=0, json_schema_extra={"example": 250000})
    stock: int = Field(..., ge=0, json_schema_extra={"example": 10})
    category_id: int = Field(..., json_schema_extra={"example": 1})


class Product(ProductCreate):
    id: int


class ProductUpdate(BaseModel):

    name: str | None = Field(None, min_length=3, max_length=80, json_schema_extra={"example": "Updated Product Name"})

    category_id: int | None = Field(None, json_schema_extra={"example": 1})

    price: float | None = Field(None, gt=0, json_schema_extra={"example": 29.99})

    stock: int | None = Field(None, ge=0, json_schema_extra={"example": 50})

    available: bool | None = None


"""
SCHEMAS CATEGORY
"""

class CategoryCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=60, json_schema_extra={"example": "Periféricos"})
    description: str | None = Field(None,max_length=200, json_schema_extra={"example": "Computadora portátil."})
    active : bool | None = None


class Category(CategoryCreate):
    id: int


class CategoryUpdate(BaseModel):
    name: str | None = Field(None, min_length=3, max_length=60, json_schema_extra={"example": "Nombre de la categoria actualizado"})
    description : str | None = Field(None,max_length=200, json_schema_extra={"example": "Descripcion de la categoria actualizado"})
    active : bool | None = None