<?php
// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: CRUD de Productos en PHP

include 'conexion.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $nombre = $_POST['nombre'];
    $precio = $_POST['precio'];

    $sql = "INSERT INTO productos (nombre, precio) VALUES ('$nombre', '$precio')";
    if ($conn->query($sql)) {
        header("Location: index.php");
    } else {
        echo "Error: " . $conn->error;
    }
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agregar Producto</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
    <header>
        <h1>Agregar Producto</h1>
        <a href="index.php" class="btn">Regresar</a>
    </header>
    <main>
        <form method="POST" action="agregar.php">
            <label for="nombre">Nombre:</label>
            <input type="text" id="nombre" name="nombre" required>
            
            <label for="precio">Precio:</label>
            <input type="number" id="precio" name="precio" step="0.01" required>
            
            <button type="submit" class="btn">Agregar</button>
        </form>
    </main>
</body>
</html>
