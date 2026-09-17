# =====================================================
# TESTS DE PRODUCTOS
# CP-PROD-01 a CP-PROD-18
# =====================================================


# CP-PROD-01 - Crear producto válido
def test_create_valid_product(client):
    payload = {
        "name": "Teclado mecánico",
        "price": 250000,
        "stock": 10,
        "category_id": 1
    }

    response = client.post("/products", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Teclado mecánico"
    assert data["price"] == 250000
    assert data["stock"] == 10
    assert data["category_id"] == 1
    assert "id" in data


# CP-PROD-02 - Listar productos
def test_get_products(client):
    response = client.get("/products/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


# CP-PROD-03 - Consultar producto existente
def test_get_existing_product(client):
    response = client.get("/products/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert "name" in data


# CP-PROD-04 - Consultar producto inexistente
def test_get_non_existing_product(client):
    response = client.get("/products/99999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Product not found"}


# CP-PROD-05 - Actualizar producto existente
def test_update_existing_product(client):
    response = client.put(
        "/products/1",
        json={"price": 99999}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["price"] == 99999


# CP-PROD-06 - Actualizar producto inexistente
def test_update_non_existing_product(client):
    response = client.put(
        "/products/99999",
        json={"price": 99999}
    )

    assert response.status_code == 404


# CP-PROD-07 - Eliminar producto existente
def test_delete_existing_product(client):

    created = client.post(
        "/products",
        json={
            "name": "Producto para eliminar",
            "price": 10000,
            "stock": 1,
            "category_id": 1
        }
    )

    assert created.status_code == 201

    product_id = created.json()["id"]

    response = client.delete(
        f"/products/{product_id}"
    )

    assert response.status_code == 204

    response_get = client.get(
        f"/products/{product_id}"
    )

    assert response_get.status_code == 404


# CP-PROD-08 - Eliminar producto inexistente
def test_delete_non_existing_product(client):
    response = client.delete("/products/99999")

    assert response.status_code == 404


# CP-PROD-09 - Nombre menor a 3 caracteres
def test_product_name_too_short(client):
    response = client.post(
        "/products",
        json={
            "name": "AB",
            "price": 10000,
            "stock": 5,
            "category_id": 1
        }
    )

    assert response.status_code == 422


# CP-PROD-10 - Nombre exactamente de 3 caracteres
def test_product_name_exactly_3_characters(client):
    response = client.post(
        "/products",
        json={
            "name": "PC1",
            "price": 10000,
            "stock": 5,
            "category_id": 1
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "PC1"


# CP-PROD-11 - Precio igual a 0
def test_product_price_zero(client):
    response = client.post(
        "/products",
        json={
            "name": "Producto precio cero",
            "price": 0,
            "stock": 5,
            "category_id": 1
        }
    )

    assert response.status_code == 422


# CP-PROD-12 - Precio negativo
def test_product_price_negative(client):
    response = client.post(
        "/products",
        json={
            "name": "Producto precio negativo",
            "price": -1000,
            "stock": 5,
            "category_id": 1
        }
    )

    assert response.status_code == 422


# CP-PROD-13 - Precio mínimo positivo
def test_product_minimum_positive_price(client):
    response = client.post(
        "/products",
        json={
            "name": "Producto mínimo",
            "price": 0.01,
            "stock": 5,
            "category_id": 1
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["price"] == 0.01


# CP-PROD-14 - Stock igual a 0
def test_product_stock_zero(client):
    response = client.post(
        "/products",
        json={
            "name": "Monitor sin stock",
            "price": 850000,
            "stock": 0,
            "category_id": 1
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["stock"] == 0


# CP-PROD-15 - Stock negativo
def test_product_stock_negative(client):
    response = client.post(
        "/products",
        json={
            "name": "Producto stock negativo",
            "price": 10000,
            "stock": -1,
            "category_id": 1
        }
    )

    assert response.status_code == 422


# CP-PROD-16 - Categoría inexistente al crear producto
def test_create_product_with_non_existing_category(client):
    response = client.post(
        "/products",
        json={
            "name": "Producto categoría inexistente",
            "price": 10000,
            "stock": 5,
            "category_id": 99999
        }
    )

    assert response.status_code == 404


# CP-PROD-17 - Precio inválido al actualizar
def test_update_product_invalid_price(client):
    response = client.put(
        "/products/1",
        json={"price": 0}
    )

    assert response.status_code == 422


# CP-PROD-18 - Categoría inexistente al actualizar
def test_update_product_non_existing_category(client):
    response = client.put(
        "/products/1",
        json={"category_id": 99999}
    )

    assert response.status_code == 404