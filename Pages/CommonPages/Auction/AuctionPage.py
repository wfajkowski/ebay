import logging

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from Pages.CommonPages.TopMenu.TopMenu import TopMenu
from Pages.CommonPages.Auction.AuctionPageObjects import AuctionPageObjects


class AuctionPage(TopMenu):

    def getAuctionName(self):
        title = self.driver.find_element(*AuctionPageObjects.AuctionTitle).text
        logging.info("Auction title: {0}".format(title))
        return title

    def getSellerName(self):
        seller = self.driver.find_element(*AuctionPageObjects.SellerName).text
        logging.info("Auction seller: {0}".format(seller))
        return seller

    def getTimeLeft(self):
        timeLeft = self.driver.find_element(*AuctionPageObjects.TimeLeft).text
        logging.info("Auction time left: {0}".format(timeLeft))
        return timeLeft

    def getAuctionStartBid(self):
        startBid = self.driver.find_element(*AuctionPageObjects.AuctionStartBid).text
        logging.info("Auction start bid: {0}".format(startBid))
        return startBid

    def addAuctionToWatchList(self):
        WebDriverWait(self.driver, 10). \
            until(expected_conditions.presence_of_element_located(AuctionPageObjects.AddToWatchListLink))
        logging.info("Adding auction to watch list")
        self.driver.find_element(*AuctionPageObjects.AddToWatchListLink).click()
        WebDriverWait(self.driver, 10).\
            until(expected_conditions.presence_of_element_located(AuctionPageObjects.WatchingInfo))
        return self

    def checkThatAuctionIsNotWatched(self):
        logging.info("Checking that auction is not added to watch list")
        try:
            self.driver.find_element(*AuctionPageObjects.AddToWatchListLink)
        except NoSuchElementException:
            return False
        return True
