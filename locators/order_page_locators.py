"""Локаторы страницы оформления заказа."""

from selenium.webdriver.common.by import By


class OrderPageLocators:
    INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    INPUT_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    INPUT_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    INPUT_PHONE = (By.XPATH, "//input[contains(@placeholder, 'Телефон')]")
    NEXT_BUTTON = (By.XPATH, "//*[contains(text(), 'Далее')]")
    STATION_SUGGESTION = (By.CSS_SELECTOR, "div[data-testid='metro-suggestions'] div[class*='option'], ul[class*='suggestions'] li, div[class*='dropdown'] li, [class*='suggest'] li")
    INPUT_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DROPDOWN_DURATION = (By.XPATH, "//div[contains(@class, 'Dropdown-placeholder') or contains(@class, 'select') or contains(@class, 'dropdown')]")
    DROPDOWN_OPTIONS = (By.XPATH, "//div[contains(@class, 'Dropdown-option') or contains(@class, 'option') or contains(@class, 'item')]")
    OPTION_ONE_DAY = (By.XPATH, "(//div[contains(@class, 'Dropdown-option') or contains(@class, 'option')])[1]")
    OPTION_TWO_DAYS = (By.XPATH, "(//div[contains(@class, 'Dropdown-option') or contains(@class, 'option')])[2]")
    COLOR_BLACK_CHECKBOX = (By.XPATH, "//label[contains(text(), 'чёрный')]//input[@type='checkbox']")
    COLOR_GREY_CHECKBOX = (By.XPATH, "//label[contains(text(), 'серая')]//input[@type='checkbox']")
    INPUT_COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(), 'Заказать') and contains(@class, 'Button_Middle')]")
    CONFIRMATION_MODAL = (By.XPATH, "//*[contains(text(), 'Хотите оформить заказ?')]")
    CONFIRMATION_YES_BUTTON = (By.XPATH, "//button[contains(text(), 'Да') and (@class or @type)]")
    CONFIRMATION_NO_BUTTON = (By.XPATH, "//button[contains(text(), 'Нет')]")
    SUCCESS_MESSAGE = (By.XPATH, "//*[contains(text(), 'Заказ оформлен') or contains(text(), 'Номер заказа')]")
    SUCCESS_MODAL = (By.XPATH, "//*[contains(text(), 'Заказ оформлен')]")