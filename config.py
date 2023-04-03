SQLITE = 'sqlite:///project.db'
POSTGRESQL = 'postgresql+psycopg2://postgres:1234@localhost:5432/blog_db'

class Config:
    DEBUG = True
    SECRET_KEY = 'super-secret-key'

    SQLALCHEMY_DATABASE_URI = POSTGRESQL