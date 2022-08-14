<?php
include 'conexion.php';

$id = $_GET['id'];
$resultado = $conn->query("SELECT * FROM tareas WHERE id = $id");
$tarea = $resultado->fetch_assoc();

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $descripcion = $_POST['descripcion'];
    $conn->query("UPDATE tareas SET descripcion = '$descripcion' WHERE id = $id");
    header("Location: index.php");
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Editar Tarea</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
    <header>
        <h1>Editar Tarea</h1>
    </header>
    <main>
        <form method="POST">
            <label for="descripcion">Descripción:</label>
            <input type="text" id="descripcion" name="descripcion" value="<?= $tarea['descripcion'] ?>" required>
            <button type="submit">Actualizar</button>
        </form>
    </main>
</body>
</html>
