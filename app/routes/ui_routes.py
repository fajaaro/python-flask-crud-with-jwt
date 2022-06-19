from flask import Blueprint, render_template

ui = Blueprint('ui', __name__)

@ui.route('/')
def index():
    return render_template('index.html')

@ui.route('/about')
def about():
    return render_template('about.html')

@ui.route('/person/<person_name>')
def person(person_name):
    return render_template('person.html', person_name = person_name)