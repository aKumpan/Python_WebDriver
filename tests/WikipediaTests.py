import unittest

from main.core.driverfactory.WebDriverFactory import WebDriverFactory
from main.pages.MainPage import MainPage


class WikipediaTests(unittest.TestCase):
    def setUp(self):
        self.driver = WebDriverFactory.get_web_driver("chrome")
        self.driver.maximize_window()  # maximizing browser window

    def tearDown(self):
        self.driver.quit()

    def search_test(self):
        main_page = MainPage(self.driver).open()
        article_page = main_page.search_item("Software")  # searching for 'Software'

        article_page.check_page_title("Software")  # Verifying that Article page title contains Software
