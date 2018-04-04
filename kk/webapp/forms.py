from flask_wtf import Form  
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length


class ReplyForm(Form):
    name = StringField(
        'Name',
        validators=[DataRequired(), Length(max=255)]
    )
    text = TextAreaField(u'Reply', validators=[DataRequired()])


