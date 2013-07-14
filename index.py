from .base import BaseView


class IndexView(BaseView):
    template = 'flaskengine/index.html'
    include = None
