// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022

function enviarEncuesta() {
    const lenguaje = document.getElementById("pregunta1").value;
    const tiempo = document.getElementById("pregunta2").value;
    
    const resultadoDiv = document.getElementById("resultado");
    resultadoDiv.innerHTML = `<p>Gracias por participar en la encuesta.</p>
                              <p>Tu lenguaje de programación favorito es: <strong>${lenguaje}</strong></p>
                              <p>Tiempo dedicado a la programación: <strong>${tiempo}</strong></p>`;
}
