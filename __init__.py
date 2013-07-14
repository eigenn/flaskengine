from flask import Blueprint
from .index import IndexView
from .list import ModelList
from .edit import ModelEdit
from .create import ModelCreate
from .delete import ModelDelete

flaskengine_bp = Blueprint('flaskengine',
                           __name__,
                           static_folder='static',
                           static_url_path='/fe_static',
                           template_folder='templates',
                           )
