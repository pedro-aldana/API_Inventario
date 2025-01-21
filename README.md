
# API REST - Gestion de inventario, clientes y proveedores

una API REST para la gestión de inventarios, clientes y proveedores, diseñada para ser escalable y eficiente. La API permite llevar un control detallado de los productos en inventario, administrar relaciones con clientes y proveedores, y optimizar los procesos de negocio mediante operaciones CRUD seguras y rápidas. Implementé autenticación robusta, manejo de permisos y endpoints personalizados, garantizando un flujo de trabajo organizado y seguro




# API REST Documentacion

## Default Routes

### POST `/verify-token`
**Description:** Verifies the validity of a provided token.

---

## User Routes

### POST `/api/users/register`
**Description:** Registers a new user.

### POST `/api/users/login`
**Description:** Logs in a user and provides an authentication token.

### GET `/api/users/me`
**Description:** Retrieves the details of the currently authenticated user.

---

## Category Routes

### POST `/api/category/create`
**Description:** Creates a new category.

### GET `/api/category/list`
**Description:** Retrieves a list of all categories.

### GET `/api/category/by_id/{category_id}`
**Description:** Retrieves details of a specific category by its ID.

### PUT `/api/category/update/{category_id}`
**Description:** Updates the details of a specific category by its ID.

### DELETE `/api/category/delete/{category_id}`
**Description:** Deletes a specific category by its ID.

---

## Product Routes

### POST `/api/product/create`
**Description:** Creates a new product.

### GET `/api/product/list`
**Description:** Retrieves a list of all products.

### GET `/api/product/by_id/{product_id}`
**Description:** Retrieves details of a specific product by its ID.

### PUT `/api/product/update/{product_id}`
**Description:** Updates the details of a specific product by its ID.

### DELETE `/api/product/delete/{product_id}`
**Description:** Deletes a specific product by its ID.

---

## Stock Routes

### POST `/api/stock/create`
**Description:** Creates a new stock entry.

### GET `/api/stock/list`
**Description:** Retrieves a list of all stock entries.

### GET `/api/stock/by_id/{stock_id}`
**Description:** Retrieves details of a specific stock entry by its ID.

### PUT `/api/stock/update/{stock_id}`
**Description:** Updates the details of a specific stock entry by its ID.

### DELETE `/api/stock/delete/{stock_id}`
**Description:** Deletes a specific stock entry by its ID.



## Screenshots

![App Screenshot](https://zt7prs54ew.ufs.sh/f/MWxHR0BmEvpLrzEFCrIGKCcBtvDoeh6wnPJpVAX2Ub1qHg5m)


## Modelo ER

![App Screenshot](https://zt7prs54ew.ufs.sh/f/MWxHR0BmEvpLzUzD1XTY6Pc7isqFomhgClU9Z1AESy3THvJx)
# Tecnologías Utilizadas

Este proyecto utiliza las siguientes tecnologías:

## 1. **FastAPI**
FastAPI es un framework web moderno y rápido (de alto rendimiento) para construir APIs con Python 3.7+ basado en anotaciones de tipo estándar de Python.
- **Características:**
  - Soporte integrado para programación asincrónica.
  - Generación automática de documentación interactiva para la API (Swagger UI y ReDoc).
  - Validación y serialización de datos usando Pydantic.
  - Alto rendimiento, comparable con frameworks como Node.js y Go.

## 2. **PostgreSQL**
PostgreSQL es un sistema de base de datos relacional de código abierto, potente y orientado a objetos, que utiliza y amplía el lenguaje SQL.
- **Características:**
  - Robusto y escalable para manejar grandes cantidades de datos.
  - Soporte avanzado para consultas y manipulación de datos.
  - Cumplimiento con ACID para transacciones confiables.

## 3. **Uvicorn**
Uvicorn es una implementación de servidor ASGI extremadamente rápida, que utiliza `uvloop` y `httptools`.
- **Características:**
  - Servidor asincrónico de alto rendimiento.
  - Diseñado para ejecutar aplicaciones FastAPI de manera eficiente.

## 4. **Tortoise-ORM**
Tortoise-ORM es un ORM asincrónico fácil de usar, inspirado en Django.
- **Características:**
  - Manejo simplificado de consultas a la base de datos y relaciones.
  - Soporte completo para PostgreSQL y otras bases de datos.
  - Integración con Pydantic para validación y serialización de datos sin complicaciones.

---

### ¿Por qué estas tecnologías?
Esta pila tecnológica fue elegida para garantizar un alto rendimiento, escalabilidad y facilidad de desarrollo. FastAPI y Tortoise-ORM simplifican la creación de APIs robustas, mientras que PostgreSQL proporciona una solución de base de datos confiable, y Uvicorn asegura una ejecución eficiente de la aplicación.
