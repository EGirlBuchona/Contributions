<?php
// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: Página de Registro de Usuarios en PHP

include 'conexion.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nombre = $_POST['nombre'];
    $email = $_POST['email'];
    $password = password_hash($_POST['password'], PASSWORD_DEFAULT);

    $sql = "INSERT INTO usuarios (nombre, email, password) VALUES ('$nombre', '$email', '$password')";
    if ($conn->query($sql) === TRUE) {
        echo "<p class='success'>Registro exitoso. ¡Bienvenido $nombre!</p>";
    } else {
        echo "<p class='error'>Error: " . $conn->error . "</p>";
    }
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registro de Usuario</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
    <header>
        <h1>Registro de Usuarios</h1>
        <p>Complete el formulario para registrarse.</p>
    </header>
    <main>
        <form method="POST" action="">
            <label for="nombre">Nombre:</label>
            <input type="text" id="nombre" name="nombre" required>
            
            <label for="email">Correo Electrónico:</label>
            <input type="email" id="email" name="email" required>
            
            <label for="password">Contraseña:</label>
            <input type="password" id="password" name="password" required>
            
            <button type="submit">Registrar</button>
        </form>
    </main>
    <footer>
        <p>© 2022 Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona</p>
    </footer>
</body>
</html>
