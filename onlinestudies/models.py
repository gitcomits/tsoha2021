from datetime import datetime
from onlinestudies import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    rights = db.Column(db.String(20), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"Users('{self.username}', '{self.email}', '{self.rights}', '{self.image_file}', '{self.created_on}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    course_code = db.Column(db.String(7), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}', '{self.course_code}')"



class Quizz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String(7), nullable=False)
    question1 = db.Column(db.String(100), nullable=False)
    answer1 = db.Column(db.String(20), nullable=False)
    question2 = db.Column(db.String(100), nullable=False)
    answer2 = db.Column(db.String(20), nullable=False)
    question3 = db.Column(db.String(100), nullable=False)
    answer3 = db.Column(db.String(20), nullable=False)


#class Enroll(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    course_code = db.Column(db.String(7), nullable=False)
#    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)



class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    tq_id = db.Column(db.Text, nullable=False)
    rq_id = db.Column(db.Text, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"Course('{self.title}', '{self.user_id}', '{self.created_on}')"


    db.create_all()
    db.session.commit()
