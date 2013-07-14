import flask
from flask.ext.testing import TestCase
from flaskengine import flaskengine_bp
from google.appengine.ext import ndb

test_bp = flask.Blueprint('test_case', __name__)


#MODEL THAT WE TASTING AGAINST
class TestModel(ndb.Model):
    test_val_1 = ndb.StringProperty()
    test_val_2 = ndb.StringProperty()

    @property
    def __unicode__(self):
        return self.test_val_1


#TO REGISTER BP WITH THE TEST APP
class BpAppRegister(object):
    """docstring for BlogApp"""
    def __init__(self, bp, app):
        app.register_blueprint(bp, url_prefix='/test')


class BaseTest(TestCase):
    def _generate_data(self, data):
        for val in data:
            to_put = TestModel(test_val_1=val[0], test_val_2=val[1])
            to_put.put()

    def create_app(self):
        app = flask.Flask(__name__)
        app.config['TESTING'] = True
        return app

    def setUp(self):
        super(BaseTest, self).setUp()
        self.app.register_blueprint(flaskengine_bp)
        self.client = self.app.test_client()

    def tearDown(self):
        super(BaseTest, self).tearDown()
        all_entries = TestModel.query()
        for to_remove in all_entries:
            to_remove.key.delete()
