<?php
// Datos de conexión
$servidor = "localhost";
$usuario = "root";
$contrasena = "";
$base_datos = "pagina_dinamica";

// Crear conexión
$conn = new mysqli($servidor, $usuario, $contrasena, $base_datos);

// Verificar conexión
if ($conn->connect_error) {
    die("Error de conexión: " . $conn->connect_error);
}
?>
