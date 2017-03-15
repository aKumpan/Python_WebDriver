import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

script_dir = os.path.dirname(__file__)


class WebDriverFactory(object):

    @staticmethod
    def get_web_driver(browser_name):
        if browser_name == "firefox":
            return webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser_name == "chrome":
            return webdriver.Chrome(ChromeDriverManager().install())
        raise Exception("No such " + browser_name + " browser exists")
