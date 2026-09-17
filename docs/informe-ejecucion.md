# Informe de Ejecución de Pruebas

## 1. Información general

| Campo                  | Valor                         |
| ---------------------- | ----------------------------- |
| Proyecto               | API de Productos y Categorías |
| Responsable            | Julian Quiroga                |
| Ambiente               | Entorno local                 |
| Framework              | FastAPI                       |
| Herramienta de pruebas | pytest                        |
| Cliente de pruebas     | FastAPI TestClient            |
| Fecha                  | 17/09/2026                    |

---

## 2. Objetivo

Presentar los resultados obtenidos durante la ejecución de las pruebas automatizadas de la API de Productos y Categorías, incluyendo la detección, corrección, retest y regresión de un defecto controlado.

---

## 3. Resumen de ejecución

La suite automatizada está conformada por **23 casos de prueba**.

### Ejecución inicial con defecto controlado

Durante la ejecución controlada se obtuvieron:

| Resultado  | Cantidad |
| ---------- | -------: |
| Aprobadas  |       21 |
| Fallidas   |        2 |
| Bloqueadas |        0 |
| Total      |       23 |

Porcentaje inicial de aprobación:

**21 / 23 × 100 = 91,30 %**

Los casos afectados fueron:

* `test_get_non_existing_category`
* `test_delete_existing_category`

El primer fallo permitió identificar directamente el defecto controlado DEF-001: la consulta de una categoría inexistente retornaba HTTP 202 en lugar de HTTP 404.

El segundo fallo se produjo como consecuencia del mismo defecto, ya que después de eliminar una categoría, la consulta posterior también debía retornar HTTP 404.

---

## 4. Defecto identificado

### DEF-001

**Descripción:** código HTTP incorrecto al consultar una categoría inexistente.

**Resultado esperado:**

```text
404 Not Found
```

**Resultado obtenido durante la ejecución controlada:**

```text
202 Accepted
```

**Componente afectado:**

```text
app/main.py
```

**Función:**

```text
get_category_by_id()
```

El defecto fue introducido temporalmente de forma controlada con fines académicos para demostrar el proceso de gestión de defectos. No corresponde a un defecto descubierto en un ambiente de producción.

---

## 5. Corrección

Se corrigió el código de la función `get_category_by_id()` para retornar nuevamente HTTP 404 cuando la categoría solicitada no existe.

Código corregido:

```python
if category is None:
    raise HTTPException(status_code=404, detail="Category not found")
```

---

## 6. Retest

Después de realizar la corrección se ejecutó nuevamente el caso afectado:

```text
pytest -v tests/test_categories.py::test_get_non_existing_category
```

Resultado:

```text
1 passed, 1 warning
```

El caso de prueba quedó aprobado después de la corrección.

---

## 7. Regresión

Después del retest se ejecutó nuevamente la suite completa:

```text
pytest -v
```

Resultado final:

```text
23 passed, 1 warning
```

### Resultado final

| Resultado  | Cantidad |
| ---------- | -------: |
| Aprobadas  |       23 |
| Fallidas   |        0 |
| Bloqueadas |        0 |
| Total      |       23 |

### Porcentaje de aprobación

**23 / 23 × 100 = 100 %**

La corrección aplicada no generó regresiones en las demás funcionalidades probadas.

---

## 8. Cobertura de pruebas

Las pruebas automatizadas cubren funcionalidades relacionadas con:

### Productos

* Consulta de productos.
* Consulta de producto por ID.
* Creación de productos.
* Actualización parcial.
* Eliminación.
* Consulta de productos inexistentes.
* Validaciones de datos.
* Filtros.
* Health check.

### Categorías

* Consulta de categorías.
* Consulta de categoría por ID.
* Consulta de categoría inexistente.
* Creación.
* Validación de datos.
* Actualización parcial.
* Eliminación.
* Filtro por estado activo.
* Búsqueda por nombre.

---

## 9. Criterios de salida

Los principales criterios de salida definidos para la ejecución fueron:

| Criterio                           | Resultado       |
| ---------------------------------- | --------------- |
| Ejecución de pruebas automatizadas | Cumplido        |
| Casos críticos aprobados           | Cumplido        |
| Defecto identificado y documentado | Cumplido        |
| Corrección aplicada                | Cumplido        |
| Retest ejecutado                   | Cumplido        |
| Regresión ejecutada                | Cumplido        |
| Pruebas finales sin fallos         | Cumplido        |
| Tasa final de aprobación ≥ 95 %    | Cumplido: 100 % |

---

## 10. Advertencias del entorno

En las ejecuciones se presentó un `DeprecationWarning` relacionado con:

```text
anyio.abc.BlockingPortal
```

El warning se genera desde una dependencia utilizada por `starlette.testclient`.

No produjo fallos en las pruebas y no afecta el resultado funcional de la API.

---

## 11. Conclusión técnica

La ejecución final de la suite automatizada obtuvo **23 casos aprobados de 23 ejecutados**, equivalente a una tasa de aprobación del **100 %**.

El defecto controlado DEF-001 fue reproducido, documentado, corregido y sometido a retest. Posteriormente se ejecutó la regresión completa y no se presentaron nuevos fallos.

Por lo tanto, con respecto al alcance de las pruebas realizadas, los criterios de salida definidos fueron cumplidos.
