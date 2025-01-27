from .auth_controller import auth_bp


def auth_module(app):
    app.register_blueprint(auth_bp)
