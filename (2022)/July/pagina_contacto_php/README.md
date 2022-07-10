# Contact Form Page in PHP

This project implements a contact form using PHP. It stores the submitted data in a MySQL database and includes basic validations.

## Features

- **Form Submission:** Allows users to submit their name, email, and a message.
- **Database Integration:** Saves form submissions in a MySQL database.
- **Responsive Design:** The page is responsive and adapts to various screen sizes.

## Instructions

1. Set up a MySQL database with the following structure:
   ```sql
   CREATE DATABASE formulario_contacto;
   USE formulario_contacto;
   CREATE TABLE contactos (
       id INT AUTO_INCREMENT PRIMARY KEY,
       nombre VARCHAR(255),
       email VARCHAR(255),
       mensaje TEXT
   );
   ```

2. Update `conexion.php` with your database credentials.

3. Open `index.php` in a browser to test the contact form.

## Dependencies

- PHP 7.0 or higher
- MySQL

# Página de Formulario de Contacto en PHP

Este proyecto implementa un formulario de contacto utilizando PHP. Los datos enviados se almacenan en una base de datos MySQL e incluye validaciones básicas.

## Características

- **Envío de Formularios:** Permite a los usuarios enviar su nombre, correo electrónico y un mensaje.
- **Integración con Base de Datos:** Guarda los datos del formulario en una base de datos MySQL.
- **Diseño Responsivo:** La página es responsiva y se adapta a diferentes tamaños de pantalla.

## Instrucciones

1. Configure una base de datos MySQL con la siguiente estructura:
   ```sql
   CREATE DATABASE formulario_contacto;
   USE formulario_contacto;
   CREATE TABLE contactos (
       id INT AUTO_INCREMENT PRIMARY KEY,
       nombre VARCHAR(255),
       email VARCHAR(255),
       mensaje TEXT
   );
   ```

2. Actualice `conexion.php` con sus credenciales de base de datos.

3. Abra `index.php` en un navegador para probar el formulario de contacto.

## Dependencias

- PHP 7.0 o superior
- MySQL
