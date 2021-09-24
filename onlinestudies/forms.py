from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField
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


#class UploadCourseForm(FlaskForm):
#        title = StringField("Title", validators=[DataRequired(), Length(min=7, max=100)])
#        content = StringField("The course text", validators=[DataRequired(), Length(min=100, max=2000)])
#        submit = SubmitField('Submit the course')
