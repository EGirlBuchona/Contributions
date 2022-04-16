// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022

const palabras = ["javascript", "ahorcado", "programacion", "desarrollador", "algoritmo"];
let palabraSeleccionada = palabras[Math.floor(Math.random() * palabras.length)];
let palabraOculta = Array(palabraSeleccionada.length).fill("_");
let intentos = 6;

document.getElementById("palabra").textContent = palabraOculta.join(" ");
document.getElementById("intentos").textContent = intentos;

function adivinarLetra() {
    const letra = document.getElementById("letra").value.toLowerCase();
    let acierto = false;

    for (let i = 0; i < palabraSeleccionada.length; i++) {
        if (palabraSeleccionada[i] === letra) {
            palabraOculta[i] = letra;
            acierto = true;
        }
    }

    document.getElementById("palabra").textContent = palabraOculta.join(" ");
    document.getElementById("letra").value = "";

    if (!acierto) {
        intentos--;
        document.getElementById("intentos").textContent = intentos;
    }

    if (palabraOculta.join("") === palabraSeleccionada) {
        document.getElementById("mensaje").textContent = "¡Ganaste! Has adivinado la palabra.";
    } else if (intentos === 0) {
        document.getElementById("mensaje").textContent = `Perdiste. La palabra era "${palabraSeleccionada}".`;
    }
}
