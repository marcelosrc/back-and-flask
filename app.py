from flask import Flask
from routes.users import users_bp
from routes.posts import posts_bp

app = Flask(__name__)

if __name__ == "__main__":
    app.register_blueprint(users_bp)
    app.register_blueprint(posts_bp)
    app.run(debug=True)