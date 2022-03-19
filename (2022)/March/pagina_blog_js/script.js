// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022

document.addEventListener("DOMContentLoaded", function() {
    fetch("publicaciones.json")
        .then(response => response.json())
        .then(data => cargarPublicaciones(data))
        .catch(error => console.error("Error al cargar las publicaciones:", error));
});

function cargarPublicaciones(publicaciones) {
    const blog = document.getElementById("blog");
    
    publicaciones.forEach(publicacion => {
        const articulo = document.createElement("div");
        articulo.classList.add("publicacion");
        
        const titulo = document.createElement("h2");
        titulo.textContent = publicacion.titulo;
        
        const fecha = document.createElement("p");
        fecha.textContent = `Fecha: ${publicacion.fecha}`;
        
        const contenido = document.createElement("p");
        contenido.textContent = publicacion.contenido;

        articulo.appendChild(titulo);
        articulo.appendChild(fecha);
        articulo.appendChild(contenido);
        
        blog.appendChild(articulo);
    });
}
