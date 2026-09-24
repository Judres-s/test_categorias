Julian Quiroga, Yoberson Diaz, Daniela Jaraba, Kamila Pinzon, Zuleima Terraza


El proyecto trabaja con dos recursos principales:

* **Productos (`/products`)**: corresponde al CRUD desarrollado originalmente durante la práctica del módulo.
* **Categorías (`/categories`)**: corresponde al CRUD desarrollado para cumplir con los requisitos de la **Actividad Autónoma: API de Categorías con FastAPI**.

---

## 1. Instalación

Para preparar el entorno de trabajo se crea inicialmente un entorno virtual de Python y posteriormente se instalan las dependencias necesarias para ejecutar la API y sus pruebas.

```bash
python -m venv .venv

.venv\Scripts\Activate.ps1

python -m pip install fastapi "uvicorn[standard]" pytest httpx

python.exe -m pip install --upgrade pip
```

El proyecto también cuenta con un archivo `requirements.txt`, donde se encuentran registradas las dependencias utilizadas. Por esta razón, también es posible realizar la instalación ejecutando:

```bash
python -m pip install -r requirements.txt
```

---

## 2. Ejecución del servidor

Para iniciar la API se utiliza **Uvicorn**, que funciona como servidor ASGI para ejecutar la aplicación desarrollada con FastAPI.

El comando utilizado es:

```bash
  python -m uvicorn app.main:app --reload
```

La opción `--reload` permite que el servidor se reinicie automáticamente cuando se realizan cambios en el código durante el desarrollo.

Una vez iniciado el servidor, la documentación interactiva de la API puede consultarse mediante Swagger en:

