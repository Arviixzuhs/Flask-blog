from .user_controller import user_bp


def user_module(app):
    app.register_blueprint(user_bp)
