from flask import render_template
from . import main
from app import create_app

@main.route('/')
def index():
    title = 'Home - Welcome to Pitch App'
    return render_template('index.html')
