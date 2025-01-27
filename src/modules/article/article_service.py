from flask import jsonify
from .models.article_model import Article
from ...sqlite.database import db
from .dto.article_dto import ArticleDTO


class ArticleService:
    def __init__(self):
        self.article_dto = ArticleDTO()

    def get_all_articles(self):
        articles = Article.query.all()
        return jsonify(self.article_dto.dump(articles, many=True)), 200

    def create_article(self, data):
        article = Article(
            title=data["title"],
            description=data["description"],
            image=data.get("image", ""),
            tags=data.get("tags", ""),
        )
        db.session.add(article)
        db.session.commit()
        return jsonify(self.article_dto.dump(article)), 201

    def delete_article(self, article_id):
        article = Article.query.get(article_id)
        if not article:
            return jsonify({"message": "Article not found"}), 404

        db.session.delete(article)
        db.session.commit()
        return jsonify({"message": "Article deleted successfully"}), 200

    def find_article_by_id(self, article_id):
        article = Article.query.get(article_id)
        if not article:
            return jsonify({"message": "Article not found"}), 404

        return jsonify(self.article_dto.dump(article)), 200

    def update_article(self, article_id, data):
        article = Article.query.get(article_id)
        if not article:
            return jsonify({"message": "Article not found"}), 404

        article.title = data.get("title", article.title)
        article.description = data.get("description", article.description)
        article.image = data.get("image", article.image)
        article.tags = data.get("tags", article.tags)
        db.session.commit()
        return jsonify(self.article_dto.dump(article)), 200
