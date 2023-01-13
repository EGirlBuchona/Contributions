from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = "your_secret_key"  # Cambia esta clave para producción


# ** Inicialización de la base de datos **
def init_db():
    with sqlite3.connect("blog.db") as conn:
        cursor = conn.cursor()
        # Tabla de usuarios
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )''')
        # Tabla de publicaciones
        cursor.execute('''CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )''')


# ** Página principal: Mostrar publicaciones **
@app.route("/")
def index():
    with sqlite3.connect("blog.db") as conn:
        cursor = conn.cursor()
        posts = cursor.execute("SELECT * FROM posts ORDER BY date_created DESC").fetchall()
    return render_template("index.html", posts=posts)


# ** Registro de usuario **
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        try:
            with sqlite3.connect("blog.db") as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                conn.commit()
            flash("User registered successfully!", "success")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("Username already exists.", "danger")
    return render_template("register.html")


# ** Login de usuario **
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        with sqlite3.connect("blog.db") as conn:
            cursor = conn.cursor()
            user = cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password)).fetchone()
            if user:
                session["user_id"] = user[0]
                flash("Logged in successfully!", "success")
                return redirect(url_for("index"))
            else:
                flash("Invalid username or password.", "danger")
    return render_template("login.html")

# ** Registro de usuario **
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        # Validar que las contraseñas coincidan
        if password != confirm_password:
            flash("Passwords do not match!", "danger")
            return redirect(url_for("register"))

        # Conectar con la base de datos
        with sqlite3.connect("blog.db") as conn:
            cursor = conn.cursor()
            
            # Verificar si el usuario ya existe
            cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            if cursor.fetchone():
                flash("Username already exists!", "danger")
                return redirect(url_for("register"))

            # Insertar el nuevo usuario
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            flash("User registered successfully!", "success")
            return redirect(url_for("login"))

    return render_template("register.html")


# ** Cerrar sesión **
@app.route("/logout")
def logout():
    session.pop("user_id", None)
    flash("Logged out successfully.", "info")
    return redirect(url_for("index"))


# ** Crear publicación **
@app.route("/create", methods=["GET", "POST"])
def create_post():
    if "user_id" not in session:
        flash("Please log in to create a post.", "warning")
        return redirect(url_for("login"))

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        with sqlite3.connect("blog.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
            conn.commit()
        flash("Post created successfully!", "success")
        return redirect(url_for("index"))
    return render_template("create_post.html")


# ** Editar publicación **
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_post(id):
    if "user_id" not in session:
        flash("Please log in to edit a post.", "warning")
        return redirect(url_for("login"))

    with sqlite3.connect("blog.db") as conn:
        cursor = conn.cursor()
        post = cursor.execute("SELECT * FROM posts WHERE id = ?", (id,)).fetchone()

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        with sqlite3.connect("blog.db") as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE posts SET title = ?, content = ? WHERE id = ?", (title, content, id))
            conn.commit()
        flash("Post updated successfully!", "success")
        return redirect(url_for("index"))
    return render_template("edit_post.html", post=post)


# ** Eliminar publicación **
@app.route("/delete/<int:id>", methods=["POST"])
def delete_post(id):
    if "user_id" not in session:
        flash("Please log in to delete a post.", "warning")
        return redirect(url_for("login"))

    with sqlite3.connect("blog.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM posts WHERE id = ?", (id,))
        conn.commit()
    flash("Post deleted successfully!", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
