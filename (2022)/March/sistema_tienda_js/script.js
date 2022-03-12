// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022

let carrito = [];
let total = 0;

function agregarAlCarrito(nombre, precio) {
    carrito.push({ nombre, precio });
    total += precio;
    actualizarCarrito();
}

function actualizarCarrito() {
    const listaCarrito = document.getElementById("lista-carrito");
    const totalElemento = document.getElementById("total");

    // Limpiar el carrito antes de actualizar
    listaCarrito.innerHTML = "";

    // Mostrar cada elemento en el carrito
    carrito.forEach((producto, index) => {
        const item = document.createElement("li");
        item.textContent = `${producto.nombre} - $${producto.precio}`;
        const botonEliminar = document.createElement("button");
        botonEliminar.textContent = "Eliminar";
        botonEliminar.onclick = () => eliminarDelCarrito(index);
        item.appendChild(botonEliminar);
        listaCarrito.appendChild(item);
    });

    // Actualizar el total
    totalElemento.textContent = total.toFixed(2);
}

function eliminarDelCarrito(indice) {
    total -= carrito[indice].precio;
    carrito.splice(indice, 1);
    actualizarCarrito();
}
