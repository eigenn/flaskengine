from flask.views import View
from flask import render_template, current_app, abort, url_for, request
from google.appengine.api import users
from google.appengine.ext import ndb
from .config import ConfigLoader


class BaseView(View):
    """
    docstring for BaseCrudView
    base view that can be used to generate flask views.
    """
    #ONLY GET ALLOWED BY DEFAULT ALTO GET AND POST IMPLEMENTED
    methods = ['GET', ]
    template = None
    admin = True
    endpoint = None

    def has_permissions(self):
        """
        check if user have permissions to the view
        """
        if self.admin and not users.is_current_user_admin():
            #TODO: Something smarter here.
            return abort(403)

    def render_template(self, **context):
        """
        base rendering of a template
        """
        return render_template(self.template, **context)

    def template_context(self, **kwargs):
        """
        base context for templates
        """
        context = {
            'config': ConfigLoader.get_or_load_default(current_app.config),
            'view': self,
        }
        if kwargs:
            context.update(kwargs)
        return context

    def dispatch_request(self, **kwargs):
        """
        Base dispatch_request
        """
        self.has_permissions()
        if request.method == 'POST':
            return self.post(**kwargs)
        elif request.method == 'GET':
            return self.get(**kwargs)
        else:
            return abort(405)

    def post(self, **kwargs):
        """
        handle post method
        """
        return self.render_template(**self.template_context())

    def get(self, **kwargs):
        """
        handle get method
        """
        return self.render_template(**self.template_context())

    @classmethod
    def get_endpoint(cls):
        """
        set the endpoint for the view method
        """
        if cls.endpoint:
            return '/' + cls.endpoint
        else:
            return '/' + cls.get_view_name()

    @classmethod
    def get_view_name(cls):
        """
        as_view name register
        """
        return cls.__name__.lower()

    @classmethod
    def register_bp(cls, bp):
        bp.add_url_rule(cls.get_endpoint(),
                        view_func=cls.as_view(cls.get_view_name())
                        )


class BaseModelView(BaseView):
    """
    base model view for ndb models on app engine
    colection of all the avalible actions
    """
    #NDB MODEL
    model = None
    view_actions = []

    def get_entity_from_key(self, key):
        """
        get the ndb entity form the key
        """
        try:
            return ndb.Key(urlsafe=key).get()
        except:
            return abort(405)

    @classmethod
    def get_endpoint(cls):
        """
        get endpoint for the model view.
        """
        if cls.endpoint:
            return cls.endpoint
        return '/' + cls.action()

    def template_context(self, **kwargs):
        return super(BaseModelView, self).template_context(model=self.model,
                                                           **kwargs)

    @classmethod
    def action(cls):
        """
        define a current action
        """
        return ''

    @classmethod
    def get_view_name(cls, action=None):
        """
        generate view_name
        view names are defined as modelName_ActionOnModel
        """
        if not action:
            action = cls.action()
        return cls.model.__name__.lower() + '_' + action

    @classmethod
    def get_action_url(cls, action, **kwargs):
        """
        get action url
        """
        return url_for('.' + cls.get_view_name(action), **kwargs)

    #LIST ACTION
    @classmethod
    def list_action(cls):
        return 'list'

    @classmethod
    def get_list_action_url(cls):
        return cls.get_action_url(cls.list_action())

    #EDIT ACTION
    @classmethod
    def edit_action(cls):
        return 'edit'

    @classmethod
    def get_edit_action_url(cls, entry):
        entry = entry.key.urlsafe()
        return cls.get_action_url(cls.edit_action(), key=entry)

    #DELETE ACTION
    @classmethod
    def delete_action(cls):
        return 'delete'

    @classmethod
    def get_delete_action_url(cls, entry):
        return cls.get_action_url(cls.delete_action(), key=entry.key.urlsafe())

    #CREATE ACTION
    @classmethod
    def create_action(cls):
        return 'create'

    @classmethod
    def get_create_action_url(cls):
        return cls.get_action_url(cls.create_action())
