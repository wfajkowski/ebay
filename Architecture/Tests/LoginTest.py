from __future__ import absolute_import
import logging
from Architecture.Tests.BaseTestCase import BaseTestCase
from Architecture.Assets.User import User


class LoginTest(BaseTestCase):

    def test_succesfulLogin(self):
        logging.info("Test succesfullLogin")
        ebayMainPage = self.page.clickSignInLink().loginWithValidUser(
            self.envSettings.ebayUser[0]) # EbayMainPage/LoginPage/EbayMainPage/EbayMainPage
        messagetext = ebayMainPage.getLoggedUser()
        self.assertEquals("ebay", messagetext)

    def test_wrongLogin(self):
        ebayUser = User('ebay.automatization123@gmail.com', 'ebay123ebay')
        messagetext = self.page.clickSignInLink().loginWithInvalidUser(
            ebayUser)  # EbayMainPage/LoginPage/EbayMainPage/EbayMainPage
        self.assertEquals("Oops, that's not a match.", messagetext)
