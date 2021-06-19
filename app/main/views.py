from flask import render_template,request,redirect,url_for,abort
from ..request import get_quotes
from . import main
from flask_login import login_required
from ..models  import User

#Views
@main.route("/")
def index():
    '''
    View root page function that returns the index page and its data
    '''
    quotes = get_quotes()
    return render_template("index.html", quotes = quotes)