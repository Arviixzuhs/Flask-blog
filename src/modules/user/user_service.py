from flask import jsonify
from .models.user_model import User
from ...sqlite.database import db
from .dto.user_dto import UserDTO


class UserService:
    def __init__(self):
        self.user_dto = UserDTO()

    def get_all_users(self):
        users = User.query.all()
        return jsonify(self.user_dto.dump(users, many=True)), 200

    def create_user(self, data):
        user = User(username=data["username"], email=data["email"])
        db.session.add(user)
        db.session.commit()
        return jsonify(self.user_dto.dump(user)), 201

    def delete_user(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return jsonify({"message": "User not found"}), 401

        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"}), 200

    def find_user_by_id(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return jsonify({"message": "User not found"}), 401

        return jsonify(self.user_dto.dump(user)), 200

    def update_user(self, user_id, data):
        user = User.query.get(user_id)
        if not user:
            return jsonify({"message": "User not found"}), 401

        user.username = data.get("username", user.username)
        user.email = data.get("email", user.email)
        db.session.commit()
        return jsonify(self.user_dto.dump(user)), 200
