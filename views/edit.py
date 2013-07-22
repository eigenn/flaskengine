from .base import BaseModelView, request
from wtforms.ext.appengine.ndb import model_form


class ModelEdit(BaseModelView):
    methods = ['GET', 'POST']
    template = 'flaskengine/edit.html'
    form = None
    endpoint = '/<key>/edit/'

    @classmethod
    def default_form(cls):
        '''
        if self.form not set it will render the default model_form
        '''
        form = model_form(cls.model)
        return form

    @classmethod
    def action(cls):
        '''
        current action edit
        '''
        return cls.edit_action()

    def post(self, **kwargs):
        '''
        safe the form to datastore
        kwargs:
            key: datastore urlsafekey to populate form
        '''
        if not self.form:
            self.form = self.default_form()
        if kwargs.get('key'):
            entity = self.get_entity_from_key(kwargs.get('key'))
        else:
            entity = self.model()
        form = self.form(request.form, obj=entity)
        context = {
            'form': form,
            'entity': entity,
        }
        if form.validate():
            form.populate_obj(entity)
            entity.put()
            context['message_ok'] = 'Enity Saved'
        else:
            context['message_alert'] = 'Enity Could not be Saved.'
        return self.render_template(**self.template_context(**context))

    def get(self, **kwargs):
        '''
        render the form
        kwargs:
            key: datastore urlsafekey to populate form
        '''
        if kwargs.get('key'):
            entity = self.get_entity_from_key(kwargs.get('key'))
        else:
            entity = None
        if not self.form:
            self.form = self.default_form()

        form = self.form(obj=entity)
        context = {
            'form': form,
            'entity': entity,
        }
        return self.render_template(**self.template_context(**context))
