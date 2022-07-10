<?php
// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: Página de Contacto en PHP

include 'conexion.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nombre = $_POST['nombre'];
    $email = $_POST['email'];
    $mensaje = $_POST['mensaje'];

    $sql = "INSERT INTO contactos (nombre, email, mensaje) VALUES ('$nombre', '$email', '$mensaje')";
    if ($conn->query($sql) === TRUE) {
        echo "<p class='success'>Mensaje enviado exitosamente. ¡Gracias, $nombre!</p>";
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
    <title>Formulario de Contacto</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
    <header>
        <h1>Contacto</h1>
        <p>Envíanos un mensaje y nos pondremos en contacto contigo.</p>
    </header>
    <main>
        <form method="POST" action="">
            <label for="nombre">Nombre:</label>
            <input type="text" id="nombre" name="nombre" required>
            
            <label for="email">Correo Electrónico:</label>
            <input type="email" id="email" name="email" required>
            
            <label for="mensaje">Mensaje:</label>
            <textarea id="mensaje" name="mensaje" required></textarea>
            
            <button type="submit">Enviar</button>
        </form>
    </main>
    <footer>
        <p>© 2022 Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona</p>
    </footer>
</body>
</html>
