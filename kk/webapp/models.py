from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


tags = db.Table(
    'post_tags', 
    db.Column('post_id',db.Integer, db.ForeignKey('post.id')), 
    db.Column('tag_id',db.Integer, db.ForeignKey('tag.id'))
)

stu_crse = db.Table(
    'student_course',
    db.Column('student_id',db.Integer, db.ForeignKey('student.id')), 
    db.Column('course_id',db.Integer, db.ForeignKey('course.id'))
)

tch_crse = db.Table(
    'teacher_course',
    db.Column('teacher_id',db.Integer, db.ForeignKey('teacher.id')), 
    db.Column('course_id',db.Integer, db.ForeignKey('course.id'))
)

tch_stu = db.Table(
   'teacher_student',
    db.Column('teacher_id',db.Integer, db.ForeignKey('teacher.id')), 
    db.Column('student_id',db.Integer, db.ForeignKey('student.id')) 
)


class Tag(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return "<Tag '{}'>".format(self.title)


class Teacher(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    teacher_name = db.Column(db.String(255))
    password = db.Column(db.String(255))

    posts = db.relationship(
        'Post', 
        backref='teacher',
        lazy='dynamic'
    )
    tch_crse = db.relationship(
        'Course',
        secondary = tch_crse,
        backref=db.backref('crse_tch', lazy='dynamic')
    )
    tch_stu = db.relationship(
        'Student',
        secondary = tch_stu,
        backref=db.backref('stu_tch', lazy='dynamic')
    )

    def __init__(self, teacher_name):
        self.teacher_name = teacher_name

    def __repr__(self):
        return "<Teacher '{}'>".format(self.teacher_name)


class Course(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    course_name =  db.Column(db.String(255))

    def __init__(self, course_name):
        self.course_name = course_name

    def __repr__(self):
        return "<Course '{}'>".format(self.course_name)

class Student(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    student_name = db.Column(db.String(255))
    password = db.Column(db.String(255))

    posts = db.relationship(
        'Post', 
        backref='student',
        lazy='dynamic'
    )
    stu_crse = db.relationship(
        'Course',
        secondary = stu_crse,
        backref=db.backref('crse_stu', lazy='dynamic')
    )

    def __init__(self, student_name):
        self.student_name = student_name

    def __repr__(self):
        return "<Student '{}'>".format(self.student_name)


class Post(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    title = db.Column(db.String(255))
    publish_date = db.Column(db.DateTime())
    address = db.Column(db.String(255))
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

    reply = db.relationship(
        'Reply',
        uselist=False,
        backref='post'
    )
    tags = db.relationship(
        'Tag',
        secondary=tags,
        backref=db.backref('posts', lazy='dynamic')
    )

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return "<Post '{}'>".format(self.title)


class Reply(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())
    post_id = db.Column(db.Integer(), db.ForeignKey('post.id'))

    def __repr__(self):
        return "<Reply '{}'>".format(self.text[:15])