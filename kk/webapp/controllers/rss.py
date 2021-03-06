import datetime
from os import path
from sqlalchemy import func
from flask import render_template, Blueprint

from webapp.models import db, Post, Tag, Reply, tags ,Course, Teacher , Student, Score, Task
from webapp.forms import ReplyForm submForm ReportForm


rss_blueprint = Blueprint(
    'rss',
    __name__,
    template_folder=path.join(path.pardir, 'templates', 'rss'),
    url_prefix='/rss'
)


def sidebar_data():
    recent = Post.query.order_by(Post.publish_date.desc()).limit(5).all()
    top_tags = db.session.query(
        Tag, func.count(tags.c.post_id).label('total')
    ).join(tags).group_by(Tag).order_by('total DESC').limit(5).all()

    return recent, top_tags

@rss_blueprint.route('/')
@rss_blueprint.route('/<int:page>')
def home(page = 1):
    posts = Post.query.order_by(Post.publish_date.desc()).paginate(page, 10)
    recent, top_tags = sidebar_data()

    return render_template(
        'home.html',
        posts=posts, 
        recent=recent, 
        top_tags=top_tags
    )

@rss_blueprint.route('/rss/<int:stu_id>')
def score(stu_id):
    scores = Score.query.filter(score.stu_id == stu_id).all()
    return render_template(
        'stu_score.html',
        scorses=scores
    )

@rss_blueprint.route('/rss/stu_task')
def stu_task():
    tasks = Task.query.order_by(Task.date.desc()).all()
    return render_template(
        'stu_task,html',
        ) 

@rss_blueprint.route('/rss/tea_task')
def tea_task():

    return render_template(
        'tea_task.html',
        )

@rss_blueprint.route('/rss/stu_subm')
def stu_subm():
    form = submForm()
    form = ReportForm()
    if form.validate_on_submit():
        
        f = form.Report.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(
            app.instance_path, 'reports', filename
        ))
        return redirect(url_for('index'))

    return render_template('stu_subm.html', form=form)
    if form.validate_on_submit():
        new_reply = Reply()
        new_reply.name = form.name.data
        new_reply.text = form.text.data 
        new_reply.post_id = post_id
        new_reply.date = datetime.datetime.now()
        db.session.add(new_reply)
        db.session.commit()



@rss_blueprint.route('/post/<int:post_id>', methods=('GET', 'POST'))
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


@rss_blueprint.route('/tag/<string:tag_name>')
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
