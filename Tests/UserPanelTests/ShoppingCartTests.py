from Tests.BaseTestCase import BaseTestCase


class ShoppingTests(BaseTestCase):
    """
    Klasa zawierajaca TC jedynie zwiazane z koszykiem
    """

    def test_checkAddressForm(self):
        # pobranie usera z settingsow
        user = self.envSettings.user
        # zaczynamy od strony startowej
        # przechodzimy do strony logowania
        # logujemy sie - zwracana jest strona startowa
        # sprawdzamy zalogowane uzytkownika
        # przechodzimy do koszyka (przez klik w ikonke)
        # sprawdzamy czy wyswietlily sie poprawne pola
        self.page.\
            clickSignInLink().\
            loginWithProperCredentials(user).\
            checkLoggedUser(user).\
            goToShoppingCart().\
            checkAllFieldsAreInAddressForm()
