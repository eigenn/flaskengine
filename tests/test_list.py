from .base import BaseTest, TestModel, BpAppRegister, test_bp
from flaskengine.list import ModelList


class ListTestView(ModelList):
    model = TestModel
    admin = False
    view_actions = []

ListTestView.register_bp(test_bp)


class ListTestViewCustom(ModelList):
    model = TestModel
    admin = False
    view_actions = []
    display_values = ['test_val_1', 'test_val_2']

    @classmethod
    def action(cls):
        return 'custome_list'

    def model_query(self):
        return self.model.query(self.model.test_val_1 == 'aaa')


ListTestViewCustom.register_bp(test_bp)


class TestModelList(BaseTest):

    def setUp(self):
        super(TestModelList, self).setUp()
        BpAppRegister(test_bp, self.app)
        dummy_data = [('fff', 'ddd'), ('aaa', 'bbb')]
        self._generate_data(dummy_data)

    def test_for_model_table(self):
        """TEST LIST MODEL: test if table render model correctly
        """
        response = self.client.get('/test/list')
        #CHECK RESPONSE
        self.assert_200(response)
        #CHECK TEMPLATE
        self.assert_template_used(ListTestView.template)
        #CHECK TABLE VALUES AND MODEL
        table = self.get_context_variable('table')
        model = self.get_context_variable('model')
        self.assertEqual(model, TestModel)
        model_counter = 0
        for row in table:
            model_counter += 1
            self.assertEqual(row.entity.__class__, TestModel)
            display_count = 0
            for val in row:
                display_count += 1
            self.assertEqual(display_count, 1)

        self.assertEqual(model_counter, TestModel.query().count())

    def test_custome_list_view(self):
        """TEST LIST MODEL: Custom filter and action
        """
        response = self.client.get('/test/custome_list')
        #CHECK RESPONSE
        self.assert_200(response)
        #CHECK TEMPLATE
        self.assert_template_used(ListTestView.template)
        #CHECK TABLE VALUES AND MODEL
        table = self.get_context_variable('table')
        model = self.get_context_variable('model')
        self.assertEqual(model, TestModel)
        model_counter = 0
        for row in table:
            model_counter += 1
            self.assertEqual(row.entity.__class__, TestModel)
            display_count = 0
            for val in row:
                display_count += 1
            self.assertEqual(display_count, 2)

        self.assertEqual(model_counter,
                         TestModel.query(TestModel.test_val_1 == 'aaa').count())
