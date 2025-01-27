from .blog_controller import blog_bp


def blog_module(app):
    app.register_blueprint(blog_bp)
