from __future__ import absolute_import
import logging
from Architecture.Tests.BaseTestCase import BaseTestCase
from Architecture.Pages.Auctions.Auctions import Auctions
from Architecture.Pages.Auctions.AuctionsObjects import AuctionsObjects
import time


class AddToWatch(BaseTestCase):

    def test_addToWatch(self):
        logging.info("Test addToWatch")
        auctionPage = self.page.clickSignInLink().loginWithValidUser(
            self.envSettings.ebayUser[0]).goToCategory().clickMotorcycles().clickFirstAuction()
        #auctionURL = self.driver.current_url
        #self.assertEquals("http://www.ebay.com/itm/2015-Harley-Davidson-Touring-/332141618973", auctionURL)
        infos = Auctions(self.driver)
        infos.getAuctionName()
        infos.getSeller()
        infos.getTimeToEnd()