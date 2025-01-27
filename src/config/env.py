import os


class EnvConfig:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///mydatabase.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
