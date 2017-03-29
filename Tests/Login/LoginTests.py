import random

from Tests.BaseTestCase import BaseTestCase


class LoginTests(BaseTestCase):

    def test_LoginIntoEbay(self):
        user = self.envSettings.user
        self.page.clickSignInLink().\
            loginWithProperCredentials(user).\
            checkLoggedUser(user)

    def test_LoginWithWrongPassword(self):
        user = self.envSettings.user
        user.login += random.choice("abcdefghj1234")
        loginErrorMsg = self.page.clickSignInLink().\
            loginWithWrongCredentials(user).\
            getLoginErrorMessage()

        self.assertEqual(loginErrorMsg, "Oops, that's not a match.")
