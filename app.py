from flask import Flask
from routes.routes import bp as routes_bp# Import the Blueprint
from routes.routes import Routes


app = Flask(__name__)
app.register_blueprint(routes_bp)  # Register the Blueprint
routes = Routes()
app.register_blueprint(routes.bp)



if __name__ == "__main__":
    app.run(debug=True)