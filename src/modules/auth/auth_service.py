import bcrypt
import jwt
import datetime
from flask import jsonify, make_response
from ..user.models.user_model import User
from ...sqlite.database import db
import os

SECRET_KEY = os.getenv("JWT_SECRET")


class AuthService:
    # Función para generar hash de contraseña
    def hash_password(self, password):
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    # Función para verificar hash de contraseña
    def check_password(self, hashed_password, password):
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password)

    # Registro de usuario
    def register(self, data):
        hashed_password = self.hash_password(data["password"])
        user = User(
            username=data["username"], email=data["email"], password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User registered successfully"}), 201

    # Inicio de sesión de usuario
    def login(self, data):
        user = User.query.filter_by(email=data["email"]).first()

        if not user or not self.check_password(user.password, data["password"]):
            return make_response(
                jsonify({"message": "Invalid username or password"}), 401
            )

        # Generación del token JWT
        token = jwt.encode(
            {
                "user_id": user.id,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
            },
            SECRET_KEY,
            algorithm="HS256",
        )

        return jsonify({"message": "Login successful", "token": token}), 200
