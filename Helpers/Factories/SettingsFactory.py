from Settings.ProductionSettings import ProductionSettings


class SettingsFactory:
    """
    Klasa obsługująca wybór środowiska. Polecam poczytać trochę o wzorcu projektowym Fabryka.
    """

    @staticmethod
    def getSettings(env):
        if env == 'prod':
            return ProductionSettings()
        raise Exception("No such '{0}' env exists".format(env))
