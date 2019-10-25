from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from jopt.project_utils import *


class WebAutomator:

    def __init__(self):
        self.__driver = None
        self.__wait = None
        self.__launch()

    @property
    def driver(self):
        return self.__driver

    @property
    def wait(self):
        return self.__wait

    def __launch(self):
        driver_path = get_full_driver_path("chromedriver")
        self.__driver = webdriver.Chrome(executable_path=driver_path)
        self.__wait = WebDriverWait(self.driver, 60)

    def quit(self):
        self.__driver.quit()

    def go_to_url(self, url):
        self.__driver.get(url)

    def wait_until_present(self, by_type, by_value):
        return self.wait.until(EC.presence_of_element_located((by_type, by_value)))

    def wait_until_clickable(self, by_type, by_value):
        return self.wait.until(EC.element_to_be_clickable((by_type, by_value)))

    def set_element_text(self, by_type, by_value, text):
        element = self.wait_until_clickable(by_type, by_value)
        element.clear()
        element.send_keys(text)
        return element.get_attribute("value")

    def click_element(self, by_type, by_value):
        element = self.wait_until_clickable(by_type, by_value)
        element.click()
