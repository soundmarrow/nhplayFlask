from flask import Flask
import application.db as db

# from flask_sqlalchemy import SQLAlchemy
# from flask_redis import FlaskRedis


# Globally accessible libraries
# db = SQLAlchemy()
# r = FlaskRedis()

# db = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server +
#                      ';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD=' + password + ';TrustServerCertificate=yes')
# cursor = cnxn.cursor()

# db = db()


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize Plugins
    # db.init_app(app)
    # r.init_app(app)

    with app.app_context():
        db.init_app(app)

        # Include our Routes
        from .gws.routes import gws_bp

        # Register Blueprints
        app.register_blueprint(gws_bp)

        return app
