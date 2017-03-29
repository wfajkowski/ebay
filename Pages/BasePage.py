from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def waitTillJavaScriptsEnds(self, waitTime=30):
        WebDriverWait(self.driver, waitTime).until(
            lambda driver: self.driver.execute_script("return jQuery.active == 0"))
