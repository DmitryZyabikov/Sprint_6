import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from pages.order_page import OrderPage


class MainPage(BasePage):

    @allure.step("Клик по верхней кнопке 'Заказать'")
    def click_order_button_top(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)
        return OrderPage(self.driver)

    @allure.step("Клик по нижней кнопке 'Заказать'")
    def click_order_button_bottom(self):
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)
        return OrderPage(self.driver)

    @allure.step("Получение кнопок аккордеона")
    def get_accordion_buttons(self):
        return self.find_elements(MainPageLocators.ACCORDION_BUTTONS)

    @allure.step("Клик по логотипу Самоката")
    def click_logo_scooter(self):
        self.click(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Клик по логотипу Яндекса")
    def click_logo_yandex(self):
        self.click(MainPageLocators.LOGO_YANDEX)
