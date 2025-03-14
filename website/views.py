from flask import Blueprint, render_template, request
from flask_login import current_user
from .models import Post

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html', user=current_user)

@views.route('/flow/<string:flow_type>')
def flow_posts(flow_type):
    page = request.args.get('page', 1, type=int)
    per_page = 10
    posts = Post.query.filter_by(flow=flow_type).order_by(Post.updated_at.desc()).paginate(page=page, per_page=per_page, error_out=False)
    return render_template('flow_posts.html', user=current_user, posts=posts, flow_type=flow_type)

