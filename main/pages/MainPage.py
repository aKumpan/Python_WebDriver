from main.locators.locators import MainPageLocators
from main.pages.ArticlePage import ArticlePage
from main.pages.Page import Page


class MainPage(Page):

    def open(self):
        self.driver.get("https://en.wikipedia.org/wiki/Main_Page")
        return self

    def search_item(self, item):
        self.find_element(*MainPageLocators.SEARCH_INPUT).send_keys(item)
        self.find_element(*MainPageLocators.SEARCH_BUTTON).click()
        return ArticlePage(self.driver)
