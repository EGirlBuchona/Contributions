<?php
// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: CRUD de Productos en PHP

include 'conexion.php';

$id = $_GET['id'];
$sql = "SELECT * FROM productos WHERE id = $id";
$resultado = $conn->query($sql);
$producto = $resultado->fetch_assoc();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $nombre = $_POST['nombre'];
    $precio = $_POST['precio'];

    $sql = "UPDATE productos SET nombre = '$nombre', precio = '$precio' WHERE id = $id";
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
    <title>Editar Producto</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
    <header>
        <h1>Editar Producto</h1>
        <a href="index.php" class="btn">Regresar</a>
    </header>
    <main>
        <form method="POST" action="editar.php?id=<?= $id ?>">
            <label for="nombre">Nombre:</label>
            <input type="text" id="nombre" name="nombre" value="<?= $producto['nombre'] ?>" required>
            
            <label for="precio">Precio:</label>
            <input type="number" id="precio" name="precio" step="0.01" value="<?= $producto['precio'] ?>" required>
            
            <button type="submit" class="btn">Guardar Cambios</button>
        </form>
    </main>
</body>
</html>
