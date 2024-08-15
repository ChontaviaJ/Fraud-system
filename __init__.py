from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'  # Ensure this is securely generated

    with app.app_context():
        from . import routes
        app.register_blueprint(routes.bp)

    return app
