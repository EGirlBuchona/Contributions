<?php
// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: CRUD de Productos en PHP

include 'conexion.php';

$resultado = $conn->query("SELECT * FROM productos");

?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRUD de Productos</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
    <header>
        <h1>Gestión de Productos</h1>
        <a href="agregar.php" class="btn">Agregar Producto</a>
    </header>
    <main>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nombre</th>
                    <th>Precio</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                <?php while ($producto = $resultado->fetch_assoc()): ?>
                    <tr>
                        <td><?= $producto['id'] ?></td>
                        <td><?= $producto['nombre'] ?></td>
                        <td><?= $producto['precio'] ?></td>
                        <td>
                            <a href="editar.php?id=<?= $producto['id'] ?>" class="btn">Editar</a>
                            <a href="eliminar.php?id=<?= $producto['id'] ?>" class="btn eliminar">Eliminar</a>
                        </td>
                    </tr>
                <?php endwhile; ?>
            </tbody>
        </table>
    </main>
</body>
</html>
