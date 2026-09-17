# Casos de Prueba – API de Productos y Categorías

## 1. Información general

**Proyecto:** API REST de Productos y Categorías
**Versión:** 1.0.0
**Total de casos:** 25
**Casos de categorías:** 7
**Casos de productos:** 18
**Casos automatizados:** 25

### Convención de estados

* **PASSED:** El resultado obtenido coincide con el esperado.
* **FAILED:** El resultado obtenido no coincide con el esperado.
* **BLOCKED:** No fue posible ejecutar el caso.
* **NOT EXECUTED:** Caso diseñado pero aún no ejecutado.

---

# 2. Casos de prueba de Categorías

## CP-CAT-01 – Crear categoría válida

**Requisito:** RF01
**Reglas:** RN01
**Prioridad:** Alta
**Tipo:** Positiva

**Precondiciones:**

* La API está disponible.
* No existe una categoría llamada `Periféricos`.

**Datos:**

```json
{
  "name": "Periféricos",
  "description": "Dispositivos periféricos",
  "active": true
}
```

**Pasos:**

1. Enviar POST a `/categories`.
2. Incluir el JSON indicado.
3. Verificar el código HTTP.
4. Verificar los datos de la respuesta.

**Resultado esperado:**

* HTTP 201.
* Se crea la categoría.
* La respuesta contiene `id`, `name`, `description` y `active`.

**Resultado obtenido:** HTTP 201 y categoría creada correctamente.

**Estado:** PASSED

---

## CP-CAT-02 – Listar categorías

**Requisito:** RF02
**Prioridad:** Media
**Tipo:** Positiva

**Precondiciones:**

* La API está disponible.
* Existen categorías.

**Datos:** No aplica.

**Pasos:**

1. Enviar GET a `/categories`.
2. Verificar el código HTTP.
3. Verificar que la respuesta sea una lista.

**Resultado esperado:**

* HTTP 200.
* La respuesta contiene una lista de categorías.

**Resultado obtenido:** HTTP 200 y lista recibida correctamente.

**Estado:** PASSED

---

## CP-CAT-03 – Consultar categoría existente

**Requisito:** RF03
**Prioridad:** Alta
**Tipo:** Positiva

**Precondiciones:**

* Existe la categoría con ID 1.

**Datos:**

```text
category_id = 1
```

**Pasos:**

1. Enviar GET a `/categories/1`.
2. Verificar el código HTTP.
3. Verificar que el ID sea 1.

**Resultado esperado:**

* HTTP 200.
* Se devuelve la categoría con ID 1.

**Resultado obtenido:** HTTP 200 y categoría encontrada.

**Estado:** PASSED

---

## CP-CAT-04 – Consultar categoría inexistente

**Requisito:** RF04
**Prioridad:** Alta
**Tipo:** Negativa

**Precondiciones:**

* No existe la categoría con ID 99999.

**Datos:**

```text
category_id = 99999
```

**Pasos:**

1. Enviar GET a `/categories/99999`.
2. Verificar el código HTTP.
3. Verificar el mensaje de error.

**Resultado esperado:**

* HTTP 404.
* Detalle: `Category not found`.

**Resultado obtenido:** HTTP 404 y mensaje esperado.

**Estado:** PASSED

---

## CP-CAT-05 – Nombre de categoría menor a 3 caracteres

**Requisito:** RN01
**Prioridad:** Alta
**Tipo:** Negativa / Frontera

**Precondiciones:**

* La API está disponible.

**Datos:**

```json
{
  "name": "AB"
}
```

**Pasos:**

1. Enviar POST a `/categories`.
2. Utilizar un nombre de 2 caracteres.
3. Verificar el código HTTP.

**Resultado esperado:**

* HTTP 422.
* La categoría no debe crearse.

**Resultado obtenido:** HTTP 422.

**Estado:** PASSED

---

## CP-CAT-06 – Nombre de categoría exactamente de 3 caracteres

**Requisito:** RN01
**Prioridad:** Alta
**Tipo:** Positiva / Frontera

**Precondiciones:**

* No existe una categoría llamada `PCs`.

**Datos:**

```json
{
  "name": "PCs"
}
```

**Pasos:**

1. Enviar POST a `/categories`.
2. Utilizar un nombre de exactamente 3 caracteres.
3. Verificar el código HTTP.

**Resultado esperado:**

* HTTP 201.
* La categoría debe crearse correctamente.

