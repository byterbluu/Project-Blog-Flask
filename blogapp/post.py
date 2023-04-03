from flask import Blueprint

bp = Blueprint('post', __name__, url_prefix='/post')


@bp.route('/posts')
def posts():
    return 'Pagina de Posts'


@bp.route('/create')
def create():
    return 'Pagina de create post'

@bp.route('/update')
def update():
    return 'Pagina de update'