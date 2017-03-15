from main.pages.MainPage import MainPage
from tests.BaseTest import BaseTest


class WikipediaTests(BaseTest):
    SEARCH_TERM = "Software"

    def search_test(self):
        main_page = MainPage(self.driver).open()
        article_page = main_page.search_for(self.SEARCH_TERM)  # searching for self.SEARCH_TERM

        article_page.check_page_title(self.SEARCH_TERM)  # Verifying that Article page title contains self.SEARCH_TERM
