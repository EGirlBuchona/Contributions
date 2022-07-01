# Dynamic PHP Page with Database Connection

This project is a dynamic web page built with PHP and MySQL. It retrieves and displays content from a database table in a visually appealing format.

## Features

- **Dynamic Content:** Displays data directly from the database.
- **Database Connection:** Utilizes MySQL for data storage.
- **Responsive Design:** Adapts to various screen sizes.
- **Easy to Customize:** Modify the PHP and CSS files to fit your needs.

## Instructions

1. Set up a MySQL database with the following structure:
   ```sql
   CREATE DATABASE pagina_dinamica;
   USE pagina_dinamica;
   CREATE TABLE contenidos (
       id INT AUTO_INCREMENT PRIMARY KEY,
       titulo VARCHAR(255),
       descripcion TEXT
   );
   INSERT INTO contenidos (titulo, descripcion) VALUES
   ('Project 1', 'Description of Project 1'),
   ('Project 2', 'Description of Project 2'),
   ('Project 3', 'Description of Project 3');
   ```

2. Update `conexion.php` with your database credentials.

3. Open `index.php` in a browser to see the dynamic content.

## Dependencies

- PHP 7.0 or higher
- MySQL

# Página Dinámica en PHP con Conexión a Base de Datos

Este proyecto es una página web dinámica construida con PHP y MySQL. Recupera y muestra contenido desde una tabla en la base de datos en un formato visualmente atractivo.

## Características

- **Contenido Dinámico:** Muestra datos directamente desde la base de datos.
- **Conexión a Base de Datos:** Utiliza MySQL para el almacenamiento de datos.
- **Diseño Responsivo:** Se adapta a varios tamaños de pantalla.
- **Fácil de Personalizar:** Modifique los archivos PHP y CSS para adaptarlos a sus necesidades.

## Instrucciones

1. Configure una base de datos MySQL con la siguiente estructura:
   ```sql
   CREATE DATABASE pagina_dinamica;
   USE pagina_dinamica;
   CREATE TABLE contenidos (
       id INT AUTO_INCREMENT PRIMARY KEY,
       titulo VARCHAR(255),
       descripcion TEXT
   );
   INSERT INTO contenidos (titulo, descripcion) VALUES
   ('Proyecto 1', 'Descripción del Proyecto 1'),
   ('Proyecto 2', 'Descripción del Proyecto 2'),
   ('Proyecto 3', 'Descripción del Proyecto 3');
   ```

2. Actualice `conexion.php` con sus credenciales de base de datos.

3. Abra `index.php` en un navegador para ver el contenido dinámico.

## Dependencias

- PHP 7.0 o superior
- MySQL
