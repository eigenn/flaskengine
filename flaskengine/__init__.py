'''
	Base Usage Case.

	from flask import Flask
	from flaskengine import flaskengine_bp


	app = Flask(__name__)
	#Register The Blueprint to use the templates and static files for the flaskengine app
	app.register_blueprint(flaskengine_bp)

	from google.appengine.ext import ndb

	class SomeModel(ndb.Model):
		entity_1 = ndb.StringProperty()
		entity_2 = ndb.StringProperty()


	# Lets generate some view's
	from flaskengine import IndexView, ModelList, ModelDelete, ModelEdit, ModelCreate
	from flask import Blueprint


	example_bp = Blueprint('example', __name__)

	# Generate a index view that will extend the base template.
	class ExampleIndex(IndexView):
		include = 'template_to_include_in.html'

		def some_func(self):
			return 'use me in template like this {{ view.some_func() }}'



	# List view for given model that will be rendered in table.
	class ExampleList(ModelList):
		model = SomeModel
		display_values = ['entity_1', 'entity_2']
		display_order = 'entity_1'


	#Delete view for a model entity
	class ExampleDelete(ModelDelete):
		model = SomeModel


	#Edit view for a model entity
	class ExampleEdit(ModelEdit):
		model = SomeModel


	#Create view for a model entity
	class ExampleCreate(ModelCreate):
		model = SomeModel


	#Register All views with Blueprint
	ExampleIndex.register_bp(example_bp)
	ExampleList.register_bp(example_bp)
	ExampleDelete.register_bp(example_bp)
	ExampleEdit.register_bp(example_bp)
	ExampleCreate.register_bp(example_bp)


	#Register Blueprint with the app
	app.register_blueprint(example_bp, url_prefix='example')
'''

from flask import Blueprint
from .views.index import IndexView
from .views.list import ModelList
from .views.edit import ModelEdit
from .views.create import ModelCreate
from .views.delete import ModelDelete

flaskengine_bp = Blueprint('flaskengine',
                           __name__,
                           static_folder='static',
                           static_url_path='/fe_static',
                           template_folder='templates',
                           )
