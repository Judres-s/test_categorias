# =====================================================
# TESTS DE CATEGORÍAS
# CP-CAT-01 a CP-CAT-07
# =====================================================


# CP-CAT-01 - Crear categoría válida
def test_create_valid_category(client):
    payload = {
        "name": "Periféricos",
        "description": "Dispositivos periféricos",
        "active": True
    }

    response = client.post("/categories", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Periféricos"
    assert data["description"] == "Dispositivos periféricos"
    assert data["active"] is True
    assert "id" in data


# CP-CAT-02 - Listar categorías
def test_list_categories(client):
    response = client.get("/categories")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


# CP-CAT-03 - Consultar categoría existente
def test_get_existing_category(client):
    response = client.get("/categories/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert "name" in data


# CP-CAT-04 - Consultar categoría inexistente
def test_get_non_existing_category(client):
    response = client.get("/categories/99999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Category not found"}


# CP-CAT-05 - Nombre de categoría menor a 3 caracteres
def test_create_category_name_too_short(client):
    response = client.post(
        "/categories",
        json={"name": "AB"}
    )

    assert response.status_code == 422


# CP-CAT-06 - Nombre de categoría exactamente de 3 caracteres
def test_create_category_name_exactly_3_characters(client):
    response = client.post(
        "/categories",
        json={"name": "PCs"}
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "PCs"


# CP-CAT-07 - Nombre de categoría duplicado sin distinguir mayúsculas
def test_create_duplicate_category_case_insensitive(client):

    existing_category = client.get("/categories/1").json()
    existing_name = existing_category["name"]

    response = client.post(
        "/categories",
        json={"name": existing_name.upper()}
    )

    assert response.status_code == 409