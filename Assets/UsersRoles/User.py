class User:
    """
    Podstawowa klasa obsługująca Usera
    """

    def __init__(self, login='', password='', name=''):
        self.login = login
        self.password = password
        self.name = name
