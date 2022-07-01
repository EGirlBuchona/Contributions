<?php
// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: Página Dinámica en PHP

include 'conexion.php';

// Obtener datos de la base de datos
$sql = "SELECT * FROM contenidos";
$resultado = $conn->query($sql);

?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página Dinámica PHP</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
    <header>
        <h1>Bienvenido a Mi Página Dinámica</h1>
        <p>Contenido generado desde una base de datos.</p>
    </header>
    <main>
        <section>
            <h2>Contenido</h2>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Título</th>
                        <th>Descripción</th>
                    </tr>
                </thead>
                <tbody>
                    <?php
                    if ($resultado->num_rows > 0) {
                        while ($fila = $resultado->fetch_assoc()) {
                            echo "<tr>";
                            echo "<td>" . $fila['id'] . "</td>";
                            echo "<td>" . $fila['titulo'] . "</td>";
                            echo "<td>" . $fila['descripcion'] . "</td>";
                            echo "</tr>";
                        }
                    } else {
                        echo "<tr><td colspan='3'>No hay contenido disponible</td></tr>";
                    }
                    $conn->close();
                    ?>
                </tbody>
            </table>
        </section>
    </main>
    <footer>
        <p>© 2022 Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona</p>
    </footer>
</body>
</html>
