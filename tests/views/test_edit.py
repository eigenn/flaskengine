from .base import BaseTest, TestModel, BpAppRegister, test_bp
from flaskengine import ModelEdit


class EditTestView(ModelEdit):
    admin = False
    model = TestModel

EditTestView.register_bp(test_bp)


class TestEditModel(BaseTest):
    def setUp(self):
        super(TestEditModel, self).setUp()
        BpAppRegister(test_bp, self.app)
        dummy_data = [('fff', 'ddd'), ('aaa', 'bbb')]
        self._generate_data(dummy_data)

    def test_form_rendering(self):
        """
        TEST MODEL EDIT: test form rendering.
        """
        entity = TestModel.query().get()
        response = self.client.get('/test/%s/edit/' % entity.key.urlsafe())
        self.assert_200(response)
        form = self.get_context_variable('form')
        for field in form:
            entity_values = getattr(entity, field.id)
            self.assertEqual(field.data, entity_values)

    def test_model_form_editing(self):
        """
        TEST MODEL EDIT: test save on post
        """
        entity = TestModel.query().get()
        form_data = {'test_val_1': 'test', 'test_val_2': 'test'}
        response = self.client.post('/test/%s/edit/' % entity.key.urlsafe(),
                                    data=form_data)
        self.assert_200(response)
        self.assertEqual(form_data, entity.to_dict())

    def test_entity_does_not_exist(self):
        """
        TEST MODEL EDIT: test for non valid key
        """
        response = self.client.post('/test/%s/edit/' % 'idontexist')
        self.assertStatus(response, 405)
