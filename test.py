import datetime

import flask
from flask_sqlalchemy import SQLAlchemy


app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text)
    created_date = db.Column(db.DateTime, default=datetime.date.today())


post = Post()
post.name = 'name '
post.text = 'text'
db.session.add(post)
print(post.id)