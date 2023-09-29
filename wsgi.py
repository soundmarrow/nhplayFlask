# app = Flask(__name__)
# app.run(debug=True)


from flask import Flask
# from flask_restx import Api
from apis import api
from core import db

# api = Api()

# app = Flask(__name__)
# api.init_app(app)


def create_app():
    app = Flask(__name__)
    api.init_app(app)

    with app.app_context():
        # db.get_db()
        db.init_app(app)

    return app

# from application import create_app

# app = create_app()
# if __name__ == "__main__":
#     app.run(host='0.0.0.0')
