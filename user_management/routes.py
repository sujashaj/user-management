from flask import Blueprint, request, jsonify
from user_management.UserManager import UserManager

DB_FILE = "user_database.db"



class Routes:
    def __init(self):
        self.bp = Blueprint("routes", __name__)
        self.register_routes()
        self.user_manager = UserManager(DB_FILE)


    def home(self):
        return "Welcome to the User Management Application"

    def register_user(self):
        data = request.get_json()
        if data:
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")
        response = self.user_manager.register_user(username, email, password)
        return jsonify({"message": response}), 201

    def login(self):
        data = request.args
        username = data.get("username")
        password = data.get("password")
        response = self.user_manager.login(useranme, password)
        return jsonify({"meassage": response}), 200

    def register_routes(self):
        self.bp.add_url_rule("/", "home", self.home)
        self.bp.add_url_rule("/register_user", "register_user", self.register_user, methods=["POST"])
        self.bp.add_url_rule("/login", "login", self.login)




