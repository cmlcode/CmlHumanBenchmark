import chromedriver_autoinstaller
from selenium import webdriver

class DriverFactory:
    def __init__(self, install_driver = True):
        if install_driver:
            self.install_driver()
        self.browser_options = webdriver.ChromeOptions()
    def install_driver(self):    
        chromedriver_autoinstaller.install()
    def add_maximized(self):
        self.browser_options.add_argument("--start-maximized")
    def add_detached(self):
        self.browser_options.add_experimental_option("detach", True)
    def create_driver(self):
        return webdriver.Chrome(options = self.browser_options)