from flask import Blueprint


class Routes:
    def __init(self):
        self.bp = Blueprint("routes", __name__)
        self.register_routes()


@bp.route("/")
    def home(self):
    return "Welcome to Flask App!"
    def about(self):
        return "This is the about page."

    def register_routes(self):
        self.bp.add_url_rule("/", "home", self.home)
        self.bp.add_url_rule("/about", "about", self.about)



@bp.route("/about")
def about()
     return "This is the about page."

