# Informe de Ejecución de Pruebas – API de Productos y Categorías

## 1. Información general

**Proyecto:** API REST de Productos y Categorías
**Versión evaluada:** 1.0.0
**Fecha de ejecución:** Septiembre de 2026
**Sistema operativo:** Windows
**Python:** 3.14.6
**FastAPI:** 0.141.1
**Starlette:** 1.6.0
**pytest:** 9.1.1
**Cliente HTTP:** FastAPI TestClient

---

## 2. Objetivo

Presentar los resultados de la ejecución de las pruebas funcionales y automatizadas realizadas sobre la API de Productos y Categorías.

El informe consolida:

* Casos diseñados.
* Casos ejecutados.
* Resultados obtenidos.
* Defectos identificados.
* Retest.
* Regresión.
* Cobertura de requisitos.
* Cumplimiento de los criterios de salida.

---

## 3. Resumen de ejecución

La suite automatizada contiene **25 casos de prueba**:

* 7 casos de categorías.
* 18 casos de productos.

### Resultado final

| Resultado    | Cantidad |
| ------------ | -------: |
| PASSED       |       25 |
| FAILED       |        0 |
| BLOCKED      |        0 |
| NOT EXECUTED |        0 |
| **TOTAL**    |   **25** |

### Porcentaje de aprobación

**25 / 25 = 100 %**

**Resultado final: 100 % de los casos ejecutados fueron aprobados.**

---

## 4. Distribución de casos

| Módulo     | Diseñados | Ejecutados | PASSED | FAILED |
| ---------- | --------: | ---------: | -----: | -----: |
| Categorías |         7 |          7 |      7 |      0 |
| Productos  |        18 |         18 |     18 |      0 |
| **Total**  |    **25** |     **25** | **25** |  **0** |

---

## 5. Cobertura de requisitos

### Requisitos funcionales

Se verificaron todos los requisitos funcionales RF01–RF12.

**Cobertura: 12/12 = 100 %.**

| Requisito | Cobertura |
| --------- | --------- |
| RF01      | Cubierto  |
| RF02      | Cubierto  |
| RF03      | Cubierto  |
| RF04      | Cubierto  |
| RF05      | Cubierto  |
| RF06      | Cubierto  |
| RF07      | Cubierto  |
| RF08      | Cubierto  |
| RF09      | Cubierto  |
| RF10      | Cubierto  |
| RF11      | Cubierto  |
| RF12      | Cubierto  |

### Reglas de negocio

Se verificaron todas las reglas RN01–RN08.

**Cobertura: 8/8 = 100 %.**

| Regla | Cobertura |
| ----- | --------- |
| RN01  | Cubierta  |
| RN02  | Cubierta  |
| RN03  | Cubierta  |
| RN04  | Cubierta  |
| RN05  | Cubierta  |
| RN06  | Cubierta  |
| RN07  | Cubierta  |
| RN08  | Cubierta  |

---

## 6. Tipos de pruebas ejecutadas

La suite incluye:

### Pruebas positivas

Se verificó el funcionamiento esperado utilizando datos válidos.

Entre ellas:

* Creación de categorías.
* Listado de categorías.
* Consulta de categorías.
* Creación de productos.
* Listado de productos.
* Consulta de productos.
* Actualización de productos.
* Eliminación de productos.

### Pruebas negativas

Se verificó el comportamiento ante datos inválidos y recursos inexistentes.

Se incluyeron:

* Categoría inexistente.
* Producto inexistente.
* Nombre inválido.
* Categoría duplicada.
* Precio cero.
* Precio negativo.
* Stock negativo.
* Categoría inexistente al crear un producto.
* Precio inválido al actualizar.
* Categoría inexistente al actualizar.

### Pruebas de frontera

Se verificaron límites relevantes:

* Nombre de categoría menor a 3 caracteres.
* Nombre de categoría exactamente de 3 caracteres.
* Nombre de producto menor a 3 caracteres.
* Nombre de producto exactamente de 3 caracteres.
* Precio igual a cero.
* Precio mínimo positivo.
* Stock igual a cero.

