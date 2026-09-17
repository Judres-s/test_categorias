# INSTRUCCIONES PARA LA EJECUCIÓN DEL PROYECTO

## Estructura del proyecto

```text
C:.
│   .gitignore
│   README.md
│   requirements.txt
│
├───app
│       database.py
│       main.py
│       schemas.py
│       __init__.py
│
├───docs
│       Actividad_Autonoma_API_Categorias_FastAPI.pdf
│       CASOS_DE_PRUEBA.TXT
│
├───Liteclient
│       fast_api_productos_categorias.postman_collection.json
│
└───tests
        conftest.py
        test_categories.py
        test_products.py
        __init__.py
```

## 1. Crear el entorno virtual

Para aislar las dependencias del proyecto, primero se debe crear un entorno virtual:

```bash
python -m venv .venv
```

## 2. Activar el entorno virtual

En Windows PowerShell, active el entorno mediante el siguiente comando:

```powershell
.\.venv\Scripts\Activate.ps1
```

## 3. Instalar las dependencias

Las librerías necesarias pueden instalarse directamente mediante:

```bash
pip install fastapi "uvicorn[standard]" pytest httpx
```

También es posible instalarlas utilizando el archivo `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

## 4. Ejecutar el servidor

Una vez instaladas las dependencias, inicie la aplicación utilizando Uvicorn:

```bash
uvicorn app.main:app --reload
```

El servidor estará disponible de forma local en el puerto 8000.

# Endpoints de Categorías

| Método | Endpoint           | Descripción                                                                             | Códigos       |
| ------ | ------------------ | --------------------------------------------------------------------------------------- | ------------- |
| GET    | `/categories`      | Obtiene todas las categorías y permite aplicar filtros mediante `?active=` y `?search=` | 200           |
| GET    | `/categories/{id}` | Busca una categoría específica mediante su identificador                                | 200, 404      |
| POST   | `/categories`      | Registra una nueva categoría                                                            | 201, 422      |
| PATCH  | `/categories/{id}` | Modifica parcialmente una categoría existente                                           | 200, 404, 422 |
| DELETE | `/categories/{id}` | Elimina una categoría mediante su identificador                                         | 204, 404      |

# Pruebas con LiteClient

## Guía rápida para probar la API

La API puede probarse mediante herramientas como Postman, Insomnia u otros clientes HTTP. A continuación se indican las características principales de cada método.

## Configuración según el método HTTP

| Método | Función                         | ¿Utiliza body?                        | Headers                          | ¿Requiere ID en la URL? |
| ------ | ------------------------------- | ------------------------------------- | -------------------------------- | ----------------------- |
| GET    | Consultar o buscar información  | No                                    | No                               | Opcional                |
| POST   | Crear un nuevo registro         | Sí                                    | `Content-Type: application/json` | No                      |
| PATCH  | Modificar información existente | Sí, únicamente los campos a modificar | `Content-Type: application/json` | Sí                      |
| DELETE | Eliminar un registro            | No                                    | No                               | Sí                      |

## Uso del body

* **POST:** Se deben enviar todos los campos requeridos por el esquema. Si falta alguno o tiene un formato incorrecto, la API responderá con un código `422`.

* **PATCH:** Solo es necesario enviar los atributos que se desean modificar. Por ejemplo, para cambiar únicamente el precio, se puede enviar:

```json
{
    "price": 10.99
}
```

* **GET y DELETE:** No requieren un body. La información necesaria se proporciona mediante la URL, los parámetros de consulta o el identificador correspondiente.

## Consideraciones importantes

### Headers

Para las solicitudes `POST` y `PATCH`, se debe establecer el siguiente encabezado:

```text
Content-Type: application/json
```

Esto permite que el servidor interprete correctamente la información enviada en formato JSON.

### URLs

Se recomienda utilizar las rutas sin una barra `/` al final. Por ejemplo:

```text
/products
```

en lugar de:

```text
/products/
```

Esto evita posibles redirecciones innecesarias durante las solicitudes.

### Códigos de error frecuentes

* **404:** El recurso o identificador solicitado no existe.
* **422:** Los datos enviados no cumplen con el formato o los campos definidos por la API.
* **405:** El método HTTP utilizado no está permitido para esa ruta.

# Documentación de la API

FastAPI genera automáticamente documentación interactiva para consultar y probar los diferentes endpoints.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

# Productos

En esta sección se encuentran los endpoints y funcionalidades relacionados con la gestión de productos.

# Categorías

En esta sección se encuentran los endpoints y funcionalidades correspondientes a la administración de categorías.
