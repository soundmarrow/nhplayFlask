from flask_restx import Api

from .gws import api as gws
# Add namespaces here as needed thusly
# from .namespace2 import api as ns2
# from .namespaceX import api as nsX


# def create_app():
#     app = ...
#     # existing code omitted

#     from . import db
#     db.init_app(app)

#     return app


api = Api(
    title='NHPlay REST APIs',
    version='1.0',
    description='A description',
    # All API metadatas
)


api.add_namespace(gws)
# api.vars(db)
