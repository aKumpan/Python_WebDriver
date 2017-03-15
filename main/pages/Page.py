from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Page(object):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30

    def check_page_title(self, title):
        WebDriverWait(self.driver, self.timeout).until(EC.title_contains(title))

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url
