# Basic Task Management API with Flask

This project is a simple REST API built with Flask in Python for managing a task list. It supports CRUD operations to create, read, update, and delete tasks.

## Instructions

1. Install Flask if you haven't already:
pip install Flask
2. Run the application:
python app.py
3. Access the API at `http://127.0.0.1:5000/tareas`.

## Endpoints

- **GET /tareas** - Retrieve all tasks
- **GET /tareas/<id>** - Retrieve a task by ID
- **POST /tareas** - Create a new task
- **PUT /tareas/<id>** - Update an existing task
- **DELETE /tareas/<id>** - Delete a task

## Dependencies
- Flask

# API Básica de Gestión de Tareas con Flask

Este proyecto es una API REST sencilla construida con Flask en Python para gestionar una lista de tareas. Soporta operaciones CRUD para crear, leer, actualizar y eliminar tareas.

## Instrucciones

1. Instale Flask si aún no lo ha hecho:
pip install Flask
2. Ejecute la aplicación:
python app.py
3. Acceda a la API en `http://127.0.0.1:5000/tareas`.

## Endpoints

- **GET /tareas** - Obtener todas las tareas
- **GET /tareas/<id>** - Obtener una tarea por ID
- **POST /tareas** - Crear una nueva tarea
- **PUT /tareas/<id>** - Actualizar una tarea existente
- **DELETE /tareas/<id>** - Eliminar una tarea

## Dependencias
- Flask

Nota: Esta API permite realizar las operaciones CRUD en una lista de tareas. La API incluye rutas para crear, leer, actualizar y eliminar tareas, y maneja los errores básicos cuando no se encuentra una tarea específica.