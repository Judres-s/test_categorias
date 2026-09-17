# Plan de Pruebas – API de Productos y Categorías

## 1. Información general

**Proyecto:** API REST de Productos y Categorías
**Versión evaluada:** 1.0.0
**Tecnología:** FastAPI
**Lenguaje:** Python
**Framework de pruebas:** pytest
**Cliente de pruebas:** FastAPI TestClient
**Tipo de almacenamiento:** Datos en memoria mediante listas Python

---

## 2. Objetivo

Verificar mediante pruebas funcionales y automatizadas que la API de Productos y Categorías cumple con los requisitos funcionales, reglas de negocio, validaciones y códigos HTTP definidos para el Mini Proyecto Evaluable.

El objetivo incluye validar:

* Creación, consulta, actualización y eliminación de recursos.
* Validaciones de datos de entrada.
* Manejo de recursos inexistentes.
* Asociación de productos con categorías existentes.
* Unicidad de nombres de categorías.
* Valores límite de nombres, precios y stock.
* Códigos HTTP esperados.
* Comportamiento de la API después de una modificación.

---

## 3. Alcance

### 3.1 Categorías

Se verifican los siguientes endpoints:

| ID   | Método | Endpoint                       | Respuesta esperada |
| ---- | ------ | ------------------------------ | ------------------ |
| EP01 | POST   | `/categories`                  | 201                |
| EP02 | GET    | `/categories`                  | 200                |
| EP03 | GET    | `/categories/{id}`             | 200                |
| EP04 | GET    | `/categories/{id}` inexistente | 404                |

También se validan:

* Nombre obligatorio.
* Longitud mínima de 3 caracteres.
* Longitud máxima de 60 caracteres.
* Unicidad del nombre sin distinguir mayúsculas y minúsculas.
* Código 422 para datos inválidos.
* Código 409 para nombres duplicados.

### 3.2 Productos

Se verifican los siguientes endpoints:

| ID   | Método | Endpoint         | Respuesta esperada |
| ---- | ------ | ---------------- | ------------------ |
| EP04 | POST   | `/products`      | 201                |
| EP05 | GET    | `/products`      | 200                |
| EP06 | GET    | `/products/{id}` | 200                |
| EP07 | PUT    | `/products/{id}` | 200                |
| EP08 | DELETE | `/products/{id}` | 204                |

También se validan:

* Nombre obligatorio entre 3 y 80 caracteres.
* Precio estrictamente mayor que 0.
* Stock mayor o igual a 0.
* Stock igual a 0 permitido.
* Existencia de la categoría asociada.
* Manejo de productos inexistentes.
* Validaciones durante la actualización.

---

## 4. Fuera de alcance

No se incluyen en esta evaluación:

* Pruebas de rendimiento o carga.
* Pruebas de seguridad avanzada.
* Pruebas de integración con bases de datos externas.
* Pruebas de autenticación o autorización.
* Pruebas de despliegue en producción.
* Pruebas de interfaz gráfica.
* Persistencia de información después de reiniciar la aplicación.

---

## 5. Inventario de requisitos funcionales

| ID   | Requisito                                            |
| ---- | ---------------------------------------------------- |
| RF01 | Crear una categoría válida                           |
| RF02 | Listar categorías                                    |
| RF03 | Consultar una categoría existente                    |
| RF04 | Devolver 404 para una categoría inexistente          |
| RF05 | Crear un producto asociado a una categoría existente |
| RF06 | Listar productos                                     |
| RF07 | Consultar un producto existente                      |
| RF08 | Devolver 404 para un producto inexistente            |
| RF09 | Actualizar un producto existente                     |
| RF10 | Devolver 404 al actualizar un producto inexistente   |
| RF11 | Eliminar un producto existente                       |
| RF12 | Devolver 404 al eliminar un producto inexistente     |

---

## 6. Reglas de negocio y validación

| ID   | Regla                                                                        |
| ---- | ---------------------------------------------------------------------------- |
| RN01 | El nombre de categoría es obligatorio y debe tener entre 3 y 60 caracteres   |
| RN02 | El nombre de categoría debe ser único sin distinguir mayúsculas y minúsculas |
| RN03 | El nombre de producto es obligatorio y debe tener entre 3 y 80 caracteres    |
| RN04 | El precio del producto debe ser estrictamente mayor que 0                    |
| RN05 | El stock debe ser mayor o igual que 0                                        |
| RN06 | `category_id` debe corresponder a una categoría existente                    |
| RN07 | Un producto puede tener stock igual a 0                                      |
| RN08 | La actualización de productos conserva las validaciones de creación          |

---

## 7. Análisis de riesgos

| Riesgo                                    | Probabilidad | Impacto | Prioridad | Casos relacionados                 |
| ----------------------------------------- | ------------ | ------- | --------- | ---------------------------------- |
| Creación de categorías duplicadas         | Media        | Alta    | Alta      | CP-CAT-07                          |
| Nombre de categoría demasiado corto       | Alta         | Media   | Alta      | CP-CAT-05                          |
| Consulta de categoría inexistente         | Media        | Media   | Media     | CP-CAT-04                          |
| Código HTTP incorrecto al crear categoría | Media        | Media   | Media     | CP-CAT-01                          |
| Nombre de producto inválido               | Alta         | Media   | Alta      | CP-PROD-09, CP-PROD-10             |
| Precio inválido                           | Alta         | Alta    | Alta      | CP-PROD-11, CP-PROD-12, CP-PROD-13 |
| Stock inválido                            | Alta         | Alta    | Alta      | CP-PROD-14, CP-PROD-15             |
| Categoría inexistente en producto         | Media        | Alta    | Alta      | CP-PROD-16, CP-PROD-18             |
| Producto inexistente                      | Media        | Alta    | Alta      | CP-PROD-04, CP-PROD-06, CP-PROD-08 |
| Error durante eliminación                 | Media        | Alta    | Alta      | CP-PROD-07, CP-PROD-08             |

