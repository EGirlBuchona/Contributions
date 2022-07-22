# Product Management CRUD in PHP

This project implements a CRUD (Create, Read, Update, Delete) system in PHP for managing products stored in a MySQL database.

## Features

- **Add Products:** Allows adding new products with name and price.
- **Edit Products:** Edit existing product information.
- **Delete Products:** Remove products from the database.
- **List Products:** Display all products in a tabular format.

## Instructions

1. Set up a MySQL database with the following structure:
   ```sql
   CREATE DATABASE productos_db;
   USE productos_db;
   CREATE TABLE productos (
       id INT AUTO_INCREMENT PRIMARY KEY,
       nombre VARCHAR(100),
       precio DECIMAL(10, 2)
   );
   ```

2. Update `conexion.php` with your database credentials.

3. Open `index.php` in your browser to manage products.

## Dependencies

- PHP 7.0 or higher
- MySQL

# CRUD de Gestión de Productos en PHP

Este proyecto implementa un sistema CRUD (Crear, Leer, Actualizar, Eliminar) en PHP para gestionar productos almacenados en una base de datos MySQL.

## Características

- **Agregar Productos:** Permite agregar nuevos productos con nombre y precio.
- **Editar Productos:** Edita la información de productos existentes.
- **Eliminar Productos:** Elimina productos de la base de datos.
- **Listar Productos:** Muestra todos los productos en formato tabular.

## Instrucciones

1. Configure una base de datos MySQL con la siguiente estructura:
   ```sql
   CREATE DATABASE productos_db;
   USE productos_db;
   CREATE TABLE productos (
       id INT AUTO_INCREMENT PRIMARY KEY,
       nombre VARCHAR(100),
       precio DECIMAL(10, 2)
   );
   ```

2. Actualice `conexion.php` con sus credenciales de base de datos.

3. Abra `index.php` en su navegador para gestionar productos.

## Dependencias

- PHP 7.0 o superior
- MySQL
