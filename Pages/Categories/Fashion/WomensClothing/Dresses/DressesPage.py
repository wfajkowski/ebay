from Pages.Categories.Fashion.WomensClothing.SideMenu import SideMenu
from Pages.Categories.Fashion.WomensClothing.Dresses.DressesPageObjects import DressesPageObjects


class DressesPage(SideMenu):

    def enterFirstAuction(self):
        from Pages.CommonPages.Auction.AuctionPage import AuctionPage
        self.driver.find_element(*DressesPageObjects.firstAuctionImg).click()
        return AuctionPage(self.driver)

    def filterOnlyAuctions(self):
        self.driver.find_element(*DressesPageObjects.filterAuctionRadio).click()
        return self
