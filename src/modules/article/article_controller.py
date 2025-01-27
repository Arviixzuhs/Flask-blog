from flask import Blueprint, request
from .article_service import ArticleService


class ArticleController:
    def __init__(self):
        self.article_service = ArticleService()
        self.article_bp = Blueprint("article", __name__)

        self.article_bp.route("/articles", methods=["GET"])(self.list_articles)
        self.article_bp.route("/articles", methods=["POST"])(self.add_article)
        self.article_bp.route("/articles/<int:article_id>", methods=["DELETE"])(
            self.delete_article
        )
        self.article_bp.route("/articles/<int:article_id>", methods=["PUT"])(
            self.update_article
        )

    def list_articles(self):
        return self.article_service.get_all_articles()

    def add_article(self):
        return self.article_service.create_article(request.get_json())

    def delete_article(self, article_id):
        return self.article_service.delete_article(article_id)

    def update_article(self, article_id):
        return self.article_service.update_article(article_id, request.get_json())


article_controller = ArticleController()
article_bp = article_controller.article_bp
