from flask import render_template
from app import webapp


@webapp.route('/')
@webapp.route('/index')
def index():
    return render_template("index.html")
