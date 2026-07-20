from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class ChatMsgForm(FlaskForm):
    content = StringField("消息内容", validators=[DataRequired(message="消息不能为空")])
