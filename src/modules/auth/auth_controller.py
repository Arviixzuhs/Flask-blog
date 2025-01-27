from flask import Blueprint, request
from .auth_service import AuthService


class AuthController:
    def __init__(self):
        self.auth_service = AuthService()
        self.auth_bp = Blueprint("auth", __name__)

        # Definición de rutas
        self.auth_bp.route("/auth/login", methods=["POST"])(self.login)
        self.auth_bp.route("/auth/register", methods=["POST"])(self.register)

    def login(self):
        return self.auth_service.login(request.get_json())

    def register(self):
        return self.auth_service.register(request.get_json())


# Instanciar el controlador
auth_controller = AuthController()
auth_bp = auth_controller.auth_bp
