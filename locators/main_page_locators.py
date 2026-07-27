"""Локаторы главной страницы."""

from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_BUTTON_TOP = (By.XPATH, "(//button[contains(text(), 'Заказать')])[1]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[contains(text(), 'Заказать')])[2]")
    ACCORDION_BUTTONS = (By.CLASS_NAME, 'accordion__button')
    LOGO_SCOOTER = (By.XPATH, "//img[@alt='Scooter']")
    LOGO_YANDEX = (By.XPATH, "//img[@alt='Yandex']")
    COOKIES_BUTTON = (By.XPATH, "//button[contains(text(), 'да все привыкли')]")
