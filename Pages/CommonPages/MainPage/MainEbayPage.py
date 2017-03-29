import logging

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from Assets.DataTypes.Sites import Sites
from Pages.CommonPages.TopMenu.TopMenu import TopMenu
from Pages.CommonPages.MainPage.MainEbayPageObjects import MainEbayPageObjects


class MainEbayPage(TopMenu):
    """
    Dziedziczeniu tutaj zostalo zmienione na TopMenu a nie BasePage ze wzgledu na to, ze teraz mamy w klasie
    widoczne wszystkie funkcje z TopMenu -> TopMenu jest czyms co widac na wszystkich stronach poza strona
    logowania i rejestracji
    """

    def OpenFashionWomenClothingSubPage(self, site=Sites.USA):
        from Pages.Categories.Fashion.WomensClothing.WomensClothingPage import WomensClothingPage
        logging.info("Going to Fashion/Women Clothing sub-page")
        ActionChains(self.driver).move_to_element(
            self.driver.find_element(*MainEbayPageObjects.FashionCategory)).perform()
        if site == Sites.USA:
            WebDriverWait(self.driver, 30).until(
                expected_conditions.element_to_be_clickable(MainEbayPageObjects.UsaWomenClothingSubCategory))
            self.driver.find_element(*MainEbayPageObjects.UsaWomenClothingSubCategory).click()
        elif site == Sites.UK:
            WebDriverWait(self.driver, 30).until(
                expected_conditions.element_to_be_clickable(MainEbayPageObjects.UkWomenClothingSubCategory))
            self.driver.find_element(*MainEbayPageObjects.UkWomenClothingSubCategory).click()
        return WomensClothingPage(self.driver)

    def changeSiteTo(self, site):
        logging.info("Changing site to United Kingdom")
        ActionChains(self.driver).move_to_element(
            self.driver.find_element(*MainEbayPageObjects.EbaySites)).perform()
        WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((MainEbayPageObjects.SiteIcon[0],
                                                         MainEbayPageObjects.SiteIcon[1].format(site.value))))
        self.driver.find_element(MainEbayPageObjects.SiteIcon[0],
                                 MainEbayPageObjects.SiteIcon[1].format(site.value)).click()
        return self

    def checkUrl(self, site, envSettings):
        logging.info("Checking url for site: {0}".format(site.name))
        if site == Sites.USA:
            assert self.driver.current_url == envSettings.usaUrl
        elif site == Sites.UK:
            assert self.driver.current_url == envSettings.ukUrl
        else:
            logging.error("Unrecognized site given")
            raise TypeError
        return self
