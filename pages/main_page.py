from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from pages.order_page import OrderPage


class MainPage(BasePage):
    def click_order_button_top(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)
        return OrderPage(self.driver)

    def click_order_button_bottom(self):
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)
        return OrderPage(self.driver)

    def get_accordion_buttons(self):
        return self.driver.find_elements(*MainPageLocators.ACCORDION_BUTTONS)

    def click_logo_scooter(self):
        self.click(MainPageLocators.LOGO_SCOOTER)

    def click_logo_yandex(self):
        self.click(MainPageLocators.LOGO_YANDEX)