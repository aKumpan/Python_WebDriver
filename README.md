# Selenium Webdriver + Python automation example

[![License badge](https://img.shields.io/badge/license-Apache2-orange.svg)](http://www.apache.org/licenses/LICENSE-2.0)

This repository contains [Selenium Webdriver] + [Python] examples to automate Web Based applications [Wikipedia] used as example. 
These examples are open source, released under the terms of [Apache 2.0 License].

## Code examples
1. BasePage:
```python
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
```
2. Simple test:
```python
class WikipediaTests(BaseTest):
    SEARCH_TERM = "Software"

    def search_test(self):
        main_page = MainPage(self.driver).open()
        article_page = main_page.search_for(self.SEARCH_TERM)  # searching for SEARCH_TERM

        article_page.check_page_title(self.SEARCH_TERM)  # Verifying that Article page title contains SEARCH_TERM
```

## Usage

In order to use Selenium Webdriver + Python automation example, first of all install Python 3.0+ verison and pip.
Latest version available here: 
[Download Python]

To run application:
1. Navigate to the project root folder.
2. Execute command: 
```bash
pip install -r requirements.txt
```
3.  Execute command:
```python
python -m unittest tests.WikipediaTests.WikipediaTests.search_test
```

## About

Selenium Webdriver + Python automation (Copyright &copy; 2017) is a personal project of [Anton Kumpan] licensed under [Apache 2.0 License]. 
Comments, questions and suggestions are always very [welcome][Selenium Webdriver + Python automation issues]!

[Apache 2.0 License]: http://www.apache.org/licenses/LICENSE-2.0
[Selenium Webdriver]: http://docs.seleniumhq.org/projects/webdriver/
[Python]: https://www.python.org/
[Download Python]: https://www.python.org/downloads/
[Wikipedia]: https://www.wikipedia.org/
[Anton Kumpan]: https://github.com/aKumpan
[Selenium Webdriver + Python automation issues]: https://github.com/aKumpan/Python_WebDriver/issues