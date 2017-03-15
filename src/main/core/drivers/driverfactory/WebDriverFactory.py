import os

from selenium import webdriver

script_dir = os.path.dirname(__file__)


class WebDriverFactory(object):

    @staticmethod
    def get_web_driver(browser_name):
        if browser_name == "firefox":
            return webdriver.Firefox()
        elif browser_name == "chrome":
            return webdriver.Chrome(os.path.join(os.path.dirname(script_dir), "chromedriver.exe"))
        raise Exception("No such " + browser_name + " browser exists")
