from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField

class VoiceDemandForm(FlaskForm):
    demand_text = TextAreaField("定制需求描述")
