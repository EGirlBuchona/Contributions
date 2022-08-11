<?php
// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Script para Eliminar una Tarea

include 'conexion.php';

if (isset($_GET['id'])) {
    $id = intval($_GET['id']);
    $stmt = $conn->prepare("DELETE FROM tareas WHERE id = ?");
    $stmt->bind_param("i", $id);
    $stmt->execute();

    if ($stmt->affected_rows > 0) {
        echo "<script>alert('Tarea eliminada exitosamente'); window.location='index.php';</script>";
    } else {
        echo "<script>alert('Error al eliminar la tarea'); window.location='index.php';</script>";
    }
    $stmt->close();
}
?>
