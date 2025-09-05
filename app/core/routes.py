from flask import Blueprint, render_template

bp = Blueprint('core', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')

@bp.route('/weather')
def weather():
    return render_template('weather.html')