from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

from data import DriverPath


class DriverFactory:
    def __init__(self, browser_name: str, grid: bool):
        self.browser_name = browser_name
        self.grid = grid
        self.hub_url = "http://localhost:4444/wd/hub"

    def get_driver(self) -> webdriver:
        if self.browser_name == "firefox":
            options = FirefoxOptions()
            options.add_argument("-headless")
            options.add_argument("--no-sandbox")
            if self.grid:
                return webdriver.Remote(command_executor=self.hub_url, options=options)
            return webdriver.Firefox(service=FirefoxService(DriverPath.firefox), options=options)

        elif self.browser_name == "edge":
            options = EdgeOptions()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            if self.grid:
                return webdriver.Remote(command_executor=self.hub_url, options=options)
            return webdriver.Edge(service=EdgeService(DriverPath.edge), options=options)

        else:
            options = ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            if self.grid:
                return webdriver.Remote(command_executor=self.hub_url, options=options)
            return webdriver.Chrome(service=ChromeService(DriverPath.chrome), options=options)
