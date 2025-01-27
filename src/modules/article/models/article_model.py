from ....sqlite.database import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(500), nullable=True)
    tags = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f"<Article {self.titulo}>"
