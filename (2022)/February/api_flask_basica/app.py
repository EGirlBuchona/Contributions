# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: API Básica en Flask para Gestión de Tareas

from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de tareas de ejemplo
tareas = [
    {"id": 1, "titulo": "Aprender Flask", "completado": False},
    {"id": 2, "titulo": "Crear una API", "completado": False}
]

# Obtener todas las tareas
@app.route('/tareas', methods=['GET'])
def obtener_tareas():
    return jsonify(tareas)

# Obtener una tarea por ID
@app.route('/tareas/<int:tarea_id>', methods=['GET'])
def obtener_tarea(tarea_id):
    tarea = next((t for t in tareas if t["id"] == tarea_id), None)
    return jsonify(tarea) if tarea else (jsonify({"error": "Tarea no encontrada"}), 404)

# Crear una nueva tarea
@app.route('/tareas', methods=['POST'])
def crear_tarea():
    nueva_tarea = {
        "id": tareas[-1]["id"] + 1 if tareas else 1,
        "titulo": request.json.get("titulo"),
        "completado": False
    }
    tareas.append(nueva_tarea)
    return jsonify(nueva_tarea), 201

# Actualizar una tarea existente
@app.route('/tareas/<int:tarea_id>', methods=['PUT'])
def actualizar_tarea(tarea_id):
    tarea = next((t for t in tareas if t["id"] == tarea_id), None)
    if tarea:
        tarea["titulo"] = request.json.get("titulo", tarea["titulo"])
        tarea["completado"] = request.json.get("completado", tarea["completado"])
        return jsonify(tarea)
    else:
        return jsonify({"error": "Tarea no encontrada"}), 404

# Eliminar una tarea
@app.route('/tareas/<int:tarea_id>', methods=['DELETE'])
def eliminar_tarea(tarea_id):
    global tareas
    tareas = [t for t in tareas if t["id"] != tarea_id]
    return jsonify({"mensaje": "Tarea eliminada exitosamente"})

if __name__ == '__main__':
    app.run(debug=True)
