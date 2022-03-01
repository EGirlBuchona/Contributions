// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022

// Función para mostrar un saludo basado en la hora
function mostrarSaludo() {
    const saludo = document.getElementById("saludo");
    const hora = new Date().getHours();

    if (hora < 12) {
        saludo.textContent = "¡Buenos días!";
    } else if (hora < 18) {
        saludo.textContent = "¡Buenas tardes!";
    } else {
        saludo.textContent = "¡Buenas noches!";
    }
}

// Función para mostrar un mensaje cuando se hace clic en el botón
function mostrarMensaje() {
    const mensaje = document.getElementById("mensaje");
    mensaje.textContent = "Gracias por visitar mi página interactiva. ¡Que tengas un gran día!";
}

// Ejecutar la función de saludo al cargar la página
window.onload = mostrarSaludo;
