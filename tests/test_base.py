from .base import BaseTest, test_bp, BpAppRegister
from flaskengine.index import IndexView
from flaskengine.config import ConfigLoader


class BaseViewTest(IndexView):
    admin = False


BaseViewTest.register_bp(test_bp)


class BaseViewTestWithAdmin(IndexView):
    endpoint = 'test_admin'
    admin = True

BaseViewTestWithAdmin.register_bp(test_bp)


class TestBaseView(BaseTest):
    def setUp(self):
        super(TestBaseView, self).setUp()
        BpAppRegister(test_bp, self.app)

    def test_request_context(self):
        """TEST BASE VIEW: Test for correct context
        """
        response = self.client.get('/test/baseviewtest')
        #CHECK RESPONSE
        self.assert_200(response)

        #CHECK CONFIG
        config = self.get_context_variable('config')
        default_config = ConfigLoader.get_or_load_default({})
        self.assertEqual(config, default_config)

        #CHECK IF VIEW IS PASSED TO THE TEMPLATE
        view = self.get_context_variable('view')
        self.assertEqual(view.__class__, BaseViewTest)

    def test_config_set(self):
        """
        TEST BASE VIEW: Config loader
        """
        app_conf = {'FE_LAND_URL': 'test'}
        self.app.config.update(app_conf)
        response = self.client.get('/test/baseviewtest')
        #CHECK RESPONSE
        self.assert_200(response)

        #CHECK CONFIG
        config = self.get_context_variable('config')
        default_config = ConfigLoader.get_or_load_default(app_conf)
        self.assertEqual(config, default_config)

    def test_for_admin_login(self):
        """
        TEST BASE VIEW: test for admin loggin and setting endpoint
        """
        response = self.client.get('/test/test_admin')
        self.assert_403(response)
