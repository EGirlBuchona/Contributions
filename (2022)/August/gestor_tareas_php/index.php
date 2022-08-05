<?php
// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: Gestor de Tareas en PHP

include 'conexion.php';

$resultado = $conn->query("SELECT * FROM tareas");

?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestor de Tareas</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
    <header>
        <h1>Gestor de Tareas</h1>
        <a href="agregar.php" class="btn">Agregar Tarea</a>
    </header>
    <main>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Tarea</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                <?php while ($tarea = $resultado->fetch_assoc()): ?>
                    <tr>
                        <td><?= $tarea['id'] ?></td>
                        <td><?= $tarea['descripcion'] ?></td>
                        <td>
                            <a href="editar.php?id=<?= $tarea['id'] ?>" class="btn">Editar</a>
                            <a href="eliminar.php?id=<?= $tarea['id'] ?>" class="btn eliminar">Eliminar</a>
                        </td>
                    </tr>
                <?php endwhile; ?>
            </tbody>
        </table>
    </main>
</body>
</html>
