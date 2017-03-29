from Pages.BasePage import BasePage
from Pages.Categories.Fashion.WomensClothing.SideMenuObjects import SideMenuObjects


class SideMenu(BasePage):

    def goToDressesCategory(self):
        from Pages.Categories.Fashion.WomensClothing.Dresses.DressesPage import DressesPage
        self.driver.find_element(*SideMenuObjects.dressesLink).click()
        return DressesPage(self.driver)
