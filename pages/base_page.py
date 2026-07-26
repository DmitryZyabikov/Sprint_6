"""Базовый класс для всех страниц."""

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )
        time.sleep(5)
        self.accept_cookies()

    def accept_cookies(self):
        try:
            btn = WebDriverWait(self.driver, 8).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'да все привыкли')]"))
            )
            time.sleep(1)
            self.driver.execute_script("arguments[0].click();", btn)
            time.sleep(1)
        except Exception:
            pass

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text