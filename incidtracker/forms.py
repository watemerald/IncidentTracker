from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from incidtracker.models import User, Incident


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    role = StringField('Role', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class IncidentForm(FlaskForm):
    category = SelectField(choices=['A','B','C'], validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    state = SelectField(choices=['A', 'B', 'C'], validators=[DataRequired()])
    poc = StringField('Email', validators=[DataRequired(), Email()])
    tag = StringField('Tag', validators=[DataRequired()])
    assignee = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Create')

    def validate_assignee(self, assignee):
        user = User.query.filter_by(username=assignee.data).first()
        if user:
            raise ValidationError('That assignee is not exist. Please choose a different one.')