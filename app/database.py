products_db: list[dict] = [
    {
        "id": 1,
        "name": "Computadora portatil",
        "price": 10.99,
        "stock": 100,
        "category_id": 1
    },
    {
        "id": 2,
        "name": "Smartphones",
        "price": 15.99,
        "stock": 50,
        "category_id": 2
    },
    {
        "id": 3,
        "name": "Tablets",
        "price": 20.99,
        "stock": 0,
        "category_id": 1
    },
    {
        "id": 4,
        "name": "Headphones",
        "price": 25.99,
        "stock": 30,
        "category_id": 2
    },
    {
        "id": 5,
        "name": "Product 5",
        "price": 30.99,
        "stock": 20,
        "category_id": 1
    }
]


category_db: list[dict] = [
    {
        "id": 1,
        "name": "Laptops",
        "description": "Computadora portátil.",
        "active": True
    },
    {
        "id": 2,
        "name": "Smartphones",
        "description": "Teléfono celular inteligente.",
        "active": True
    },
    {
        "id": 3,
        "name": "Tablets",
        "description": "Tableta táctil.",
        "active": True
    },
    {
        "id": 4,
        "name": "Headphones",
        "description": "Audífonos para música.",
        "active": True
    },
    {
        "id": 5,
        "name": "Monitors",
        "description": "Pantalla para computadora.",
        "active": True
    },
    {
        "id": 6,
        "name": "Keyboards",
        "description": "Teclado para computadora.",
        "active": True
    },
    {
        "id": 7,
        "name": "Mice",
        "description": "Ratón para computadora.",
        "active": False
    },
    {
        "id": 8,
        "name": "Smartwatches",
        "description": "Reloj inteligente.",
        "active": False
    },
    {
        "id": 9,
        "name": "Speakers",
        "description": "Parlantes para audio.",
        "active": False
    }
]