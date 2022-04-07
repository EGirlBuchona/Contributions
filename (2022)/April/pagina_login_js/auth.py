# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Autenticación para Página de Login

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def verificar_usuario(username, password):
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, password))
    resultado = cursor.fetchone()
    conexion.close()
    return resultado is not None

@app.route("/auth", methods=["POST"])
def autenticar():
    datos = request.get_json()
    username = datos["username"]
    password = datos["password"]
    
    if verificar_usuario(username, password):
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})

if __name__ == "__main__":
    app.run(debug=True)
