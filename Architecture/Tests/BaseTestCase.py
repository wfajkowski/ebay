import unittest
import logging
from datetime import datetime
import sys
from selenium import webdriver
from Architecture.Settings.ProductionSettings import ProductionSettings
from Architecture.Settings.StagingSettings import StagingSettings

from Architecture.Pages.Ebay.EbayMainPage import EbayMainPage

class BaseTestCase(unittest.TestCase):
    def setUp(self,env='prod'):
        if env == 'prod':
            self.envSettings = ProductionSettings()
        elif env == 'stg':
            self.envSettings = StagingSettings()
        else:
            self.envSettings = ProductionSettings()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.envSettings.ebayUrl)
        self.page = EbayMainPage(self.driver)
        logging.basicConfig(level=logging.INFO,format="%(asctime)s %(message)s")

    def tearDown(self):
        if sys.exc_info()[0]:
            tcName = self._testMethodName
            creationTime = datetime.now().strftime("%d-%m-%Y_%H_%M_%S")
            self.driver.get_screenshot_as_file("c:/Users/iwaf/PycharmProjects/Selenium/Screens/{0}_{1}.jpg".format(tcName, creationTime))
        self.driver.quit()