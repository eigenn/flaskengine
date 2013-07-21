
## ABOUT

GAE flask model  crud view's with bootsrap.

## Requirements

* Flask==0.10.1
* WTForms==1.0.4
* Jinja2==2.7
* Werkzeug==0.9.1
* itsdangerous==0.21
* Flask-Testing==0.4
* NoseGAE==0.2.0
* blinker==1.3
* twill==0.9
* wsgiref==0.1.2
* MarkupSafe==0.18
* nose==1.3.0

## INSTALATION

in your flask powered GAE project

```
	git submodule add https://github.com/eigenn/flaskengine.git
	cd flaskengine/
	pip install -r requirements.txt
```

## USAGE


``` python
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
```

## REFERENCE

### FLASK CONFIG
configurating the flaskengine by using the flask.config handling.

Example Config.

``` python
	# SET the project title
	FE_TITLE = 'Name of my app'
	# nav menu.
	FE_NAV_BAR = {
        'Example': 'mymodel.mymodel_list',
    }
    # href for title
	FE_LAND_URL = '/'
	# Bootswaths theme
	# avalible options http://bootswatch.com
	FE_BOOTSWATCH_THEME = 'spacelab'
```

## TODO

* Pagination for List View
* Admin authentication redirect