---

## 7. Defectos

Durante la evaluación se registró un defecto controlado:

**DEF-001 – Código HTTP incorrecto al consultar una categoría inexistente.**

Durante una ejecución controlada, el endpoint devolvió HTTP 202 cuando el contrato establecía HTTP 404.

El defecto fue corregido y posteriormente sometido a retest.

### Estado final

| Severidad | Abiertos | Cerrados |
| --------- | -------: | -------: |
| Crítica   |        0 |        0 |
| Alta      |        0 |        1 |
| Media     |        0 |        0 |
| Baja      |        0 |        0 |

**Defectos críticos abiertos: 0.**

**Defectos abiertos: 0.**

---

## 8. Retest

Después de corregir DEF-001 se volvió a ejecutar el caso:

`CP-CAT-04 – Consultar categoría inexistente`

Resultado:

**PASSED**

El endpoint volvió a responder HTTP 404, conforme al contrato.

---

## 9. Regresión

Después del retest se ejecutó nuevamente la suite completa de pruebas automatizadas.

Resultado:

```text
25 passed
0 failed
0 blocked
```

Porcentaje de aprobación:

**100 %.**

La regresión no presentó nuevos fallos funcionales.

---

## 10. Warning técnico

Durante la ejecución se presentó un warning de deprecación relacionado con:

`anyio.abc.BlockingPortal`

El warning proviene de la interacción entre las versiones utilizadas de Starlette/AnyIO y no produjo fallos en los casos de prueba.

Resultado:

* No afecta el resultado funcional de la suite.
* No generó casos FAILED.
* Se mantiene registrado como observación técnica para futuras actualizaciones de dependencias.

---

## 11. Criterios de salida

| Criterio                        | Resultado        |
| ------------------------------- | ---------------- |
| Cobertura RF01–RF12             | Cumplido – 100 % |
| Cobertura RN01–RN08             | Cumplido – 100 % |
| Mínimo 15 casos automatizados   | Cumplido – 25    |
| Ejecución de casos críticos     | Cumplido         |
| Aprobación mínima del 90 %      | Cumplido – 100 % |
| Cero defectos críticos abiertos | Cumplido         |
| Defectos trazados               | Cumplido         |
| Retest realizado                | Cumplido         |
| Regresión realizada             | Cumplido         |

---

## 12. Conclusión técnica

La ejecución final de la suite automatizada obtuvo **25 casos aprobados de 25 ejecutados**, equivalente a un **100 % de aprobación**.

La cobertura documental alcanza el 100 % de los requisitos funcionales RF01–RF12 y de las reglas de negocio RN01–RN08.

Las pruebas incluyen escenarios positivos, negativos y de frontera, además de validaciones de recursos inexistentes, actualización, eliminación y asociación de productos con categorías.

El defecto controlado DEF-001 fue identificado, corregido y validado mediante retest. Posteriormente, la ejecución de regresión completa confirmó que los cambios no introdujeron nuevos fallos funcionales.

No existen defectos críticos ni defectos abiertos al finalizar la ejecución.

---

## 13. Riesgos pendientes

Aunque los criterios de salida fueron cumplidos, permanecen como riesgos fuera del alcance de esta evaluación:

* Ausencia de pruebas de carga y rendimiento.
* Ausencia de pruebas de seguridad avanzada.
* Ausencia de una base de datos persistente.
* Warning de deprecación relacionado con Starlette/AnyIO.
* No se realizaron pruebas de despliegue en producción.

Estos puntos pueden ser considerados en futuras iteraciones del proyecto.

---

## 14. Evidencia final

La evidencia principal de la ejecución final corresponde a la ejecución de pytest desde la raíz del proyecto.

Resultado:

```text
25 passed, 1 warning
```

Este resultado constituye la evidencia de la ejecución final de los 25 casos automatizados.
