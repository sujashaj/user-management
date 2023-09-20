from flask import Blueprint


bp = Blueprint("routes", __name__)

@bp.route("/")
def home():
    return "Welcome to Flask App!"



@bp.route("/about")
def about()
     return "This is the about page."
