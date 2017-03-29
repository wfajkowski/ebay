from Pages.BasePage import BasePage
from Pages.UserPanel.MyEbay.WatchList.WatchListPageObjects import WatchListPageObjects


class WatchListPage(BasePage):

    def getFirstWatchedAuctionTitle(self):
        return self.driver.find_element(*WatchListPageObjects.AuctionTitleInfo).text

    def getFirstWatchedAuctionSellerName(self):
        return self.driver.find_element(*WatchListPageObjects.AuctionSellerInfo).text
