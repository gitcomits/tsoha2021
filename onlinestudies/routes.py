import os
import secrets
from PIL import Image
from flask import redirect, render_template, request, url_for, flash, request

from onlinestudies import app, db, bcrypt
from onlinestudies.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, QuizzAnswersForm
from onlinestudies.models import Users, Post, Quizz, QuizzAnswers
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
def home():
    posts = Post.query.all()
    return render_template("home.html", posts=posts)


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





def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn



@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('your account has been updated', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)

@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, course_code=form.course_code.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        quizz = Quizz(course_code=form.course_code.data, question1=form.question1.data, answer1=form.answer1.data
        , question2=form.question2.data, answer2=form.answer2.data, question3=form.question3.data, answer3=form.answer3.data)
        db.session.add(quizz)
        db.session.commit()
        flash('New course has been created!', 'sucess')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post', form=form, legend='New post')


@app.route("/quizz/<int:post_id>", methods=['GET', 'POST'])
def quizz(post_id):
    quizz = Quizz.query.get_or_404(post_id)
    form = QuizzAnswersForm()
    if form.validate_on_submit():
        answers = QuizzAnswers(course_code=quizz.course_code,answer1=form.answer1.data,answer2=form.answer2.data,answer3=form.answer3.data,points=3,user_id=current_user)
#        db.session.add(answers)
#        db.session.commit()
        return render_template('quizz.html', title='Quizz',form=form, quizz=quizz, d='disabled', a1=quizz.answer1)
    return render_template('quizz.html', title='Quizz',form=form, quizz=quizz)


@app.route("/post/<int:post_id>")
def post(post_id):

    post = Post.query.get_or_404(post_id)
    quizz = Quizz.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post, quizz=quizz)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    quizz = Quizz.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.course_code = form.course_code.data
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        quizz.course_code=form.course_code.data
        quizz.question1=form.question1.data
        quizz.answer1=form.answer1.data
        quizz.question2=form.question2.data
        quizz.answer2=form.answer2.data
        quizz.question3=form.question3.data
        quizz.answer3=form.answer3.data
        db.session.commit()
        flash('The course has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.course_code.data = post.course_code
        form.title.data = post.title
        form.content.data = post.content
        form.question1.data = quizz.question1
        form.answer1.data = quizz.answer1
        form.question2.data = quizz.question2
        form.answer2.data = quizz.answer2
        form.question3.data = quizz.question3
        form.answer3.data = quizz.answer3
    return render_template('create_post.html', title="Update Post", form=form, legend='Update post')


@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('The course has been deleted!', 'success')
    return redirect(url_for('home'))

#@app.route("/post/<int:post_id>/quizz_done", methods=['POST'])
#@login_required
#def post_answers(post_id):
#    post = Post.query.get_or_404(post_id)
#    if post.author != current_user:
#        abort(403)
#    db.session.delete(post)
#    db.session.commit()
#    flash('The course has been deleted!', 'success')
#    return redirect(url_for('home'))





@app.route("/post/<int:post_id>/", methods=['GET', 'POST'])
@login_required
#def enroll(post_id,cc):
def enroll():
    postId  = request.args.get(post_id, None)
    cc  = request.args.get('cc', None)
    enroll = Enroll(course_code=cc)
    db.session.add(enroll)
    db.session.commit()
    return render_template('create_post.html', title="Update Post", form=form, legend='Update post')




@app.errorhandler(403)
def page_not_found(e):
    return render_template('403.html'), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(405)
def page_not_found(e):
    return render_template('405.html'), 405
