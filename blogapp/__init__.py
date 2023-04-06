from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor

db = SQLAlchemy()  #Instancia de sql alchemy




def create_app():
    # Creacion y configuracion de la app
    
    app = Flask(__name__)

    app.config.from_object('config.Config')
    
    db.init_app(app) #INICIALIZAMOS LA BASE DE DATOS

    # CKEditor
    ckeditor = CKEditor(app)

    # CHANGE IDIOM
    import locale
    locale.setlocale(locale.LC_ALL, 'es_ES')

    # REGISTER VIEW
    from blogapp import home
    app.register_blueprint(home.bp)

    from blogapp import auth
    app.register_blueprint(auth.bp)

    from blogapp import post
    app.register_blueprint(post.bp)

    #IMPORTAMOS LOS MODELOS DE LA BASE DE DATOS
    from .models import User, Post

    #MIGRACION DE MANERA AUTOMATICA
    with app.app_context():
        db.create_all()


    return app