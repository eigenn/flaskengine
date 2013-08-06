from .base import BaseModelView
from .helper import ModelTable


class ModelList(BaseModelView):
    method = ['GET']
    template = 'flaskengine/list.html'
    view_actions = ['edit', 'delete', 'create']
    display_values = ['__unicode__']
    display_order = None
    display_order_direction = 'desc'
    display_filter = None

    def model_query(self):
        """
        override this to apply filter to the diplayer model
        """
        return self.model.query()

    def get_orderred_model(self, display_order=None, order_direction=None):
        """
        get the model query obj
        """
        query = self.model_query()
        if display_order:
            order_val = getattr(self.model, display_order)
            if order_direction == 'desc':
                return query.order(-order_val)
            else:
                return query.order(order_val)
        else:
            return query

    @classmethod
    def action(cls):
        return cls.list_action()

    def get(self):
        query = self.get_orderred_model(self.display_order,
                                        self.display_order_direction)
        table = ModelTable(self.display_values, query)
        return self.render_template(**self.template_context(table=table))
