from app import app
from flask import render_template

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html.jinja')