from flask import Flask
from routes.routes import Routes


app = Flask(__name__)
routes = Routes()
app.register_blueprint(routes.bp)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
