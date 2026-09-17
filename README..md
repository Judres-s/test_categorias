# INSTRUCCIONES PARA LA EJECUCION DEL PROYECTO
# Estructura
```
C:.
│   .gitignore
│   README..md
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
### 1.CREAR EL ENTORNO VIRTUAL
```
python -m venv .venv
```
### 2.ACTIVAR EL ENTORNO
```
.\.venv\Scripts\Activate.ps1
```
### 3.INSTALAR LAS DEPENDENCIAS
```
pip install fastapi "uvicorn[standard]" pytest httpx
```
O
```
python -m pip install -r requirements.txt
```
### EJECUTAR EL SERVIDOR (UVICORN)

```
uvicorn app.main:app --reload   
```
## Endpoints de Categorías

| Método | Endpoint | Descripción | Códigos |
|--------|----------|-------------|---------|
| GET | /categories | Lista todas las categorías (filtros: ?active=, ?search=) | 200 |
| GET | /categories/{id} | Consulta una categoría por ID | 200, 404 |
| POST | /categories | Crea una categoría nueva | 201, 422 |
| PATCH | /categories/{id} | Actualiza parcialmente una categoría | 200, 404, 422 |
| DELETE | /categories/{id} | Elimina una categoría | 204, 404 |
# PRUEBAS LITECLIENT
# Guía rápida para probar la API (sin renegar)

Si vas a usar Insomnia, Postman o cualquier cliente, acá va una ayuda memoria de cómo configurar cada método. No es la biblia, pero te va a salvar.

## Lo básico según el método

| Método | ¿Pa' qué? | ¿Lleva body? | ¿Headers? | ¿ID en la URL? |
|--------|-----------|--------------|-----------|----------------|
| GET | Ver o buscar | No | No | Opcional (si buscas uno solo) |
| POST | Crear | Sí, todo | Sí, `Content-Type: application/json` | No |
| PATCH | Editar algo | Sí, solo lo que cambias | Sí, `Content-Type: application/json` | Sí |
| DELETE | Borrar | No | No | Sí |

## ¿Y el body?

- **POST:** Mandás todo. Si te falta un campo, la API te va a tirar un 422. No hay vueltas.
- **PATCH:** Mandás solo lo que querés cambiar. No hace falta que repitas todo el objeto. Por ejemplo, si solo querés cambiar el precio, mandás `{"price": 10.99}` y listo.
- **GET y DELETE:** No llevan body. Todo va en la URL. Si igual le metés algo en el body, el servidor lo ignora. Perdés el tiempo.

## Ojo con estos detalles

- **El header no se te olvide:** Cada vez que uses POST o PATCH, poné `Content-Type: application/json` en la pestaña de Headers. Si no, la API no entiende el JSON y te da error.
- **Las URLs sin barra al final:** Usá `.../products` y no `.../products/`. FastAPI se pone delicado con eso y a veces te redirige y pierde el body. Un clásico.
- **Errores que vas a ver seguido:**
  - `404`: El ID que pusiste no existe.
  - `422`: Mandaste mal el JSON. Revisá nombres de campos y tipos de datos.
  - `405`: Usaste el método equivocado (ej. intentaste crear con GET).

Con eso ya podés probar todo. Cualquier cosa, mirá el `/docs` que FastAPI te genera solo y te muestra los ejemplos.
### DOCS/SWAGGER Y REDOC
```
http://127.0.0.1:8000/docs#/
```
```
http://127.0.0.1:8000/redoc#/
```
### PRODUCTOS
### CATEGORIAS
