# Registro de Defectos – API de Productos y Categorías

## 1. Objetivo

Registrar los defectos identificados durante la ejecución de las pruebas, incluyendo su trazabilidad, evidencia, corrección, retest y resultado de la regresión.

---

# 2. Defectos identificados

## DEF-001 – Código HTTP incorrecto al consultar una categoría inexistente

**Requisito:** RF04
**Caso relacionado:** CP-CAT-04
**Endpoint:** `GET /categories/{category_id}`
**Severidad:** Alta
**Prioridad:** Alta
**Estado:** Cerrado

### Descripción

Durante una ejecución controlada se modificó temporalmente el comportamiento del endpoint de consulta de categorías para devolver HTTP 202 cuando la categoría solicitada no existía.

El contrato establece que una categoría inexistente debe generar HTTP 404.

### Precondiciones

* La aplicación estaba disponible.
* No existía una categoría con ID `99999`.

### Pasos para reproducir

1. Enviar una solicitud GET a `/categories/99999`.
2. Verificar el código HTTP recibido.
3. Compararlo con el código definido en el contrato.

### Resultado esperado

```text
HTTP 404
```

con el detalle:

```json
{
  "detail": "Category not found"
}
```

### Resultado obtenido durante la ejecución controlada

```text
HTTP 202
```

El resultado no cumplía el contrato.

### Evidencia

Ejecución automatizada del caso:

```text
test_get_non_existing_category
```

Resultado durante la ejecución controlada:

```text
FAILED
Expected: 404
Obtained: 202
```

Además, el comportamiento incorrecto afectó una segunda prueba relacionada con la eliminación de una categoría y su posterior consulta.

### Corrección

Se restauró el comportamiento correcto del endpoint para que una categoría inexistente genere:

```text
HTTP 404
```

con el mensaje:

```text
Category not found
```

### Retest

Se ejecutó nuevamente específicamente el caso:

```text
tests/test_categories.py::test_get_non_existing_category
```

Resultado:

```text
PASSED
```

### Regresión

Después de la corrección se ejecutó nuevamente la suite completa.

Resultado final:

```text
25 passed
0 failed
0 blocked
```

### Criterio de cierre

El defecto se considera cerrado porque:

* El comportamiento esperado fue restaurado.
* El caso que detectó el defecto pasó correctamente.
* La suite completa pasó después de la corrección.
* No se identificaron regresiones funcionales.

---

# 3. Resumen de defectos

| ID      | Descripción                                                                     | Severidad | Prioridad | Estado  |
| ------- | ------------------------------------------------------------------------------- | --------- | --------- | ------- |
| DEF-001 | Categoría inexistente devolvía 202 en lugar de 404 durante ejecución controlada | Alta      | Alta      | Cerrado |

**Defectos críticos abiertos:** 0

**Defectos abiertos:** 0

**Defectos cerrados:** 1

---

# 4. Retest

El retest se realizó sobre el caso que detectó el defecto.

| Defecto | Caso      | Resultado inicial | Resultado después de corrección |
| ------- | --------- | ----------------- | ------------------------------- |
| DEF-001 | CP-CAT-04 | FAILED – 202      | PASSED – 404                    |

El retest confirmó que la corrección solucionó el comportamiento observado.

---

# 5. Prueba de regresión

Después del retest se ejecutó nuevamente la totalidad de los casos automatizados.

Resultado:

| Resultado | Cantidad |
| --------- | -------: |
| PASSED    |       25 |
| FAILED    |        0 |
| BLOCKED   |        0 |
| Total     |       25 |

**Porcentaje de aprobación: 100 %.**

La regresión no evidenció nuevos fallos funcionales.

---

# 6. Estado final

Al finalizar la evaluación:

* No existen defectos críticos abiertos.
* No existen defectos abiertos.
* El defecto DEF-001 fue corregido.
* El retest fue satisfactorio.
* La regresión completa fue satisfactoria.
* La suite automatizada alcanzó 25/25 casos aprobados.
