import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Заполнение первой формы заказа")
    def fill_first_form(self, name, surname, address, station, phone):
        self.send_keys(OrderPageLocators.INPUT_NAME, name)
        self.send_keys(OrderPageLocators.INPUT_SURNAME, surname)
        self.send_keys(OrderPageLocators.INPUT_ADDRESS, address)

        phone_field = self.find_element(OrderPageLocators.INPUT_PHONE)
        phone_field.clear()
        phone_field.send_keys(phone)

        self._fill_metro_station(station)

        self._click_next_button()

        self.wait_for_visibility(OrderPageLocators.INPUT_DATE, timeout=20)

    @allure.step("Заполнение второй формы заказа")
    def fill_second_form(self, date_text, duration_locator, color_locator, comment):
        date_input = self.find_element(OrderPageLocators.INPUT_DATE)
        date_input.clear()
        date_input.send_keys(date_text)
        date_input.send_keys(Keys.ESCAPE)

        dropdown = self.find_element(OrderPageLocators.DROPDOWN_DURATION)
        dropdown.click()

        option = self.wait_for_clickable(duration_locator, timeout=5)
        self.execute_script("arguments[0].click();", option)

        checkbox = self.find_element(color_locator)
        self.execute_script("arguments[0].click();", checkbox)

        comment_field = self.find_element(OrderPageLocators.INPUT_COMMENT)
        comment_field.clear()
        comment_field.send_keys(comment)

    @allure.step("Подтверждение заказа")
    def confirm_order(self):
        confirm_btn = self.wait_for_clickable(OrderPageLocators.CONFIRM_BUTTON, timeout=10)
        self.execute_script("arguments[0].click();", confirm_btn)

        self.wait_for_visibility(OrderPageLocators.CONFIRMATION_MODAL, timeout=10)

        yes_button = self.find_element(OrderPageLocators.CONFIRMATION_YES_BUTTON)
        self.execute_script("arguments[0].scrollIntoView({block: 'center'});", yes_button)
        self.execute_script("arguments[0].click();", yes_button)

    @allure.step("Проверка видимости сообщения об успехе")
    def is_success_message_visible(self):
        selectors = [
            OrderPageLocators.SUCCESS_MESSAGE_1,
            OrderPageLocators.SUCCESS_MESSAGE_2,
            OrderPageLocators.SUCCESS_MESSAGE_3,
            OrderPageLocators.SUCCESS_MESSAGE_4,
            OrderPageLocators.SUCCESS_MESSAGE_5,
        ]

        for locator in selectors:
            try:
                element = self.wait_for_visibility(locator, timeout=5)
                if element.is_displayed():
                    return True
            except Exception:
                continue

        return False

    @allure.step("Заполнение станции метро")
    def _fill_metro_station(self, station):
        station_field = self.find_element(OrderPageLocators.INPUT_STATION)
        station_field.clear()
        station_field.send_keys(station)

        # Ждем появления подсказок метро
        try:
            self.wait_until(
                lambda d: len(d.find_elements(By.XPATH, "//*[contains(@class, 'suggest') or contains(@class, 'suggestion') or contains(@class, 'option')]")) > 0,
                timeout=10,
            )
        except Exception:
            pass

        # Пытаемся выбрать из подсказок
        selected = self._select_station_from_suggestions(
            station, OrderPageLocators.STATION_SUGGESTIONS_CSS_1
        )

        if not selected:
            selected = self._select_station_from_suggestions(
                station, OrderPageLocators.STATION_SUGGESTIONS_CSS_2
            )

        if not selected:
            selected = self._select_station_from_suggestions(
                station, OrderPageLocators.STATION_SUGGESTIONS_CSS_3
            )

        if not selected:
            # Выбираем первую подсказку стрелками
            station_field.send_keys(Keys.ARROW_DOWN)
            station_field.send_keys(Keys.ENTER)

    def _select_station_from_suggestions(self, station, css_selector):
        try:
            elements = self.find_elements_by_css(css_selector)
            for el in elements:
                if station.lower() in el.text.lower() and el.is_displayed():
                    self.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
                    self.execute_script("arguments[0].click();", el)
                    return True
        except Exception:
            pass
        return False

    def _click_next_button(self):
        selectors = [
            OrderPageLocators.NEXT_BUTTON,
            OrderPageLocators.NEXT_BUTTON_ALT_1,
            OrderPageLocators.NEXT_BUTTON_ALT_2,
        ]

        for selector in selectors:
            try:
                next_btn = self.wait_for_clickable(selector, timeout=5)
                self.execute_script("arguments[0].click();", next_btn)
                return
            except Exception:
                continue

        elements = self.find_all_elements(OrderPageLocators.NEXT_BUTTON)
        if elements:
            self.execute_script("arguments[0].click();", elements[0])
            return

        raise Exception("Кнопка 'Далее' не найдена")
