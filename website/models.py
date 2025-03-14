from . import db
from flask_login import UserMixin
from datetime import datetime
import uuid

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_admin = db.Column(db.Boolean, default=False)
    blocked = db.Column(db.Boolean, default=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    followed_posts = db.relationship('Post', secondary='post_follow', backref='followers')

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(500), nullable=True)
    flow = db.Column(db.String(50), nullable=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    slug = db.Column(db.String(50), unique=True, default=str(uuid.uuid4())[:8])

    def __repr__(self):
        return f'<Post {self.title}> by {self.author.username}'

class PostFollow(db.Model):
    __tablename__ = 'post_follow'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Thêm unique constraint để đảm bảo một user không thể follow một bài viết nhiều lần
    __table_args__ = (db.UniqueConstraint('user_id', 'post_id', name='unique_user_post_follow'),)