import allure

from pages.main_page import MainPage
from constants import BASE_URL


@allure.feature("Логотипы")
class TestLogoRedirects:

    @allure.title("Проверка редиректа по логотипу Самоката")
    def test_logo_scooter_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)
        main_page.click_logo_scooter()

        with allure.step("Проверка URL после клика по логотипу Самоката"):
            assert BASE_URL in main_page.get_current_url()

    @allure.title("Проверка редиректа по логотипу Яндекса")
    def test_logo_yandex_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)

        with allure.step("Клик по логотипу Яндекса"):
            main_page.click_logo_yandex()

        with allure.step("Переключение на новую вкладку"):
            main_page.wait_until(
                lambda d: main_page.get_window_handles_count() > 1,
                timeout=10,
            )
            main_page.switch_to_window(1)

        with allure.step("Проверка URL новой вкладки"):
            main_page.wait_until(
                lambda d: main_page.get_current_url() != "about:blank",
                timeout=10,
            )
            current_url = main_page.get_current_url()
            assert "dzen.ru" in current_url or "yandex.ru" in current_url
