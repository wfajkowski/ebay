from Architecture.Pages.BasePage import BasePage
from Architecture.Pages.Motorcycles.MotorcyclesObjects import MotorcyclesObjects


class Motorcycles(BasePage):

    def clickFirstAuction(self):
        #from Architecture.Pages.Motors.Motors import Motors
        self.driver.find_element(*MotorcyclesObjects.firstAuction).click()
        #return Motors