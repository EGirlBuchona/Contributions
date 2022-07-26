<?php
// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: CRUD de Productos en PHP

include 'conexion.php';

$id = $_GET['id'];

$sql = "DELETE FROM productos WHERE id = $id";

if ($conn->query($sql)) {
    header("Location: index.php");
} else {
    echo "Error: " . $conn->error;
}
?>
