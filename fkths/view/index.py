from fkths import app
from trex.flask import render_html
from flask import Blueprint

blueprint = Blueprint('index', __name__)

@blueprint.route('/')
@render_html()
def index():
    """
    We can't stop here, this is bat country
    """
    return {}

app.register_blueprint(blueprint)