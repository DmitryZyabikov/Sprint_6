import pytest
import allure

from pages.main_page import MainPage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from constants import BASE_URL


@allure.title("Проверка точек входа в заказ - {point_name}")
class TestScooterFunctional:

    @pytest.mark.parametrize("entry_point", [
        ("top", "Верхняя кнопка"),
        ("bottom", "Нижняя кнопка"),
    ])
    @allure.title("Проверка точек входа в заказ - {point_name}")
    def test_order_entry_points(self, driver, entry_point):
        point_type, point_name = entry_point
        main_page = MainPage(driver)
        main_page.open(BASE_URL)

        with allure.step(f"Вход {point_name}"):
            if point_type == "top":
                main_page.click_order_button_top()
            else:
                main_page.click_order_button_bottom()

        with allure.step("Проверка формы заказа"):
            assert driver.find_element(*OrderPageLocators.INPUT_NAME).is_displayed()

    @pytest.mark.parametrize("name, surname, address, station, phone, date, comment", [
        ("Василий", "Петров", "Москва, Ленина, 1", "Черкизовская", "+79991112233", "01.08.2026", "Быстрый темп"),
        ("Анна", "Смирнова", "МКАД, Щелково, 10", "Сокольническая", "+79994445566", "02.08.2026", "Без звука"),
    ])
    @allure.title("Полный цикл оформления заказа - {name} {surname}")
    def test_full_order_flow(self, driver, name, surname, address, station, phone, date, comment):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)

        with allure.step("Клик по кнопке заказать сверху"):
            order_page = main_page.click_order_button_top()

        with allure.step("Заполнение первой формы заказа"):
            order_page.fill_first_form(name, surname, address, station, phone)

        with allure.step("Заполнение второй формы заказа"):
            order_page.fill_second_form(
                date_text=date,
                duration_locator=OrderPageLocators.OPTION_ONE_DAY,
                color_locator=OrderPageLocators.COLOR_BLACK_CHECKBOX,
                comment=comment,
            )

        with allure.step("Подтверждение заказа"):
            order_page.confirm_order()

        with allure.step("Проверка сообщения об успехе"):
            assert order_page.is_success_message_visible(), "Сообщение не появилось после оформления заказа"

    @pytest.mark.parametrize("question_index", [0, 1, 2, 3, 4, 5, 6, 7])
    @allure.title("Проверка блока вопросов - Вопрос #{question_index}")
    def test_accordion(self, driver, question_index):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)
        buttons = main_page.get_accordion_buttons()

        with allure.step(f"Проверка вопроса #{question_index}"):
            assert question_index < len(buttons), f"Вопрос #{question_index} не найден"

        question_button = buttons[question_index]
        question_text = question_button.text

        with allure.step(f"Клик по вопросу: {question_text}"):
            question_button.click()

        WebDriverWait(driver, 5).until(
            lambda d: question_button.get_attribute("aria-expanded") == "true"
        )

    @allure.title("Проверка редиректа по логотипу Самоката")
    def test_logo_scooter_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)
        main_page.click_logo_scooter()
        assert BASE_URL in driver.current_url

    @allure.title("Проверка редиректа по логотипу Яндекса")
    def test_logo_yandex_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)

        with allure.step("Клик по логотипу Яндекса"):
            main_page.click_logo_yandex()

        with allure.step("Переключение на новую вкладку и проверка URL"):
            WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
            driver.switch_to.window(driver.window_handles[-1])
            WebDriverWait(driver, 10).until(lambda d: d.current_url != "about:blank")
            assert "dzen.ru" in driver.current_url or "yandex.ru" in driver.current_url