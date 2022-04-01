// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022

document.addEventListener("DOMContentLoaded", function() {
    const proyectos = [
        { titulo: "Proyecto 1", descripcion: "Descripción del proyecto 1", imagen: "proyecto1.jpg" },
        { titulo: "Proyecto 2", descripcion: "Descripción del proyecto 2", imagen: "proyecto2.jpg" },
        { titulo: "Proyecto 3", descripcion: "Descripción del proyecto 3", imagen: "proyecto3.jpg" }
    ];

    const galeria = document.getElementById("galeria");

    proyectos.forEach(proyecto => {
        const div = document.createElement("div");
        div.classList.add("proyecto");

        const imagen = document.createElement("img");
        imagen.src = proyecto.imagen;
        imagen.alt = `Imagen de ${proyecto.titulo}`;

        const contenido = document.createElement("div");
        contenido.classList.add("contenido");

        const titulo = document.createElement("h2");
        titulo.textContent = proyecto.titulo;

        const descripcion = document.createElement("p");
        descripcion.textContent = proyecto.descripcion;

        contenido.appendChild(titulo);
        contenido.appendChild(descripcion);
        div.appendChild(imagen);
        div.appendChild(contenido);

        galeria.appendChild(div);
    });
});
