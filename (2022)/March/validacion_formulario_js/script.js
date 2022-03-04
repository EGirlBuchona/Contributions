// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022

function validarFormulario() {
    let valido = true;

    // Validación del campo Nombre
    const nombre = document.getElementById("nombre").value;
    const errorNombre = document.getElementById("errorNombre");
    if (nombre.length < 3) {
        errorNombre.textContent = "El nombre debe tener al menos 3 caracteres.";
        valido = false;
    } else {
        errorNombre.textContent = "";
    }

    // Validación del campo Email
    const email = document.getElementById("email").value;
    const errorEmail = document.getElementById("errorEmail");
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        errorEmail.textContent = "Por favor, ingrese un correo electrónico válido.";
        valido = false;
    } else {
        errorEmail.textContent = "";
    }

    // Validación del campo Contraseña
    const password = document.getElementById("password").value;
    const errorPassword = document.getElementById("errorPassword");
    if (password.length < 8) {
        errorPassword.textContent = "La contraseña debe tener al menos 8 caracteres.";
        valido = false;
    } else {
        errorPassword.textContent = "";
    }

    return valido;
}
