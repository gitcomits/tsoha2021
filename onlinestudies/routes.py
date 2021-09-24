from flask import redirect, render_template, request, url_for, flash, request
from onlinestudies import app, db, bcrypt
from onlinestudies.forms import RegistrationForm, LoginForm
from onlinestudies.models import Users, Post
from flask_login import login_user, current_user, logout_user, login_required


title = "one time post"

@app.route("/")
def home():
    return render_template("home.html", title=title)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsecsesfull', 'danger')
    return render_template("login.html", title="Login", form=form)




@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users(username=form.username.data, email=form.email.data, rights=form.rights.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in!', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title="Register", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
def account():
    return render_template("account.html")



@app.route("/upload", methods=['GET', 'POST'])
def upload():
    form = UploadCourseForm()
    return render_template("upload.html", title="Upload Courses")
