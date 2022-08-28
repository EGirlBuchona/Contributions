# Task Manager in PHP

This project implements a task manager in PHP with full CRUD (Create, Read, Update, Delete) functionality.

## Features

- **Add Tasks:** Create new tasks with a description.
- **Edit Tasks:** Update existing tasks.
- **Delete Tasks:** Remove tasks from the database.
- **List Tasks:** Display all tasks in a table.

## Instructions

1. Set up a MySQL database with the following structure:
   ```sql
   CREATE DATABASE gestor_tareas;
   USE gestor_tareas;
   CREATE TABLE tareas (
       id INT AUTO_INCREMENT PRIMARY KEY,
       descripcion VARCHAR(255)
   );
   ```

2. Update `conexion.php` with your database credentials.

3. Open `index.php` in your browser to manage tasks.

## Dependencies

- PHP 7.0 or higher
- MySQL

# Gestor de Tareas en PHP

Este proyecto implementa un gestor de tareas en PHP con funcionalidad CRUD completa (Crear, Leer, Actualizar, Eliminar).

## Características

- **Agregar Tareas:** Crea nuevas tareas con una descripción.
- **Editar Tareas:** Actualiza tareas existentes.
- **Eliminar Tareas:** Elimina tareas de la base de datos.
- **Listar Tareas:** Muestra todas las tareas en una tabla.

## Instrucciones

1. Configure una base de datos MySQL con la siguiente estructura:
   ```sql
   CREATE DATABASE gestor_tareas;
   USE gestor_tareas;
   CREATE TABLE tareas (
       id INT AUTO_INCREMENT PRIMARY KEY,
       descripcion VARCHAR(255)
   );
   ```

2. Actualice `conexion.php` con sus credenciales de base de datos.

3. Abra `index.php` en su navegador para gestionar tareas.

## Dependencias

- PHP 7.0 o superior
- MySQL
