from fastapi import FastAPI, HTTPException, Response, status


from app.database import products_db, category_db

from app.schemas import (
    Product, ProductCreate, ProductUpdate,
    Category, CategoryCreate, CategoryUpdate
)


app = FastAPI(
    title="Product API",
    description="A simple API for managing products",
    version="1.0.0"
)


@app.get("/", tags=["Funcionamiento"])
def root():
    return {"message": "Hello, World! api Functional!"}


"""
----------------------------------------------------
PRODUCTOS
----------------------------------------------------
"""


@app.get("/products/", response_model=list[Product], tags=["Products"])
def get_product(
    category_id: int | None = None,
    search: str | None = None
):
    result = products_db

    if category_id is not None:
        result = [
            product
            for product in result
            if product["category_id"] == category_id
        ]

    if search is not None:
        result = [
            product
            for product in result
            if search.lower() in product["name"].lower()
        ]

    return result


@app.get("/products/{product_id}", response_model=Product, tags=["Products"])
def get_product_by_id(product_id: int):
    product = next(
        (product for product in products_db if product["id"] == product_id),
        None
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


def get_next_product_id() -> int:
    if not products_db:
        return 1

    return max(product["id"] for product in products_db) + 1


@app.post(
    "/products",
    response_model=Product,
    status_code=status.HTTP_201_CREATED,
    tags=["Products"]
)
def create_product(product: ProductCreate):

    category = next(
        (
            category
            for category in category_db
            if category["id"] == product.category_id
        ),
        None
    )

    if category is None:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    new_product = {
        "id": get_next_product_id(),
        **product.model_dump()
    }

    products_db.append(new_product)

    return new_product


@app.put(
    "/products/{product_id}",
    response_model=Product,
    tags=["Products"]
)
def update_product(
    product_id: int,
    product_update: ProductUpdate
):
    product = next(
        (product for product in products_db if product["id"] == product_id),
        None
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    update_data = product_update.model_dump(exclude_unset=True)

    if "category_id" in update_data:

        category = next(
            (
                category
                for category in category_db
                if category["id"] == update_data["category_id"]
            ),
            None
        )

        if category is None:
            raise HTTPException(
                status_code=404,
                detail="Category not found"
            )

    for key, value in update_data.items():
        product[key] = value

    return product


@app.delete(
    "/products/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Products"]
)
def delete_product(product_id: int):

    product = next(
        (product for product in products_db if product["id"] == product_id),
        None
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    products_db.remove(product)

    return Response(
        status_code=status.HTTP_204_NO_CONTENT
    )


@app.get("/health", tags=["Funcionamiento"])
def health_check():
    return {"status": "healthy"}


"""
-------------------------------------------------------------------
CATEGORIAS
-------------------------------------------------------------------
"""


def get_next_category_id() -> int:
    if not category_db:
        return 1

    return max(category["id"] for category in category_db) + 1


@app.get(
    "/categories",
    response_model=list[Category],
    tags=["Categories"]
)
def get_categories(
    active: bool | None = None,
    search: str | None = None
):
    result = category_db

    if active is not None:
        result = [
            category
            for category in result
            if category.get("active") == active
        ]

    if search is not None:
        result = [
            category
            for category in result
            if search.lower() in category["name"].lower()
        ]

    return result


@app.get(
    "/categories/{category_id}",
    response_model=Category,
    tags=["Categories"]
)
def get_category_by_id(category_id: int):

    category = next(
        (
            category
            for category in category_db
            if category["id"] == category_id
        ),
        None
    )

    if category is None:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return category


@app.post(
    "/categories",
    response_model=Category,
    status_code=status.HTTP_201_CREATED,
    tags=["Categories"]
)
def create_category(category: CategoryCreate):

    for existing_category in category_db:

        if existing_category["name"].lower() == category.name.lower():
            raise HTTPException(
                status_code=409,
                detail="Category already exists"
            )

    new_category = {
        "id": get_next_category_id(),
        **category.model_dump()
    }

    category_db.append(new_category)

    return new_category


@app.put(
    "/categories/{category_id}",
    response_model=Category,
    tags=["Categories"]
)
def update_category(
    category_id: int,
    category_update: CategoryUpdate
):

    category = next(
        (
            category
            for category in category_db
            if category["id"] == category_id
        ),
        None
    )

    if category is None:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    update_data = category_update.model_dump(exclude_unset=True)

    if "name" in update_data:

        for existing_category in category_db:

            if (
                existing_category["id"] != category_id
                and existing_category["name"].lower()
                == update_data["name"].lower()
            ):
                raise HTTPException(
                    status_code=409,
                    detail="Category already exists"
                )

    for key, value in update_data.items():
        category[key] = value

    return category


@app.delete(
    "/categories/{category_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Categories"]
)
def delete_category(category_id: int):

    category = next(
        (
            category
            for category in category_db
            if category["id"] == category_id
        ),
        None
    )

    if category is None:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    category_db.remove(category)

    return Response(
        status_code=status.HTTP_204_NO_CONTENT
    )