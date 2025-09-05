from flask import Blueprint

bp = Blueprint('auth', __name__)

@bp.route('/login')
def login():
    return "Login page - Coming soon!"

@bp.route('/register')
def register():
    return "Register page - Coming soon!"