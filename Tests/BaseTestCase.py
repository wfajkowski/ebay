import logging
import unittest

from selenium.webdriver.support.ui import WebDriverWait


class BaseTestCase(unittest.TestCase):
    """
    Klasa bazowa dla Test Casow
    """

    waitTime = 30

    def setUp(self, browser='chrome', env='prod'):
        from Pages.CommonPages.MainPage.MainEbayPage import MainEbayPage
        from Helpers.Factories.SettingsFactory import SettingsFactory
        from Helpers.Factories.WebdriverFactory import WebdriverFactory
        logging.basicConfig(level=logging.INFO)
        self.envSettings = SettingsFactory.getSettings(env)
        self.ebayDriver = WebdriverFactory.getWebdriver(browser)
        self.ebayDriver.maximize_window()
        self.ebayDriver.get(self.envSettings.usaUrl)
        self.wait = WebDriverWait(self.ebayDriver, self.waitTime)
        self.page = MainEbayPage(self.ebayDriver)

    def tearDown(self):
        self.ebayDriver.quit()
