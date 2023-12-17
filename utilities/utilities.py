from selenium import webdriver
from selenium.common import WebDriverException


class WebDriverElements:
    def __init__(self, browser="chrome"):
        if browser.lower() == "chrome":
            # Especifico la ubicación del chromedriver
            chromedriver_path = '/Users/lucho/LUIS/Prueba cargo QA R5/AutomationWithPOM/Driver/chromedriver'
            # Configuro las opciones del navegador
            chrome_options = webdriver.ChromeOptions()
            try:
                self.driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)
            except WebDriverException as e:
                print(f"Un error ocurrió: {e}")
            # Creo una instancia del navegador Chrome
            self.driver.maximize_window()
            self.driver.delete_all_cookies()
        elif browser.lower() == "firefox":
            # Especifico la ubicación del firefoxdriver
            firefoxdriver_path = '/Users/lucho/LUIS/Prueba cargo QA R5/AutomationWithPOM/Driver/geckodriver'
            # Configuro las opciones del navegador
            firefox_options = webdriver.FirefoxOptions()
            try:
                self.driver = webdriver.Firefox(executable_path=firefoxdriver_path, options=firefox_options)
            except WebDriverException as e:
                print(f"Un error ocurrió: {e}")
            # Creo una instancia del navegador Chrome
            self.driver.maximize_window()
            self.driver.delete_all_cookies()
        else:
            raise ValueError(f"Navegador NO soportado: {browser}")

    def get_driver(self):
        return self.driver


