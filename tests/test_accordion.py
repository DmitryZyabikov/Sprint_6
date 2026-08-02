import pytest
import allure

from pages.main_page import MainPage
from constants import BASE_URL


EXPECTED_QUESTIONS = [
    "Сколько это стоит? И как оплатить?",
    "Хочу сразу несколько самокатов! Так можно?",
    "Как рассчитывается время аренды?",
    "Можно ли заказать самокат прямо на сегодня?",
    "Можно ли продлить заказ или вернуть самокат раньше?",
    "Вы привозите зарядку вместе с самокатом?",
    "Можно ли отменить заказ?",
    "Я жизу за МКАДом, привезёте?",
]


@allure.feature("Блок вопросов")
class TestAccordion:

    @pytest.mark.parametrize("question_index,expected_text", [
        (0, EXPECTED_QUESTIONS[0]),
        (1, EXPECTED_QUESTIONS[1]),
        (2, EXPECTED_QUESTIONS[2]),
        (3, EXPECTED_QUESTIONS[3]),
        (4, EXPECTED_QUESTIONS[4]),
        (5, EXPECTED_QUESTIONS[5]),
        (6, EXPECTED_QUESTIONS[6]),
        (7, EXPECTED_QUESTIONS[7]),
    ])
    @allure.title("Проверка блока вопросов - Вопрос #{question_index}: {expected_text}")
    def test_accordion_question(self, driver, question_index, expected_text):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)
        buttons = main_page.get_accordion_buttons()

        with allure.step(f"Проверка наличия вопроса #{question_index}"):
            assert question_index < len(buttons), f"Вопрос #{question_index} не найден"

        question_button = buttons[question_index]

        with allure.step(f"Проверка текста вопроса #{question_index}"):
            assert question_button.text == expected_text, (
                f"Текст вопроса #{question_index} не совпадает. "
                f"Ожидалось: '{expected_text}', получено: '{question_button.text}'"
            )

        with allure.step(f"Клик по вопросу: {expected_text}"):
            question_button.click()

        with allure.step(f"Проверка раскрытия вопроса #{question_index}"):
            is_expanded = main_page.wait_until(
                lambda d: question_button.get_attribute("aria-expanded") == "true",
                timeout=5,
            )
            assert is_expanded, f"Вопрос #{question_index} не раскрылся"
