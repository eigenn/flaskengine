from .base import BaseTest, TestModel, BpAppRegister, test_bp
from flaskengine import ModelDelete


class DeleteTestView(ModelDelete):
    admin = False
    model = TestModel

DeleteTestView.register_bp(test_bp)


class TestDeleteModel(BaseTest):
    def setUp(self):
        super(TestDeleteModel, self).setUp()
        BpAppRegister(test_bp, self.app)
        dummy_data = [('fff', 'ddd'), ('aaa', 'bbb')]
        self._generate_data(dummy_data)

    def test_model_delete(self):
        """
        TEST MODEL DELETE
        """
        #COUNT THE ENTITY'S IN DATASTORE
        pre_model_count = TestModel.query().count()
        entity_key = TestModel.query().get().key.urlsafe()
        response = self.client.post('/test/%s/delete/' % entity_key)
        #REDIRECT
        self.assert_status(response, 302)
        #COUNT ENTITY'S AFTER THE REMOVAL
        post_model_count = TestModel.query().count()
        #COUNT AFTER ENTITY WAS REMOVED
        self.assertEqual(pre_model_count - 1, post_model_count)
