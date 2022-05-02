# API with JWT Authentication in Flask

This project is an API created with Flask that implements authentication using JWT (JSON Web Tokens). The API allows users to authenticate with credentials and receive a token to access protected endpoints.

## Instructions

1. Install Flask and PyJWT if not already installed:
   ```bash
   pip install Flask PyJWT
   ```

2. Run `app.py` to start the API server:
   ```bash
   python app.py
   ```

3. Authenticate with the `/login` endpoint by sending a POST request with:
   ```json
   {
       "usuario": "admin",
       "contraseña": "1234"
   }
   ```

4. Use the received token in the `x-access-token` header to access the protected endpoint `/protegido`.

## Dependencies
- Flask
- PyJWT
```


```markdown
# API con Autenticación JWT en Flask

Este proyecto es una API creada con Flask que implementa autenticación mediante JWT (JSON Web Tokens). La API permite que los usuarios se autentiquen con credenciales y reciban un token para acceder a los endpoints protegidos.

## Instrucciones

1. Instale Flask y PyJWT si aún no están instalados:
   ```bash
   pip install Flask PyJWT
   ```

2. Ejecute `app.py` para iniciar el servidor de la API:
   ```bash
   python app.py
   ```

3. Autentíquese con el endpoint `/login` enviando una solicitud POST con:
   ```json
   {
       "usuario": "admin",
       "contraseña": "1234"
   }
   ```

4. Use el token recibido en el header `x-access-token` para acceder al endpoint protegido `/protegido`.

## Dependencias
- Flask
- PyJWT


