from .edit import ModelEdit


class ModelCreate(ModelEdit):
    endpoint = '/create/'

    @classmethod
    def action(cls):
        return cls.create_action()
