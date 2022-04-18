// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022

const contenido = [
    "Contenido de la página 1",
    "Contenido de la página 2",
    "Contenido de la página 3",
    "Contenido de la página 4",
    "Contenido de la página 5",
    "Contenido de la página 6",
    "Contenido de la página 7",
    "Contenido de la página 8",
    "Contenido de la página 9",
    "Contenido de la página 10"
];

const itemsPorPagina = 2;
let paginaActual = 1;

function mostrarPagina(pagina) {
    const contenidoDiv = document.getElementById("contenido");
    contenidoDiv.innerHTML = "";

    const inicio = (pagina - 1) * itemsPorPagina;
    const fin = inicio + itemsPorPagina;
    const elementosPagina = contenido.slice(inicio, fin);

    elementosPagina.forEach(texto => {
        const p = document.createElement("p");
        p.textContent = texto;
        contenidoDiv.appendChild(p);
    });

    document.getElementById("paginacion").innerHTML = "";
    for (let i = 1; i <= Math.ceil(contenido.length / itemsPorPagina); i++) {
        const boton = document.createElement("button");
        boton.textContent = i;
        boton.classList.add("pagina");
        boton.disabled = (i === pagina);
        boton.classList.toggle("active", i === pagina);
        boton.addEventListener("click", () => {
            paginaActual = i;
            mostrarPagina(i);
        });
        document.getElementById("paginacion").appendChild(boton);
    }
}

document.addEventListener("DOMContentLoaded", () => {
    mostrarPagina(paginaActual);
});
