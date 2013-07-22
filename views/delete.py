from flask import redirect
from .base import BaseModelView


class ModelDelete(BaseModelView):
    methods = ['GET', 'POST']
    template = 'flaskengine/delete.html'
    endpoint = '/<key>/delete/'

    @classmethod
    def action(cls):
        '''
        current action delete
        '''
        return cls.delete_action()

    def post(self, **kwargs):
        '''
        kwargs:
            key: datastore urlsafe key 

        remove the entity from the datastore.
        redirect to list view for given model
        '''
        entity = self.get_entity_from_key(kwargs.get('key'))
        entity.key.delete()
        return redirect(self.get_list_action_url())

    def get(self, **kwargs):
        '''
        render the delete template
        kwargs:
            key: datastore urlsafe key 

        confirmation step
        '''
        entity = self.get_entry_from_key(kwargs.get('key'))
        return self.render_template(**self.dispatch_context(entity=entity))
