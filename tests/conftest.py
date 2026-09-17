
import pytest

from fastapi.testclient import TestClient

from app import main as main_module

from app.main import app


INITIAL_PRODUCTS = [
    {
        "id": 1,
        "name": "Product 1",
        "price": 10.99,
        "stock": 100,
        "category_id": 1
    },
    {
        "id": 2,
        "name": "Product 2",
        "price": 15.99,
        "stock": 50,
        "category_id": 2
    },
    {
        "id": 3,
        "name": "Product 3",
        "price": 20.99,
        "stock": 0,
        "category_id": 1
    },
    {
        "id": 4,
        "name": "Product 4",
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


INITIAL_CATEGORIES = [
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


@pytest.fixture(autouse=True)
def reset_db(monkeypatch):
    """Restaura ambas bases antes de cada test para evitar contaminación."""

    monkeypatch.setattr(
        main_module,
        "products_db",
        [product.copy() for product in INITIAL_PRODUCTS]
    )

    monkeypatch.setattr(
        main_module,
        "category_db",
        [category.copy() for category in INITIAL_CATEGORIES]
    )


@pytest.fixture
def client():
    return TestClient(app)