**Resultado obtenido:** HTTP 201.

**Estado:** PASSED

---

## CP-CAT-07 – Nombre de categoría duplicado sin distinguir mayúsculas/minúsculas

**Requisito:** RN02
**Prioridad:** Alta
**Tipo:** Negativa

**Precondiciones:**

* Existe una categoría con nombre `Laptops`.

**Datos:**

```json
{
  "name": "LAPTOPS"
}
```

**Pasos:**

1. Consultar una categoría existente.
2. Obtener su nombre.
3. Convertir el nombre a mayúsculas.
4. Enviar POST a `/categories`.
5. Verificar el código HTTP.

**Resultado esperado:**

* HTTP 409.
* No debe crearse una categoría duplicada.

**Resultado obtenido:** HTTP 409.

**Estado:** PASSED

---

# 3. Casos de prueba de Productos

## CP-PROD-01 – Crear producto válido

**Requisito:** RF05
**Reglas:** RN03, RN04, RN05, RN06
**Prioridad:** Alta
**Tipo:** Positiva

**Precondiciones:**

* Existe la categoría con ID 1.

**Datos:**

```json
{
  "name": "Teclado mecánico",
  "price": 250000,
  "stock": 10,
  "category_id": 1
}
```

**Pasos:**

1. Enviar POST a `/products`.
2. Incluir los datos válidos.
3. Verificar el código HTTP.
4. Verificar los datos retornados.

**Resultado esperado:**

* HTTP 201.
* El producto se crea correctamente.
* Se devuelve un ID.
* `category_id` corresponde a la categoría existente.

**Resultado obtenido:** HTTP 201 y producto creado.

**Estado:** PASSED

---

## CP-PROD-02 – Listar productos

**Requisito:** RF06
**Prioridad:** Media
**Tipo:** Positiva

**Precondiciones:**

* Existen productos.

**Datos:** No aplica.

**Pasos:**

1. Enviar GET a `/products/`.
2. Verificar el código HTTP.
3. Verificar que la respuesta sea una lista.

**Resultado esperado:**

* HTTP 200.
* Se devuelve una lista de productos.

**Resultado obtenido:** HTTP 200 y lista recibida correctamente.

**Estado:** PASSED

---

## CP-PROD-03 – Consultar producto existente

**Requisito:** RF07
**Prioridad:** Alta
**Tipo:** Positiva

**Precondiciones:**

* Existe el producto con ID 1.

**Datos:**

```text
product_id = 1
```

**Pasos:**

1. Enviar GET a `/products/1`.
2. Verificar el código HTTP.
3. Verificar el ID retornado.

**Resultado esperado:**

* HTTP 200.
* Se devuelve el producto con ID 1.

**Resultado obtenido:** HTTP 200 y producto encontrado.

**Estado:** PASSED

---

## CP-PROD-04 – Consultar producto inexistente

**Requisito:** RF08
**Prioridad:** Alta
**Tipo:** Negativa

**Precondiciones:**

* No existe el producto con ID 99999.

**Datos:**

```text
product_id = 99999
```

**Pasos:**

1. Enviar GET a `/products/99999`.
2. Verificar el código HTTP.
3. Verificar el mensaje.

**Resultado esperado:**

* HTTP 404.
* Detalle: `Product not found`.

**Resultado obtenido:** HTTP 404 y mensaje esperado.

**Estado:** PASSED

---

## CP-PROD-05 – Actualizar producto existente

**Requisito:** RF09
**Regla:** RN08
**Prioridad:** Alta
**Tipo:** Positiva

**Precondiciones:**

* Existe el producto con ID 1.

**Datos:**

```json
{
  "price": 99999
}
```

**Pasos:**

1. Enviar PUT a `/products/1`.
2. Modificar el precio.
3. Verificar el código HTTP.
4. Verificar el precio retornado.

**Resultado esperado:**

* HTTP 200.
* El precio se actualiza a 99999.

**Resultado obtenido:** HTTP 200 y precio actualizado.

**Estado:** PASSED

---

## CP-PROD-06 – Actualizar producto inexistente

**Requisito:** RF10
**Prioridad:** Alta
**Tipo:** Negativa

**Precondiciones:**

* No existe el producto con ID 99999.

**Datos:**

```json
{
  "price": 99999
}
```

**Pasos:**

1. Enviar PUT a `/products/99999`.
2. Verificar el código HTTP.

**Resultado esperado:**

* HTTP 404.
* El producto no debe crearse.

