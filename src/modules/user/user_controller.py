from flask import Blueprint, g, request

from src.decorators.auth_middleware import class_decorator
from src.decorators.auth_session import token_required
from .user_service import UserService


@class_decorator(token_required)
class UserController:
    def __init__(self):
        self.user_service = UserService()
        self.user_bp = Blueprint("user", __name__)

        # Definición de rutas
        self.user_bp.route("/users", methods=["GET"])(self.list_users)
        self.user_bp.route("/users", methods=["POST"])(self.add_user)
        self.user_bp.route("/users/<int:user_id>", methods=["DELETE"])(self.delete_user)
        self.user_bp.route("/users/<int:user_id>", methods=["PUT"])(self.update_user)

    def find_user_by_id(self):
        return self.user_service.find_user_by_id(g.user_id)

    def list_users(self):
        return self.user_service.get_all_users()

    def add_user(self):
        return self.user_service.create_user(request.get_json())

    def delete_user(self, user_id):
        return self.user_service.delete_user(user_id)

    def update_user(self, user_id):
        return self.user_service.update_user(user_id, request.get_json())


# Instanciar el controlador
user_controller = UserController()
user_bp = user_controller.user_bp
