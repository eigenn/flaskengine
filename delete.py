from flask import redirect
from .base import BaseModelView


class ModelDelete(BaseModelView):
    methods = ['GET', 'POST']
    template = 'flaskengine/delete.html'
    endpoint = '/<key>/delete/'

    @classmethod
    def action(cls):
        return cls.delete_action()

    def post(self, **kwargs):
        entity = self.get_entity_from_key(kwargs.get('key'))
        entity.key.delete()
        return redirect(self.get_list_action_url())

    def get(self, **kwargs):
        entity = self.get_entry_from_key(kwargs.get('key'))
        return self.render_template(**self.dispatch_context(entity=entity))
