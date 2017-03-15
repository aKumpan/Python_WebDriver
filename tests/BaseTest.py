import unittest

from main.core.driverfactory.WebDriverFactory import WebDriverFactory


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = WebDriverFactory.get_web_driver("chrome")
        self.driver.maximize_window()  # maximizing browser window

    def tearDown(self):
        self.driver.quit()
