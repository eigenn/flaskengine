from .edit import ModelEdit


class ModelCreate(ModelEdit):
    endpoint = '/create/'

    @classmethod
    def action(cls):
    	'''
    	current action create
    	'''
        return cls.create_action()
