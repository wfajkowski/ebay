from Pages.BasePage import BasePage
from Pages.CommonPages.UserPanelMenu.UserPanelMenuObjects import UserPanelMenuObjects


class UserPanelMenu(BasePage):

    def goToWatchList(self):
        from Pages.UserPanel.MyEbay.WatchList.WatchListPage import WatchListPage
        self.driver.find_element(*UserPanelMenuObjects.WatchList).click()
        return WatchListPage(self.driver)
