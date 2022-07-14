<?php
session_start();
include 'conexion.php';

$usuario = $_POST['usuario'];
$password = $_POST['password'];

$sql = "SELECT * FROM usuarios WHERE usuario = '$usuario'";
$resultado = $conn->query($sql);

if ($resultado->num_rows > 0) {
    $fila = $resultado->fetch_assoc();
    if (password_verify($password, $fila['password'])) {
        $_SESSION['usuario'] = $usuario;
        header("Location: bienvenido.php");
    } else {
        echo "<p class='error'>Contraseña incorrecta.</p>";
    }
} else {
    echo "<p class='error'>Usuario no encontrado.</p>";
}
?>
