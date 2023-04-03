from flask import Blueprint, render_template, url_for, redirect, request, flash, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from blogapp import db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        user = User(username, email, generate_password_hash(password))

        #VALIDACION DE DATOS 
        error = None
   
        #COMPARAMOS LOS NOMBRES DE USUARIOS CON LOS EXISTENTES
        user_email = User.query.filter_by(email=email).first()
        if user_email == None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            error = f'El email: {email} ya esta registrado'
        flash(error)
    return render_template('auth/register.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        error = None
        user = User.query.filter_by(email=email).first()

        if user == None or not check_password_hash(user.password, password):
            error = 'Email o contraseña incorrectos'
        
        #INICIANDO SESION
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('post.posts'))
        flash(error)

    return render_template('auth/login.html')


#CON ESTO MANTENEMOS LA SESION ACTIVA EN TODAS LAS VISTAS
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get_or_404(user_id)    

#CREAMOS UN LOGOUT
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home.index'))

import functools

#PEDIMOS EL INICIO DE SESION OBLIGATORIO EN CIERTAS VISTAS
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view

@bp.route('/profile')
def profile():
    return 'Pagina de profile'