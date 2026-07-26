import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    def fill_first_form(self, name, surname, address, station, phone):
        self.send_keys(OrderPageLocators.INPUT_NAME, name)
        self.send_keys(OrderPageLocators.INPUT_SURNAME, surname)
        self.send_keys(OrderPageLocators.INPUT_ADDRESS, address)

        phone_field = self.driver.find_element(*OrderPageLocators.INPUT_PHONE)
        phone_field.clear()
        phone_field.send_keys(phone)

        self._fill_metro_station(station)

        time.sleep(3)

        next_btn = None

        selectors = [
            OrderPageLocators.NEXT_BUTTON,
            (By.XPATH, "//button[contains(text(), 'Далее')]"),
            (By.XPATH, "//div[contains(@class, 'Button') and contains(text(), 'Далее')]"),
        ]

        for selector in selectors:
            try:
                next_btn = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable(selector)
                )
                break
            except Exception:
                continue

        if next_btn is None:
            elements = self.driver.find_elements(By.XPATH, "//*[contains(text(), 'Далее')]")
            if elements:
                next_btn = elements[0]
            else:
                raise Exception("Кнопка 'Далее' не найдена")

        self.driver.execute_script("arguments[0].click();", next_btn)

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(OrderPageLocators.INPUT_DATE)
        )

    def _fill_metro_station(self, station):
        station_field = self.driver.find_element(*OrderPageLocators.INPUT_STATION)

        station_field.clear()
        time.sleep(0.3)

        self.driver.execute_script("""
            var input = arguments[0];
            var nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
            nativeInputValueSetter.call(input, '');
            input.value = '';
            input.dispatchEvent(new Event('input', { bubbles: true }));
            input.dispatchEvent(new Event('change', { bubbles: true }));
        """, station_field)

        time.sleep(0.3)

        station_field.send_keys(station)
        time.sleep(2)

        selected = False

        try:
            elements = self.driver.find_elements(By.CSS_SELECTOR, "ul[class*='list'] li, div[class*='suggestions'] li, div[class*='options'] li")
            for el in elements:
                if station.lower() in el.text.lower() and el.is_displayed():
                    self.driver.execute_script("arguments[0].click();", el)
                    selected = True
                    break
        except Exception:
            pass

        if not selected:
            try:
                elements = self.driver.find_elements(By.CSS_SELECTOR, "div[class*='option'], div[class*='Item'], div[data-testid*='metro']")
                for el in elements:
                    if station.lower() in el.text.lower() and el.is_displayed():
                        self.driver.execute_script("arguments[0].click();", el)
                        selected = True
                        break
            except Exception:
                pass

        if not selected:
            time.sleep(0.3)
            station_field = self.driver.find_element(*OrderPageLocators.INPUT_STATION)
            station_field.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.5)
            station_field.send_keys(Keys.ENTER)
            time.sleep(1)
            selected = True

        if not selected:
            try:
                self.driver.execute_script("""
                    var input = arguments[0];
                    var nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
                    nativeInputValueSetter.call(input, arguments[1]);
                    input.dispatchEvent(new Event('input', { bubbles: true }));
                    input.dispatchEvent(new Event('change', { bubbles: true }));
                """, station_field, station)
                time.sleep(1)
            except Exception:
                pass

    def fill_second_form(self, date_text, duration_locator, color_locator, comment):
        date_input = self.driver.find_element(*OrderPageLocators.INPUT_DATE)
        date_input.clear()
        date_input.send_keys(date_text)
        time.sleep(0.5)
        date_input.send_keys(Keys.ESCAPE)
        time.sleep(1)

        dropdown = self.driver.find_element(*OrderPageLocators.DROPDOWN_DURATION)
        dropdown.click()
        time.sleep(1)

        option = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(duration_locator)
        )
        self.driver.execute_script("arguments[0].click();", option)
        time.sleep(1)

        checkbox = self.driver.find_element(*color_locator)
        self.driver.execute_script("arguments[0].click();", checkbox)
        time.sleep(0.5)

        comment_field = self.driver.find_element(*OrderPageLocators.INPUT_COMMENT)
        comment_field.clear()
        comment_field.send_keys(comment)

    def confirm_order(self):
        confirm_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.CONFIRM_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", confirm_btn)
        time.sleep(3)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.CONFIRMATION_MODAL)
        )
        time.sleep(1)

        yes_button = self.driver.find_element(*OrderPageLocators.CONFIRMATION_YES_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", yes_button)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", yes_button)
        time.sleep(15)

    def is_success_message_visible(self):
        selectors = [
            (By.XPATH, "//*[contains(text(), 'Заказ оформлен')]"),
            (By.XPATH, "//*[contains(text(), 'Номер заказа')]"),
            (By.XPATH, "//*[contains(text(), 'Заказ')]"),
            (By.CLASS_NAME, 'Order_Success__header'),
            (By.XPATH, "//h1[contains(text(), 'Заказ оформлен')]"),
        ]

        for by, selector in selectors:
            try:
                element = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located((by, selector))
                )
                if element.is_displayed():
                    return True
            except Exception:
                continue

        return False