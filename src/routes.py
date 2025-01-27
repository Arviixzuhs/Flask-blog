from .modules.blog.blog_module import blog_module
from .modules.auth.auth_module import auth_module
from .modules.user.user_module import user_module
from .modules.article.article_module import article_module


def register_routes(app):
    user_module(app)
    auth_module(app)
    blog_module(app)
    article_module(app)
