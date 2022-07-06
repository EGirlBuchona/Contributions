# User Registration Page in PHP

This project implements a user registration page using PHP and MySQL. The data is stored securely in a database, and passwords are hashed for additional security.

## Features

- **User Registration:** Allows users to register with a name, email, and password.
- **Database Integration:** Saves user data in a MySQL database.
- **Responsive Design:** The page is responsive and adapts to different screen sizes.

## Instructions

1. Set up a MySQL database with the following structure:
   ```sql
   CREATE DATABASE registro_usuarios;
   USE registro_usuarios;
   CREATE TABLE usuarios (
       id INT AUTO_INCREMENT PRIMARY KEY,
       nombre VARCHAR(255),
       email VARCHAR(255) UNIQUE,
       password VARCHAR(255)
   );
   ```

2. Update `conexion.php` with your database credentials.

3. Open `index.php` in a browser to test the registration functionality.

## Dependencies

- PHP 7.0 or higher
- MySQL

# Página de Registro de Usuarios en PHP

Este proyecto implementa una página de registro de usuarios utilizando PHP y MySQL. Los datos se almacenan de manera segura en una base de datos, y las contraseñas se encriptan para mayor seguridad.

## Características

- **Registro de Usuarios:** Permite a los usuarios registrarse con un nombre, correo electrónico y contraseña.
- **Integración con Base de Datos:** Guarda los datos de los usuarios en una base de datos MySQL.
- **Diseño Responsivo:** La página es responsiva y se adapta a diferentes tamaños de pantalla.

## Instrucciones

1. Configure una base de datos MySQL con la siguiente estructura:
   ```sql
   CREATE DATABASE registro_usuarios;
   USE registro_usuarios;
   CREATE TABLE usuarios (
       id INT AUTO_INCREMENT PRIMARY KEY,
       nombre VARCHAR(255),
       email VARCHAR(255) UNIQUE,
       password VARCHAR(255)
   );
   ```

2. Actualice `conexion.php` con sus credenciales de base de datos.

3. Abra `index.php` en un navegador para probar la funcionalidad de registro.

## Dependencias

- PHP 7.0 o superior
- MySQL
