from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import flask.ext.whooshalchemy as whooshalchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///post.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['WHOOSH_BASE'] = 'whoosh'
DEFAULT_WHOOSH_INDEX_NAME = 'whoosh_index'

db = SQLAlchemy(app)


class Post(db.Model):
    __searchable__ = ['title', 'content']

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(1000))

whooshalchemy.whoosh_index(app, Post)


@app.route('/')
def index():
    return render_template('index1.html')

app.route('/add')


def add():
    if request.method == 'POST':
        post = Post(title=request.form['title'],
                    content=request.form['content'])
        db, session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.hml')


if __name__ == '__main__':
    app.run(debug=True)
