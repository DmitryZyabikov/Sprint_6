import pytest
import allure

from pages.main_page import MainPage
from locators.order_page_locators import OrderPageLocators
from constants import BASE_URL


@allure.feature("Оформление заказа")
class TestOrderFlow:

    @pytest.mark.parametrize("method_name,point_name", [
        ("click_order_button_top", "Верхняя кнопка"),
        ("click_order_button_bottom", "Нижняя кнопка"),
    ])
    @allure.title("Проверка точки входа в заказ - {point_name}")
    def test_order_entry_points(self, driver, method_name, point_name):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)

        with allure.step(f"Вход через {point_name}"):
            order_page = getattr(main_page, method_name)()

        with allure.step("Проверка отображения формы заказа"):
            assert order_page.is_element_displayed(OrderPageLocators.INPUT_NAME)

    @pytest.mark.parametrize("name, surname, address, station, phone, date, comment", [
        ("Василий", "Петров", "Москва, Ленина, 1", "Черкизовская", "+79991112233", "01.08.2026", "Быстрый темп"),
        ("Анна", "Смирнова", "МКАД, Щелково, 10", "Парк культуры", "+79994445566", "02.08.2026", "Без звука"),
    ])
    @allure.title("Полный цикл оформления заказа - {name} {surname}")
    def test_full_order_flow(self, driver, name, surname, address, station, phone, date, comment):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)

        with allure.step("Клик по кнопке 'Заказать'"):
            order_page = main_page.click_order_button_top()

        with allure.step("Заполнение первой формы заказа"):
            order_page.fill_first_form(name, surname, address, station, phone)

        with allure.step("Заполнение второй формы заказа"):
            order_page.fill_second_form(
                date_text=date,
                duration_index=0,
                color_locator=OrderPageLocators.COLOR_BLACK_CHECKBOX,
                comment=comment,
            )

        with allure.step("Подтверждение заказа"):
            order_page.confirm_order()

        with allure.step("Проверка сообщения об успехе"):
            assert order_page.is_success_message_visible(), "Сообщение не появилось после оформления заказа"
