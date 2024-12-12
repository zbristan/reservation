from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email

class ReservationForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "eg. john@gmail.com"})
    date = DateField('Reservation Date', format='%Y-%m-%d', validators=[DataRequired()])
    time = TimeField('Reservation Time', format='%H:%M', validators=[DataRequired()])
    party_size = IntegerField('Party Size', validators=[DataRequired()])
    submit = SubmitField('Reserve')