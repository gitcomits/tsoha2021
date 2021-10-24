from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from onlinestudies.models import Users

class RegistrationForm(FlaskForm):
        username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
        email = StringField("Email", validators=[DataRequired(), Email()])
        rights = RadioField("User rights", choices=[("Teacher", 'I am a Teacher'), ("Student", "I am a Student")], default="Student")
        password = PasswordField("Password", validators=[DataRequired()])
        confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
        submit = SubmitField('Sign Up')

        def validate_username(self, username):
            user = Users.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username already taken!')

        def validate_email(self, email):
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already taken!')



class LoginForm(FlaskForm):
        email = StringField("Email", validators=[DataRequired(), Email()])
        password = PasswordField("Password", validators=[DataRequired()])
        remember = BooleanField('RememberMe')
        submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
        username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
        email = StringField("Email", validators=[DataRequired(), Email()])
        picture = FileField('Update profile picture', validators=[FileAllowed(['jpg','png'])])
        submit = SubmitField('Update')

        def validate_username(self, username):
            if username.data != current_user.username:
                user = Users.query.filter_by(username=username.data).first()
                if user:
                    raise ValidationError('Username already taken!')

        def validate_email(self, email):
            if email.data != current_user.email:
                user = Users.query.filter_by(email=email.data).first()
                if user:
                    raise ValidationError('Email already taken!')



class PostForm(FlaskForm):
    course_code = StringField('Course Code', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    question1 = TextAreaField('First Question', validators=[DataRequired()])
    answer1 = StringField('Correct answer', validators=[DataRequired()])
    question2 = TextAreaField('Second Question', validators=[DataRequired()])
    answer2 = StringField('Correct answer', validators=[DataRequired()])
    question3 = TextAreaField('Third Question', validators=[DataRequired()])
    answer3 = StringField('Correct answer', validators=[DataRequired()])
    submit = SubmitField('Post')



class QuizzAnswersForm(FlaskForm):
    answer1 = StringField('Answer1', validators=[DataRequired()])
    answer2 = StringField('Answer1', validators=[DataRequired()])
    answer3 = StringField('Answer1', validators=[DataRequired()])
    submit = SubmitField('Lock your answers')


