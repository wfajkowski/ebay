from Architecture.Pages.BasePage import BasePage
from Architecture.Pages.Motors.MotorsObjects import MotorsObjects


class Motors(BasePage):

    def clickMotorcycles(self):
        from Architecture.Pages.Motorcycles.Motorcycles import Motorcycles
        self.driver.find_element(*MotorsObjects.Motorcycles).click()
        return Motorcycles(self.driver)
