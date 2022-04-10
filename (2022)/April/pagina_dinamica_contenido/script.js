// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022

document.addEventListener("DOMContentLoaded", function() {
    const contenidoDinamico = document.getElementById("contenido-dinamico");

    fetch("https://jsonplaceholder.typicode.com/posts")
        .then(response => response.json())
        .then(data => {
            contenidoDinamico.innerHTML = ""; // Limpiar contenido de carga

            data.slice(0, 5).forEach(post => { // Mostrar solo los primeros 5 posts
                const div = document.createElement("div");
                div.classList.add("post");

                const titulo = document.createElement("h3");
                titulo.textContent = post.title;

                const cuerpo = document.createElement("p");
                cuerpo.textContent = post.body;

                div.appendChild(titulo);
                div.appendChild(cuerpo);
                contenidoDinamico.appendChild(div);
            });
        })
        .catch(error => {
            console.error("Error al cargar contenido:", error);
            contenidoDinamico.innerHTML = "<p>Error al cargar contenido.</p>";
        });
});
