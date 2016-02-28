import sqlite3

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

app = Flask(__name__)
# look for all the uppercase values in the specified module.
# from_envar() may be used to load settings from the specified file
app.config.from_object(__name__)
