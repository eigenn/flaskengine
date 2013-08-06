'''
    Base config handler for the flaskengine

    use flaks.confing hadler to chage default values.

    example:
            # SET the project title
            FE_TITLE = 'Name of my app'
            # nav menu.
            FE_NAV_BAR = {
                'Example': 'mymodel.mymodel_list',
            }
            # href for title
            FE_LAND_URL = '/'
            # Bootswaths theme
            # avalible options http://bootswatch.com
            FE_BOOTSWATCH_THEME = 'spacelab'
'''

class ConfigLoader(object):
    FE_TITLE = 'Flask Engine'
    FE_NAV_BAR = {}
    FE_LAND_URL = '/'
    FE_BOOTSWATCH_THEME = 'spacelab'

    @classmethod
    def required(cls):
        """
        get all the required config variables
        """
        return [val for val in dir(cls) if val.isupper()]

    @classmethod
    def get_or_load_default(cls, app_config):
        """
        return a dict that is a config for flaskengine template
        args:
            app_config: flask config dict.
        """
        config = {}
        for required in cls.required():
            if required in app_config:
                config[required] = app_config.get(required)
            else:
                config[required] = getattr(cls, required)
        return config
