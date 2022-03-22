# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: API Avanzada en Flask

from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Datos de ejemplo
productos = [
    {"id": 1, "nombre": "Laptop", "precio": 1200},
    {"id": 2, "nombre": "Cámara", "precio": 600},
    {"id": 3, "nombre": "Teléfono", "precio": 800}
]

# Manejo de errores personalizado
@app.errorhandler(404)
def recurso_no_encontrado(error):
    return jsonify({"error": "Recurso no encontrado"}), 404

@app.errorhandler(400)
def solicitud_invalida(error):
    return jsonify({"error": "Solicitud inválida"}), 400

# Ruta para obtener todos los productos
@app.route("/api/productos", methods=["GET"])
def obtener_productos():
    return jsonify(productos)

# Ruta para obtener un producto específico por ID
@app.route("/api/productos/<int:id>", methods=["GET"])
def obtener_producto(id):
    producto = next((p for p in productos if p["id"] == id), None)
    if producto is None:
        abort(404)
    return jsonify(producto)

# Ruta para crear un nuevo producto
@app.route("/api/productos", methods=["POST"])
def crear_producto():
    if not request.json or "nombre" not in request.json or "precio" not in request.json:
        abort(400)
    nuevo_producto = {
        "id": productos[-1]["id"] + 1 if productos else 1,
        "nombre": request.json["nombre"],
        "precio": request.json["precio"]
    }
    productos.append(nuevo_producto)
    return jsonify(nuevo_producto), 201

# Ruta para actualizar un producto existente
@app.route("/api/productos/<int:id>", methods=["PUT"])
def actualizar_producto(id):
    producto = next((p for p in productos if p["id"] == id), None)
    if producto is None:
        abort(404)
    if not request.json:
        abort(400)
    producto["nombre"] = request.json.get("nombre", producto["nombre"])
    producto["precio"] = request.json.get("precio", producto["precio"])
    return jsonify(producto)

# Ruta para eliminar un producto
@app.route("/api/productos/<int:id>", methods=["DELETE"])
def eliminar_producto(id):
    producto = next((p for p in productos if p["id"] == id), None)
    if producto is None:
        abort(404)
    productos.remove(producto)
    return jsonify({"mensaje": "Producto eliminado"})

if __name__ == "__main__":
    app.run(debug=True)
