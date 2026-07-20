from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField

class AudioEditForm(FlaskForm):
    title = StringField("音频标题")
    category = StringField("音频分类")
    is_vip = BooleanField("会员专属")
    is_show = BooleanField("前台展示")
