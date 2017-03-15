import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.main.core.drivers.driverfactory.WebDriverFactory import WebDriverFactory


class WikipediaTests(unittest.TestCase):
    def setUp(self):
        self.driver = WebDriverFactory.get_web_driver("chrome")
        self.driver.maximize_window()  # maximizing browser window

    def tearDown(self):
        self.driver.close()

    def search_test(self):
        driver = self.driver
        driver.get("https://en.wikipedia.org/wiki/Main_Page")  # navigate to Wikipedia
        driver.find_element_by_id("searchInput").send_keys("Software")  # typing 'Software' to search input

        driver.find_element_by_id("searchButton").click()  # clicking search button
        # waiting 10 seconds for 'Computer software' to be present in 'body' tag
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Computer software"))
