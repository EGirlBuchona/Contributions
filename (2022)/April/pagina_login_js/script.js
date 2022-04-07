// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022

function validarLogin() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const errorMsg = document.getElementById("error-msg");

    fetch("/auth", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Inicio de sesión exitoso");
            window.location.href = "/home";
        } else {
            errorMsg.textContent = "Usuario o contraseña incorrectos";
        }
    })
    .catch(error => {
        console.error("Error en la autenticación:", error);
        errorMsg.textContent = "Error al conectar con el servidor";
    });
}
