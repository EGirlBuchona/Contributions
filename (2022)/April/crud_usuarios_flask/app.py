# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: CRUD de Usuarios en Flask

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def conectar():
    return sqlite3.connect("database.db")

@app.route("/")
def index():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conexion.close()
    return render_template("index.html", usuarios=usuarios)

@app.route("/agregar", methods=["POST"])
def agregar():
    nombre = request.form["nombre"]
    email = request.form["email"]
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, email) VALUES (?, ?)", (nombre, email))
    conexion.commit()
    conexion.close()
    return redirect(url_for("index"))

@app.route("/editar/<int:id>")
def editar(id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
    usuario = cursor.fetchone()
    conexion.close()
    return render_template("editar.html", usuario=usuario)

@app.route("/actualizar/<int:id>", methods=["POST"])
def actualizar(id):
    nombre = request.form["nombre"]
    email = request.form["email"]
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("UPDATE usuarios SET nombre = ?, email = ? WHERE id = ?", (nombre, email, id))
    conexion.commit()
    conexion.close()
    return redirect(url_for("index"))

@app.route("/eliminar/<int:id>")
def eliminar(id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conexion.commit()
    conexion.close()
    return redirect(url_for("index"))

def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
    """)
    conexion.commit()
    conexion.close()

if __name__ == "__main__":
    crear_tabla()
    app.run(debug=True)
