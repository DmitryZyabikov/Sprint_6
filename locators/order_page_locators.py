"""Локаторы страницы оформления заказа."""

from selenium.webdriver.common.by import By


class OrderPageLocators:
    INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    INPUT_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    INPUT_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    INPUT_PHONE = (By.XPATH, "//input[contains(@placeholder, 'Телефон')]")
    NEXT_BUTTON = (By.XPATH, "//*[contains(text(), 'Далее')]")
    NEXT_BUTTON_ALT_1 = (By.XPATH, "//button[contains(text(), 'Далее')]")
    NEXT_BUTTON_ALT_2 = (By.XPATH, "//div[contains(@class, 'Button') and contains(text(), 'Далее')]")
    STATION_SUGGESTIONS_CSS_1 = "ul[class*='list'] li, div[class*='suggestions'] li, div[class*='options'] li"
    STATION_SUGGESTIONS_CSS_2 = "div[class*='option'], div[class*='Item'], div[data-testid*='metro']"
    STATION_SUGGESTIONS_CSS_3 = "div[data-testid='metro-suggestions'] div[class*='option'], ul[class*='suggestions'] li, div[class*='dropdown'] li, [class*='suggest'] li"
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
    SUCCESS_MESSAGE_1 = (By.XPATH, "//*[contains(text(), 'Заказ оформлен')]")
    SUCCESS_MESSAGE_2 = (By.XPATH, "//*[contains(text(), 'Номер заказа')]")
    SUCCESS_MESSAGE_3 = (By.XPATH, "//*[contains(text(), 'Заказ')]")
    SUCCESS_MESSAGE_4 = (By.CLASS_NAME, 'Order_Success__header')
    SUCCESS_MESSAGE_5 = (By.XPATH, "//h1[contains(text(), 'Заказ оформлен')]")
