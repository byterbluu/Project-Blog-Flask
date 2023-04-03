from blogapp import db

# CREAMOS LA TABLA DE USUARIOS

class User(db.Model):
    __tablename__ = 'users' #INIDICAMOS EL NOMBRE DE LA TABLA DE BASE DE DATOS
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    email = db.Column(db.String(120),nullable=True, unique=True)
    password = db.Column(db.Text, nullable=False)
    photo = db.Column(db.String(200))


# AGRAGAMOS UN CONSTRUCTOR DE LA CLASE

    def __init__(self, username, email, password, photo=None):
        self.username = username
        self.email = email
        self.password = password
        self.photo = photo

#  CREAMOS LA REPRESENTACION DE LA CLASE USUARIO

    def __repr__(self): 
        return f"User: '{self.username}'"  
    

#IMPORTAMMSO DATETIME PARA MEDIR LA FECHA
from datetime import datetime


# CREAMOS LA TABLA DE POSTS


class Post(db.Model):
    __tablename__ = 'posts' #INIDICAMOS EL NOMBRE DE LA TABLA DE BASE DE DATOS
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(100), nullable=False, unique=True)
    info = db.Column(db.Text)
    content = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    

    # CREAMOS UN CONSTRUCTOR DE LA CLASE
    def __init__(self, author, title, url, info, content) -> None:
        self.author = author
        self.title = title
        self.url = url
        self.info = info
        self.content = content

    # CREAMOS LA REPRESENTACION DE LA CLASE POST
    def __repr__(self): 
        return f"Post: {self.title}"
        