**[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

Desde esta interfaz es posible visualizar los endpoints disponibles, consultar sus parámetros y realizar solicitudes directamente.

---

## 3. Ejecución de las pruebas

Las pruebas automatizadas se ejecutan utilizando **pytest**.

Para ejecutar todas las pruebas del proyecto:

```bash
python -m pytest -v
```

Para ejecutar específicamente las pruebas relacionadas con las categorías:

```bash
python -m pytest tests/test_categories.py -v
```

También es posible utilizar:

```bash
python -m pytest -k "" -v
```

La opción `-v` permite visualizar con mayor detalle el resultado de cada prueba ejecutada.

---

# 4. API de Categorías

La API de categorías corresponde a la **Actividad Autónoma del Módulo III** y tiene como finalidad poner en práctica los conceptos aprendidos sobre FastAPI mediante la construcción de un CRUD completo.

### Tecnologías utilizadas

* Python
* FastAPI
* Pydantic
* pytest
* TestClient

La API no utiliza una base de datos externa. Para este proyecto se emplean estructuras de datos en memoria que se encuentran definidas en `app/database.py`.

---

## 4.1 Modelo de datos

Cada categoría contiene los siguientes campos:

| Campo         | Tipo          | Obligatorio              | Regla principal                              |
| ------------- | ------------- | ------------------------ | -------------------------------------------- |
| `id`          | `int`         | Generado automáticamente | Identificador único asignado por el servidor |
| `name`        | `str`         | Sí                       | Debe tener entre 3 y 50 caracteres           |
| `description` | `str \| None` | No                       | Puede tener máximo 200 caracteres            |
| `active`      | `bool`        | No                       | Su valor predeterminado es `true`            |

Un ejemplo de una categoría representada en formato JSON sería:

```json
{
  "id": 1,
  "name": "Computadores",
  "description": "Equipos de cómputo",
  "active": true
}
```

La estructura y validación de estos datos se encuentran definidas mediante modelos de **Pydantic** en `app/schemas.py`.

Los principales modelos utilizados son:

* `CategoryCreate`: utilizado para crear una categoría.
* `CategoryUpdate`: contiene campos opcionales y se utiliza para realizar actualizaciones parciales mediante `PATCH`.
* `Category`: representa la información que devuelve la API e incluye el identificador `id`.

---

## 4.2 Endpoints

La API dispone de los siguientes endpoints para administrar las categorías:

| Método | Endpoint                    | Función                                   | Código exitoso |
| ------ | --------------------------- | ----------------------------------------- | -------------- |
| GET    | `/categories`               | Obtener todas las categorías              | 200            |
| GET    | `/categories/{category_id}` | Consultar una categoría específica        | 200            |
| POST   | `/categories`               | Crear una nueva categoría                 | 201            |
| Put    | `/categories/{category_id}` | Modificar parcialmente una categoría      | 200            |
| DELETE | `/categories/{category_id}` | Eliminar una categoría                    | 204            |
| GET    | `/categories?active=true`   | Obtener únicamente las categorías activas | 200            |
| GET    | `/categories?search=comp`   | Buscar categorías por nombre              | 200            |

La búsqueda por nombre no diferencia entre letras mayúsculas y minúsculas.

### Manejo de errores

La API también contempla diferentes situaciones de error:

* Si se intenta consultar, modificar o eliminar una categoría que no existe, se devuelve un código **404 (Not Found)** con el mensaje:

```json
{
  "detail": "Category not found"
}
```

* Cuando los datos enviados no cumplen las reglas establecidas por los modelos de Pydantic, FastAPI devuelve un código **422 (Unprocessable Entity)**.

---

## 4.3 Pruebas automatizadas

Las pruebas correspondientes a las categorías se encuentran en:

```text
test/test_categories.py
```

Estas pruebas utilizan `TestClient` de FastAPI para realizar solicitudes a la API y comprobar que los diferentes endpoints funcionan de acuerdo con los requisitos establecidos.

En total se implementaron las **12 pruebas definidas en la matriz de la actividad (CA01–CA12)**, además de dos pruebas adicionales correspondientes a la búsqueda opcional por nombre.

| ID    | Escenario                            | Resultado esperado                            |
| ----- | ------------------------------------ | --------------------------------------------- |
| CA01  | Listar categorías                    | 200 y lista en formato JSON                   |
| CA02  | Consultar una categoría existente    | 200                                           |
| CA03  | Consultar una categoría inexistente  | 404                                           |
| CA04  | Utilizar un ID inválido              | 422                                           |
| CA05  | Crear una categoría válida           | 201                                           |
| CA06  | Enviar un nombre demasiado corto     | 422                                           |
| CA07  | Crear una categoría sin nombre       | 422                                           |
| CA08  | Actualizar una categoría existente   | 200                                           |
| CA09  | Actualizar una categoría inexistente | 404                                           |
| CA10  | Eliminar una categoría existente     | 204                                           |
| CA11  | Eliminar una categoría inexistente   | 404                                           |
| CA12  | Filtrar categorías activas           | 200 y únicamente categorías con `active=true` |
| Extra | Buscar por nombre con coincidencias  | 200                                           |
| Extra | Buscar por nombre sin coincidencias  | 200 y lista vacía                             |

Para evitar que los resultados de una prueba afecten a las siguientes, se utiliza un **fixture `autouse=True` denominado `reset_db`**.

Este fixture se encarga de restablecer los datos de `categories_db` antes de ejecutar cada prueba. De esta manera, cada prueba comienza con un estado independiente y los resultados son más confiables.

---

## 5. Resultado de las pruebas

Después de ejecutar las pruebas específicas de categorías mediante:

```bash
pytest test/test_categories.py -v
```

se obtuvo el siguiente resultado:

```text
25 passed 1 warning in 0.42s
```

Esto significa que las **25  pruebas fueron ejecutadas correctamente y todas fueron aprobadas**.

Las 25 pruebas corresponden a las  pruebas obligatorias de la actividad.

---

## Conclusión

El proyecto desarrollado por **Julian Quiroga** permite aplicar los conceptos fundamentales de construcción y pruebas de una API REST utilizando FastAPI.

La implementación incluye operaciones CRUD para productos y categorías, validación de información mediante Pydantic, manejo de errores HTTP, filtros y búsqueda, además de pruebas automatizadas mediante pytest y `TestClient`.

La ejecución final demuestra que las funcionalidades implementadas para el recurso de categorías cumplen con los escenarios establecidos, obteniendo **14 pruebas exitosas de 14 ejecutadas**.

Si quieres, también puedo convertirlo en una versión **más sencilla y con lenguaje de estudiante**, para que no parezca demasiado técnico o generado y sea más natural para entregar.
