# Matriz de Trazabilidad – API de Productos y Categorías

## 1. Objetivo

La matriz de trazabilidad relaciona los requisitos funcionales y las reglas de negocio con los casos de prueba diseñados y automatizados.

El objetivo es garantizar que cada requisito del contrato tenga al menos un caso de prueba asociado.

---

## 2. Trazabilidad de requisitos funcionales

| Requisito | Descripción                                     | Casos de prueba | Automatizado |
| --------- | ----------------------------------------------- | --------------- | ------------ |
| RF01      | Crear una categoría válida                      | CP-CAT-01       | Sí           |
| RF02      | Listar categorías                               | CP-CAT-02       | Sí           |
| RF03      | Consultar una categoría existente               | CP-CAT-03       | Sí           |
| RF04      | Devolver 404 para categoría inexistente         | CP-CAT-04       | Sí           |
| RF05      | Crear producto asociado a categoría existente   | CP-PROD-01      | Sí           |
| RF06      | Listar productos                                | CP-PROD-02      | Sí           |
| RF07      | Consultar producto existente                    | CP-PROD-03      | Sí           |
| RF08      | Devolver 404 para producto inexistente          | CP-PROD-04      | Sí           |
| RF09      | Actualizar producto existente                   | CP-PROD-05      | Sí           |
| RF10      | Devolver 404 al actualizar producto inexistente | CP-PROD-06      | Sí           |
| RF11      | Eliminar producto existente                     | CP-PROD-07      | Sí           |
| RF12      | Devolver 404 al eliminar producto inexistente   | CP-PROD-08      | Sí           |

**Cobertura de requisitos funcionales: 12/12 = 100 %.**

---

## 3. Trazabilidad de reglas de negocio

| Regla | Descripción                                                    | Casos de prueba                    | Automatizado |
| ----- | -------------------------------------------------------------- | ---------------------------------- | ------------ |
| RN01  | Nombre de categoría obligatorio, entre 3 y 60 caracteres       | CP-CAT-05, CP-CAT-06               | Sí           |
| RN02  | Nombre de categoría único sin distinguir mayúsculas/minúsculas | CP-CAT-07                          | Sí           |
| RN03  | Nombre de producto obligatorio, entre 3 y 80 caracteres        | CP-PROD-09, CP-PROD-10             | Sí           |
| RN04  | Precio estrictamente mayor que 0                               | CP-PROD-11, CP-PROD-12, CP-PROD-13 | Sí           |
| RN05  | Stock mayor o igual que 0                                      | CP-PROD-14, CP-PROD-15             | Sí           |
| RN06  | `category_id` debe corresponder a una categoría existente      | CP-PROD-16, CP-PROD-18             | Sí           |
| RN07  | Se permite stock igual a 0                                     | CP-PROD-14                         | Sí           |
| RN08  | La actualización conserva las validaciones de creación         | CP-PROD-17, CP-PROD-18             | Sí           |

**Cobertura de reglas de negocio: 8/8 = 100 %.**

---

## 4. Trazabilidad por endpoint

| Endpoint           | Método | Requisitos                         | Casos asociados                                                                                            |
| ------------------ | ------ | ---------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `/categories`      | POST   | RF01, RN01, RN02                   | CP-CAT-01, CP-CAT-05, CP-CAT-06, CP-CAT-07                                                                 |
| `/categories`      | GET    | RF02                               | CP-CAT-02                                                                                                  |
| `/categories/{id}` | GET    | RF03, RF04                         | CP-CAT-03, CP-CAT-04                                                                                       |
| `/products`        | POST   | RF05, RN03, RN04, RN05, RN06, RN07 | CP-PROD-01, CP-PROD-09, CP-PROD-10, CP-PROD-11, CP-PROD-12, CP-PROD-13, CP-PROD-14, CP-PROD-15, CP-PROD-16 |
| `/products/`       | GET    | RF06                               | CP-PROD-02                                                                                                 |
| `/products/{id}`   | GET    | RF07, RF08                         | CP-PROD-03, CP-PROD-04                                                                                     |
| `/products/{id}`   | PUT    | RF09, RF10, RN08, RN06             | CP-PROD-05, CP-PROD-06, CP-PROD-17, CP-PROD-18                                                             |
| `/products/{id}`   | DELETE | RF11, RF12                         | CP-PROD-07, CP-PROD-08                                                                                     |

---

## 5. Trazabilidad de códigos HTTP

| Situación                               | Código esperado | Caso de prueba |
| --------------------------------------- | --------------: | -------------- |
| Creación válida de categoría            |             201 | CP-CAT-01      |
| Consulta de categorías                  |             200 | CP-CAT-02      |
| Consulta de categoría existente         |             200 | CP-CAT-03      |
| Categoría inexistente                   |             404 | CP-CAT-04      |
| Nombre de categoría inválido            |             422 | CP-CAT-05      |
| Nombre de categoría en límite válido    |             201 | CP-CAT-06      |
| Categoría duplicada                     |             409 | CP-CAT-07      |
| Creación válida de producto             |             201 | CP-PROD-01     |
| Listado de productos                    |             200 | CP-PROD-02     |
| Producto existente                      |             200 | CP-PROD-03     |
| Producto inexistente                    |             404 | CP-PROD-04     |
| Actualización válida                    |             200 | CP-PROD-05     |
| Actualización de producto inexistente   |             404 | CP-PROD-06     |
| Eliminación válida                      |             204 | CP-PROD-07     |
| Eliminación de producto inexistente     |             404 | CP-PROD-08     |
| Nombre de producto inválido             |             422 | CP-PROD-09     |
| Nombre de producto en límite válido     |             201 | CP-PROD-10     |
| Precio igual a cero                     |             422 | CP-PROD-11     |
| Precio negativo                         |             422 | CP-PROD-12     |
| Precio mínimo positivo                  |             201 | CP-PROD-13     |
| Stock igual a cero                      |             201 | CP-PROD-14     |
| Stock negativo                          |             422 | CP-PROD-15     |
| Categoría inexistente al crear producto |             404 | CP-PROD-16     |
| Precio inválido al actualizar           |             422 | CP-PROD-17     |
| Categoría inexistente al actualizar     |             404 | CP-PROD-18     |

---

## 6. Resumen de cobertura

| Elemento               | Cubiertos | Total | Cobertura |
| ---------------------- | --------: | ----: | --------: |
| Requisitos funcionales |        12 |    12 |     100 % |
| Reglas de negocio      |         8 |     8 |     100 % |
| Casos de categorías    |         7 |     7 |     100 % |
| Casos de productos     |        18 |    18 |     100 % |
| Casos automatizados    |        25 |    25 |     100 % |

---

## 7. Resultado de ejecución

La suite automatizada cuenta actualmente con **25 casos de prueba**.

Resultado de la última ejecución:

* **25 PASSED**
* **0 FAILED**
* **0 BLOCKED**
* **100 % de aprobación**

Los casos automatizados cubren escenarios positivos, negativos, de frontera, recursos inexistentes, actualización y eliminación.

---

## 8. Criterio de trazabilidad

Todos los requisitos funcionales RF01–RF12 y todas las reglas de negocio RN01–RN08 cuentan con al menos un caso de prueba asociado.

La trazabilidad permite identificar:

**Requisito → Regla de negocio → Caso de prueba → Automatización → Resultado**

Por lo tanto, la cobertura documental de requisitos alcanza el **100 %**.
