import logging
from Architecture.Pages.BasePage import BasePage
from Architecture.Pages.Auctions.AuctionsObjects import AuctionsObjects


class Auctions(BasePage):
    def clickBids(self):
        self.driver.find_element(*AuctionsObjects.auctionBids).click()

    def getAuctionName(self):
        title = self.driver.find_element(*AuctionsObjects.auctionName).text
        logging.info("Auction title: {0}".format(title))
        return title

    def getSeller(self):
        seller = self.driver.find_element(*AuctionsObjects.auctionSeller).text
        logging.info("Auction seller: {0}".format(seller))
        return seller

    def getTimeToEnd(self):
        if len(self.driver.find_elements(*AuctionsObjects.auctionTimeToEnd))>0:
            timeToEnd = self.driver.find_element(*AuctionsObjects.auctionTimeToEnd).text
            logging.info("Auction time to end: {0}".format(timeToEnd))
            return timeToEnd
        else:
            msg = logging.info("It's not an auction")
            return msg
