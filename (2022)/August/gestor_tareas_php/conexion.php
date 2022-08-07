<?php
// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Archivo de Conexión a la Base de Datos

$servidor = "localhost";
$usuario = "root";
$contrasena = "";
$base_datos = "gestor_tareas";

$conn = new mysqli($servidor, $usuario, $contrasena, $base_datos);

if ($conn->connect_error) {
    die("Error de conexión: " . $conn->connect_error);
}
?>
