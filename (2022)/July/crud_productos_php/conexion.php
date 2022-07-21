<?php
$servidor = "localhost";
$usuario = "root";
$contrasena = "";
$base_datos = "productos_db";

$conn = new mysqli($servidor, $usuario, $contrasena, $base_datos);

if ($conn->connect_error) {
    die("Error de conexión: " . $conn->connect_error);
}
?>