**Resultado obtenido:** HTTP 404.

**Estado:** PASSED

---

## CP-PROD-07 – Eliminar producto existente

**Requisito:** RF11
**Prioridad:** Alta
**Tipo:** Positiva

**Precondiciones:**

* Existe un producto válido para eliminar.

**Datos:**
Se crea previamente un producto mediante POST.

**Pasos:**

1. Crear un producto válido.
2. Obtener su ID.
3. Enviar DELETE al ID obtenido.
4. Verificar el código HTTP.
5. Consultar nuevamente el producto.

**Resultado esperado:**

* DELETE devuelve HTTP 204.
* El producto queda eliminado.
* Una consulta posterior devuelve HTTP 404.

**Resultado obtenido:** HTTP 204 y consulta posterior HTTP 404.

**Estado:** PASSED

---

## CP-PROD-08 – Eliminar producto inexistente

**Requisito:** RF12
**Prioridad:** Alta
**Tipo:** Negativa

**Precondiciones:**

* No existe el producto con ID 99999.

**Datos:**

```text
product_id = 99999
```

**Pasos:**

1. Enviar DELETE a `/products/99999`.
2. Verificar el código HTTP.

**Resultado esperado:**

* HTTP 404.

**Resultado obtenido:** HTTP 404.

**Estado:** PASSED

---

## CP-PROD-09 – Nombre de producto menor a 3 caracteres

**Requisito:** RN03
**Prioridad:** Alta
**Tipo:** Negativa / Frontera

**Datos:**

```json
{
  "name": "AB",
  "price": 10000,
  "stock": 5,
  "category_id": 1
}
```

**Pasos:**

1. Enviar POST a `/products`.
2. Utilizar un nombre de 2 caracteres.
3. Verificar la respuesta.

**Resultado esperado:**

* HTTP 422.

**Resultado obtenido:** HTTP 422.

**Estado:** PASSED

---

## CP-PROD-10 – Nombre de producto exactamente de 3 caracteres

**Requisito:** RN03
**Prioridad:** Alta
**Tipo:** Positiva / Frontera

**Datos:**

```json
{
  "name": "PC1",
  "price": 10000,
  "stock": 5,
  "category_id": 1
}
```

**Pasos:**

1. Enviar POST a `/products`.
2. Utilizar un nombre de exactamente 3 caracteres.
3. Verificar la respuesta.

**Resultado esperado:**

* HTTP 201.
* El producto se crea correctamente.

**Resultado obtenido:** HTTP 201.

**Estado:** PASSED

---

## CP-PROD-11 – Precio igual a cero

**Requisito:** RN04
**Prioridad:** Alta
**Tipo:** Negativa / Frontera

**Datos:**

```json
{
  "name": "Producto precio cero",
  "price": 0,
  "stock": 5,
  "category_id": 1
}
```

**Pasos:**

1. Enviar POST a `/products`.
2. Utilizar precio 0.
3. Verificar la respuesta.

**Resultado esperado:**

* HTTP 422.
* El producto no debe crearse.

**Resultado obtenido:** HTTP 422.

**Estado:** PASSED

---

## CP-PROD-12 – Precio negativo

**Requisito:** RN04
**Prioridad:** Alta
**Tipo:** Negativa

**Datos:**

```json
{
  "name": "Producto precio negativo",
  "price": -1000,
  "stock": 5,
  "category_id": 1
}
```

**Pasos:**

1. Enviar POST a `/products`.
2. Utilizar precio negativo.
3. Verificar la respuesta.

**Resultado esperado:**

* HTTP 422.

**Resultado obtenido:** HTTP 422.

**Estado:** PASSED

---

## CP-PROD-13 – Precio mínimo positivo

**Requisito:** RN04
**Prioridad:** Alta
**Tipo:** Positiva / Frontera

**Datos:**

```json
{
  "name": "Producto mínimo",
  "price": 0.01,
  "stock": 5,
  "category_id": 1
}
```

**Pasos:**

1. Enviar POST a `/products`.
2. Utilizar precio 0.01.
3. Verificar la respuesta.

**Resultado esperado:**

* HTTP 201.
* El producto se crea correctamente.

**Resultado obtenido:** HTTP 201.

**Estado:** PASSED

---

## CP-PROD-14 – Stock igual a cero

**Requisito:** RN05, RN07
**Prioridad:** Alta
**Tipo:** Positiva / Frontera

**Datos:**

