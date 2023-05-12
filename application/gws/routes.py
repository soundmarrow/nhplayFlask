from flask import Blueprint


# Defining a blueprint
gws_bp = Blueprint(
    'gws_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@gws_bp.route('/gws')   # Focus here
def gws_home():
    return "Hello GWS!"
