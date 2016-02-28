import sqlite3

from contextlib import closing

from flask import (
    Flask, request, session, g, redirect,
    url_for, abort, render_template, flash
)

DATABASE = '/tmp/flaskr.db'
DEBUG = True
# TODO: replace with env var
SECRET_KEY = 'development_key'
USERNAME = 'admin'
PASSWORD = 'default_password'


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

app = Flask(__name__)
# look for all the uppercase values in the specified module.
# from_envar() may be used to load settings from the specified file
app.config.from_object(__name__)


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardon_requesT(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run()
