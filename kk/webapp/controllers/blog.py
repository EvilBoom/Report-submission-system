import datetime
from os import path
from sqlalchemy import func
from flask import render_template, Blueprint

from webapp.models import db, Post, Tag, Reply, tags
from webapp.forms import ReplyForm


blog_blueprint = Blueprint(
    'blog',
    __name__,
    template_folder=path.join(path.pardir, 'templates', 'blog'),
    url_prefix='/blog'
)


def sidebar_data():
    recent = Post.query.order_by(Post.publish_date.desc()).limit(5).all()
    top_tags = db.session.query(
        Tag, func.count(tags.c.post_id).label('total')
    ).join(tags).group_by(Tag).order_by('total DESC').limit(5).all()

    return recent, top_tags

@blog_blueprint.route('/')
@blog_blueprint.route('/<int:page>')
def home(page = 1):
    posts = Post.query.order_by(Post.publish_date.desc()).paginate(page, 10)
    recent, top_tags = sidebar_data()

    return render_template(
        'home.html',
        posts=posts, 
        recent=recent, 
        top_tags=top_tags
    )


@blog_blueprint.route('/post/<int:post_id>', methods=('GET', 'POST'))
def post(post_id):
    form = ReplyForm()
    if form.validate_on_submit():
        new_reply = Reply()
        new_reply.name = form.name.data
        new_reply.text = form.text.data 
        new_reply.post_id = post_id
        new_reply.date = datetime.datetime.now()
        db.session.add(new_reply)
        db.session.commit()

    post = Post.query.get_or_404(post_id)
    tags = post.tags
    replys = post.replys.order_by(Reply.date.desc()).all()
    recent, top_tags = sidebar_data()

    return render_template(
        'post.html', 
        post=post, 
        tags=tags, 
        replys=replys, 
        recent=recent, 
        top_tags=top_tags,
        form=form
    )


@blog_blueprint.route('/tag/<string:tag_name>')
def tag(tag_name):
    tag = Tag.query.filter_by(title=tag_name).first_or_404()
    posts = tag.post.order_by(Post.publish_date.desc()).all()
    recent, top_tags = sidebar_data()

    return render_template(
        'tag.html', 
        tag=tag, 
        posts=posts, 
        recent=recent, 
        top_tags=top_tags
    )


@blog_blueprint.route('/usr/<string:username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = user.posts.order_by(Post.publish_date.desc()).all()
    recent, top_tags = sidebar_data()
    return render_template(
        'user.html',
        user=user, 
        posts=posts,
        recent=recent, 
        top_tags=top_tags
    )