```json
{
  "name": "Monitor sin stock",
  "price": 850000,
  "stock": 0,
  "category_id": 1
}
```

**Pasos:**

1. Enviar POST a `/products`.
2. Utilizar stock 0.
3. Verificar la respuesta.
4. Verificar el stock retornado.

**Resultado esperado:**

* HTTP 201.
* El producto se crea.
* El stock es 0.

**Resultado obtenido:** HTTP 201 y stock 0 aceptado.

**Estado:** PASSED

---

## CP-PROD-15 – Stock negativo

**Requisito:** RN05
**Prioridad:** Alta
**Tipo:** Negativa

**Datos:**

```json
{
  "name": "Producto stock negativo",
  "price": 10000,
  "stock": -1,
  "category_id": 1
}
```

**Pasos:**

1. Enviar POST a `/products`.
2. Utilizar stock -1.
3. Verificar la respuesta.

**Resultado esperado:**

* HTTP 422.
* El producto no debe crearse.

**Resultado obtenido:** HTTP 422.

**Estado:** PASSED

---

## CP-PROD-16 – Categoría inexistente al crear producto

**Requisito:** RF05
**Regla:** RN06
**Prioridad:** Alta
**Tipo:** Negativa

**Datos:**

```json
{
  "name": "Producto categoría inexistente",
  "price": 10000,
  "stock": 5,
  "category_id": 99999
}
```

**Pasos:**

1. Enviar POST a `/products`.
2. Utilizar `category_id` 99999.
3. Verificar la respuesta.

**Resultado esperado:**

* HTTP 404.
* Detalle: `Category not found`.
* El producto no debe crearse.

**Resultado obtenido:** HTTP 404.

**Estado:** PASSED

---

## CP-PROD-17 – Precio inválido durante actualización

**Requisito:** RF09
**Regla:** RN08
**Prioridad:** Alta
**Tipo:** Negativa / Frontera

**Precondiciones:**

* Existe el producto con ID 1.

**Datos:**

```json
{
  "price": 0
}
```

**Pasos:**

1. Enviar PUT a `/products/1`.
2. Utilizar precio 0.
3. Verificar la respuesta.

**Resultado esperado:**

* HTTP 422.
* El precio inválido no debe aceptarse.

**Resultado obtenido:** HTTP 422.

**Estado:** PASSED

---

## CP-PROD-18 – Categoría inexistente durante actualización

**Requisito:** RF09
**Reglas:** RN06, RN08
**Prioridad:** Alta
**Tipo:** Negativa

**Precondiciones:**

* Existe el producto con ID 1.
* No existe la categoría con ID 99999.

**Datos:**

```json
{
  "category_id": 99999
}
```

**Pasos:**

1. Enviar PUT a `/products/1`.
2. Utilizar `category_id` 99999.
3. Verificar la respuesta.

**Resultado esperado:**

* HTTP 404.
* Detalle: `Category not found`.
* La categoría inválida no debe asignarse.

**Resultado obtenido:** HTTP 404.

**Estado:** PASSED

---

# 4. Resumen de ejecución

| Categoría  | Diseñados | Ejecutados | PASSED | FAILED | BLOCKED |
| ---------- | --------: | ---------: | -----: | -----: | ------: |
| Categorías |         7 |          7 |      7 |      0 |       0 |
| Productos  |        18 |         18 |     18 |      0 |       0 |
| **Total**  |    **25** |     **25** | **25** |  **0** |   **0** |

**Porcentaje de aprobación: 100 %.**

---

# 5. Cobertura por tipo de prueba

| Tipo      | Casos                                                                                                                                                   |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positivos | CP-CAT-01, CP-CAT-02, CP-CAT-03, CP-CAT-06, CP-PROD-01, CP-PROD-02, CP-PROD-03, CP-PROD-05, CP-PROD-07, CP-PROD-10, CP-PROD-13, CP-PROD-14              |
| Negativos | CP-CAT-04, CP-CAT-05, CP-CAT-07, CP-PROD-04, CP-PROD-06, CP-PROD-08, CP-PROD-09, CP-PROD-11, CP-PROD-12, CP-PROD-15, CP-PROD-16, CP-PROD-17, CP-PROD-18 |
| Frontera  | CP-CAT-05, CP-CAT-06, CP-PROD-09, CP-PROD-10, CP-PROD-11, CP-PROD-13, CP-PROD-14, CP-PROD-17                                                            |
