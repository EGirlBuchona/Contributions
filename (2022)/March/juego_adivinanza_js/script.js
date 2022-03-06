// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022

let numeroSecreto = Math.floor(Math.random() * 100) + 1;
let intentos = 0;

function adivinar() {
    const intento = parseInt(document.getElementById("intento").value);
    const mensaje = document.getElementById("mensaje");
    const contadorIntentos = document.getElementById("intentos");
    
    intentos++;
    contadorIntentos.textContent = intentos;

    if (isNaN(intento) || intento < 1 || intento > 100) {
        mensaje.textContent = "Por favor, ingresa un número válido entre 1 y 100.";
    } else if (intento === numeroSecreto) {
        mensaje.textContent = `¡Felicidades! Adivinaste el número en ${intentos} intentos.`;
        reiniciarJuego();
    } else if (intento < numeroSecreto) {
        mensaje.textContent = "El número secreto es más alto.";
    } else {
        mensaje.textContent = "El número secreto es más bajo.";
    }
}

function reiniciarJuego() {
    numeroSecreto = Math.floor(Math.random() * 100) + 1;
    intentos = 0;
    document.getElementById("intentos").textContent = intentos;
}