---

## 8. Estrategia de pruebas

Se utilizarán las siguientes técnicas:

### 8.1 Pruebas positivas

Verifican que la API acepta información válida.

Ejemplos:

* Crear una categoría válida.
* Crear un producto válido.
* Consultar recursos existentes.
* Actualizar un producto existente.
* Eliminar un producto existente.

### 8.2 Pruebas negativas

Verifican el comportamiento ante datos inválidos o recursos inexistentes.

Ejemplos:

* Nombre demasiado corto.
* Precio igual a cero.
* Precio negativo.
* Stock negativo.
* Categoría inexistente.
* Producto inexistente.
* Categoría duplicada.

### 8.3 Pruebas de frontera

Se verifican valores ubicados en los límites definidos por las reglas de negocio.

Ejemplos:

* Nombre de categoría de exactamente 3 caracteres.
* Nombre de producto de exactamente 3 caracteres.
* Precio mínimo positivo.
* Stock igual a cero.

### 8.4 Pruebas automatizadas

Se automatizaron **25 casos de prueba** mediante pytest:

* 7 casos de categorías.
* 18 casos de productos.

Todos los casos fueron ejecutados correctamente en la última ejecución de la suite.

---

## 9. Datos de prueba

### Categorías

Se utiliza una base inicial de categorías con identificadores del 1 al 9.

Entre los datos disponibles se encuentran:

* Laptops
* Smartphones
* Tablets
* Headphones
* Monitors
* Keyboards
* Mice
* Smartwatches
* Speakers

### Productos

Se utiliza una base inicial de cinco productos.

Los productos contienen:

* `id`
* `name`
* `price`
* `stock`
* `category_id`

### Datos especiales

Para las pruebas negativas y de frontera se utilizan:

* ID inexistente: `99999`
* Nombre de 2 caracteres.
* Nombre de exactamente 3 caracteres.
* Precio `0`.
* Precio `-1000`.
* Precio mínimo positivo `0.01`.
* Stock `0`.
* Stock `-1`.
* Categoría inexistente `99999`.

---

## 10. Ambiente de pruebas

**Sistema operativo:** Windows
**Python:** 3.14.6
**FastAPI:** 0.141.1
**Starlette:** 1.6.0
**AnyIO:** 4.15.1
**pytest:** 9.1.1
**Cliente HTTP:** FastAPI TestClient

Las pruebas se ejecutan desde la raíz del proyecto mediante pytest.

---

## 11. Criterios de entrada

Las pruebas pueden iniciar cuando:

* La aplicación puede importar correctamente.
* Los endpoints están implementados.
* Los esquemas de validación están disponibles.
* Los datos iniciales de prueba están definidos.
* Los archivos de pruebas automatizadas están disponibles.
* Los requisitos y reglas de negocio están identificados.

---

## 12. Criterios de suspensión

Las pruebas deberán suspenderse si:

* La aplicación no puede iniciar.
* Existe un error que impide ejecutar la mayoría de los casos.
* Los datos de prueba no están disponibles.
* Los cambios realizados impiden ejecutar pytest.

Una vez corregida la causa, se debe reanudar la ejecución desde los casos afectados y posteriormente realizar regresión.

---

## 13. Criterios de reanudación

Las pruebas se reanudarán cuando:

* La aplicación vuelva a ser ejecutable.
* Los datos de prueba estén disponibles.
* El defecto que provocó la suspensión haya sido corregido.
* Los casos afectados puedan ejecutarse nuevamente.

---

## 14. Criterios de salida

La evaluación se considera completa cuando se cumplan los siguientes criterios:

* Cobertura documental del 100 % de RF01–RF12.
* Cobertura documental del 100 % de RN01–RN08.
* Al menos 15 casos automatizados.
* Ejecución del 100 % de los casos críticos.
* Al menos 90 % de aprobación sobre los casos ejecutados.
* Cero defectos críticos abiertos.
* Todos los defectos identificados deben estar trazados a requisitos y casos.
* Debe existir evidencia de ejecución final.
* Debe realizarse una prueba de regresión después de las correcciones.

---

## 15. Roles

| Rol                          | Responsabilidad                                        |
| ---------------------------- | ------------------------------------------------------ |
| Equipo de desarrollo         | Implementar y corregir la API                          |
| Equipo de pruebas            | Diseñar, ejecutar y documentar las pruebas             |
| Responsable de documentación | Mantener plan, casos, trazabilidad, defectos e informe |
| Equipo del proyecto          | Revisar resultados y criterios de salida               |

---

## 16. Evidencia de ejecución actual

En la última ejecución de la suite automatizada se obtuvieron:

**25 pruebas ejecutadas**

**25 PASSED**

**0 FAILED**

**0 BLOCKED**

**Porcentaje de aprobación: 100 %**

Se presentó un warning de deprecación relacionado con `BlockingPortal` de Starlette/AnyIO. Este warning no produjo fallos en las pruebas ni alteró los resultados funcionales.
