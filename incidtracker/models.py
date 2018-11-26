from datetime import datetime
from incidtracker import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Incident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_resolved = db.Column(db.DateTime, nullable=True)
    poc = db.Column(db.String(120), nullable=False)
    tag = db.Column(db.String(20), nullable=False)
    assignee = db.Column(db.String(20), db.ForeignKey('user.username'), nullable=False)

    def __repr__(self):
        return f"Incident('{self.category}', '{self.category}','{self.date_posted}'), '{self.poc}', '{self.assignee}'"