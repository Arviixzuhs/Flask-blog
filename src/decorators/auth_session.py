from functools import wraps
from flask import request, jsonify, g
import jwt
import os

SECRET_KEY = os.getenv("JWT_SECRET")


# Middleware para verificar el token JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Verificar si el token JWT se encuentra en los encabezados de la solicitud
        if "Authorization" in request.headers:
            auth_header = request.headers["Authorization"]
            # Comprobar que el encabezado tenga el formato correcto
            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]  # El token viene después de 'Bearer '

        if not token:
            return jsonify({"message": "Token is missing!"}), 401

        try:
            # Intentar decodificar el token usando la clave secreta
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            g.user_id = decoded_token.get("user_id")  # Almacenar user_id en g
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token!"}), 401

        return f(*args, **kwargs)

    return decorated
