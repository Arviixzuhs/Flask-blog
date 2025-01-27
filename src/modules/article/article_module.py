from .article_controller import article_bp


def article_module(app):
    app.register_blueprint(article_bp)
