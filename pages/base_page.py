"""Базовый класс для всех страниц."""

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открытие страницы {url}")
    def open(self, url):
        self.driver.get(url)
        self.wait_for_element((By.TAG_NAME, 'body'), timeout=15)
        self.accept_cookies()

    @allure.step("Принятие cookies")
    def accept_cookies(self):
        try:
            btn = self.wait_for_clickable(
                (By.XPATH, "//button[contains(text(), 'да все привыкли')]"), timeout=8
            )
            self.execute_script("arguments[0].click();", btn)
        except Exception:
            pass

    @allure.step("Поиск элемента {locator}")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Поиск элементов {locator}")
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Клик по элементу {locator}")
    def click(self, locator):
        element = self.find_element(locator)
        self.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()

    @allure.step("Ввод текста '{text}' в поле {locator}")
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получение текста элемента {locator}")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Ожидание кликабельности элемента {locator}")
    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Ожидание видимости элемента {locator}")
    def wait_for_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидание присутствия элемента {locator}")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Ожидание условия")
    def wait_until(self, condition, timeout=10):
        return WebDriverWait(self.driver, timeout).until(condition)

    @allure.step("Выполнение JS-скрипта")
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    @allure.step("Получение атрибута '{attr}' элемента {locator}")
    def get_attribute(self, locator, attr):
        return self.find_element(locator).get_attribute(attr)

    @allure.step("Переключение на вкладку {index}")
    def switch_to_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Получение количества вкладок")
    def get_window_handles_count(self):
        return len(self.driver.window_handles)

    @allure.step("Проверка отображения элемента {locator}")
    def is_element_displayed(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except Exception:
            return False

    @allure.step("Поиск элементов по CSS-селектору {css_selector}")
    def find_elements_by_css(self, css_selector):
        return self.driver.find_elements(By.CSS_SELECTOR, css_selector)

    @allure.step("Поиск всех элементов по локатору {locator}")
    def find_all_elements(self, locator):
        return self.driver.find_elements(*locator)
