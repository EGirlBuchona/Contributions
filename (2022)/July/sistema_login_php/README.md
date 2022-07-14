# Login System in PHP

This project implements a basic login system in PHP that validates user credentials against a MySQL database.

## Features

- **User Authentication:** Verifies username and password.
- **Session Management:** Maintains user sessions after successful login.
- **Database Integration:** Stores user credentials in a MySQL database.

## Instructions

1. Set up a MySQL database with the following structure:
   ```sql
   CREATE DATABASE sistema_login;
   USE sistema_login;
   CREATE TABLE usuarios (
       id INT AUTO_INCREMENT PRIMARY KEY,
       usuario VARCHAR(50) UNIQUE,
       password VARCHAR(255)
   );
   INSERT INTO usuarios (usuario, password) VALUES ('admin', PASSWORD('admin123'));
   ```

2. Update `conexion.php` with your database credentials.

3. Run `index.php` in your browser to test the login system.

## Dependencies

- PHP 7.0 or higher
- MySQL

# Sistema de Login en PHP

Este proyecto implementa un sistema básico de login en PHP que valida credenciales de usuario utilizando una base de datos MySQL.

## Características

- **Autenticación de Usuarios:** Verifica el usuario y la contraseña.
- **Gestión de Sesiones:** Mantiene sesiones de usuario después del login exitoso.
- **Integración con Base de Datos:** Almacena credenciales de usuario en una base de datos MySQL.

## Instrucciones

1. Configure una base de datos MySQL con la siguiente estructura:
   ```sql
   CREATE DATABASE sistema_login;
   USE sistema_login;
   CREATE TABLE usuarios (
       id INT AUTO_INCREMENT PRIMARY KEY,
       usuario VARCHAR(50) UNIQUE,
       password VARCHAR(255)
   );
   INSERT INTO usuarios (usuario, password) VALUES ('admin', PASSWORD('admin123'));
   ```

2. Actualice `conexion.php` con sus credenciales de base de datos.

3. Ejecute `index.php` en su navegador para probar el sistema de login.

## Dependencias

- PHP 7.0 o superior
- MySQL
