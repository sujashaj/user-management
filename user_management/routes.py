from flask import Flask
from routes.routes import bp as routes_bp  # Import the Blueprint

app = Flask(__name__)
app.register_blueprint(routes_bp)  # Register the Blueprint


if __name__ == "__main__":
    app.run(debug=True)