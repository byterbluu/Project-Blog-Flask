from flask import Blueprint, request, flash, redirect, url_for, g, render_template
from .auth import login_required
from .models import Post
from blogapp import db

bp = Blueprint('post', __name__, url_prefix='/post')


@bp.route('/posts')
@login_required
def posts():
    posts = Post.query.all()
    return render_template('admin/posts.html', posts=posts)


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        url = request.form.get('url')
        url = url.replace(' ', '-')
        title = request.form.get('title')
        info = request.form.get('info')
        content = request.form.get('ckeditor')

        post = Post(g.user.id, url, title, info, content)

        error = None

        #comparamos url existentes

        post_url = Post.query.filter_by(url = url).first()
        if post_url == None:
            db.session.add(post)
            db.session.commit()
            flash(f'El blog {post.title} se ha creado correctamente')
            return redirect(url_for('post.posts'))
        else:
            error = f'El blog {url} ya esta registrado'
        flash(error)    
            

    return render_template('admin/create.html')

@bp.route('/update')
@login_required
def update():
    return 'Pagina de update'