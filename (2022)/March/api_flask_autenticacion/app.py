# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: API Flask con Autenticación JWT en Python

from flask import Flask, jsonify, request
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mi_secreto'

# Decorador para verificar el token de autenticación
def token_requerido(f):
    @wraps(f)
    def decorador(*args, **kwargs):
        token = request.headers.get('x-access-token')
        if not token:
            return jsonify({'mensaje': 'Token es necesario'}), 403
        try:
            datos = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            usuario_actual = datos['usuario']
        except:
            return jsonify({'mensaje': 'Token inválido'}), 403
        return f(usuario_actual, *args, **kwargs)
    return decorador

# Ruta de inicio de sesión para generar un token
@app.route('/login', methods=['POST'])
def login():
    datos = request.get_json()
    usuario = datos.get('usuario')
    contraseña = datos.get('contraseña')

    if usuario == 'admin' and contraseña == '1234':
        token = jwt.encode({
            'usuario': usuario,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({'token': token})

    return jsonify({'mensaje': 'Credenciales inválidas'}), 401

# Ruta protegida que requiere autenticación
@app.route('/protegido', methods=['GET'])
@token_requerido
def protegido(usuario_actual):
    return jsonify({'mensaje': f'Bienvenido, {usuario_actual}. Acceso concedido.'})

if __name__ == '__main__':
    app.run(debug=True)
