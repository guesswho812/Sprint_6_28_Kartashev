import allure
import pytest
from pages.main_page import MainPage
from config.urls import BASE_URL


@allure.epic("Яндекс.Самокат")
@allure.feature("Навигация по логотипам")
class TestNavigation:
    """Тесты для навигации между страницами через логотипы"""
    
    @allure.title("Проверка перехода по логотипу Самоката")
    @allure.story("Навигация на главную страницу")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("""
    Проверка что клик по логотипу Самоката возвращает на главную страницу.
    Ожидаемое поведение: остаемся на текущей странице с главным URL.
    """)
    def test_scooter_logo_navigation(self, driver):
        main_page = MainPage(driver)
        
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()
        
        with allure.step("Кликнуть на логотип Самоката"):
            main_page.click_scooter_logo()
        
        with allure.step("Проверить URL главной страницы"):
            current_url = main_page.get_current_url()
            expected_url = BASE_URL
            assert current_url == expected_url, f"Ожидался URL: {expected_url}, получен: {current_url}"

    @allure.title("Проверка перехода по логотипу Яндекса")  
    @allure.story("Навигация на внешний ресурс")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("""
    Проверка что клик по логотипу Яндекса открывает новое окно/вкладку
    с переходом на главную страницу Дзена.
    Ожидаемое поведение: открывается новое окно с URL содержащим 'dzen.ru'.
    """)
    def test_yandex_logo_navigation(self, driver):
        main_page = MainPage(driver)
        
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()
            original_window = main_page.get_current_window_handle()
        
        with allure.step("Кликнуть на логотип Яндекса"):
            main_page.click_yandex_logo()
        
        with allure.step("Дождаться открытия нового окна и переключиться"):
            # Ждем открытия нового окна - используем assert вместо if
            main_page.wait_for_new_window(original_window, timeout=10)
            main_page.switch_to_new_window()
                
            # Ждем загрузки страницы Дзена
            with allure.step("Ожидать загрузки страницы Дзена"):
                main_page.wait_for_url_contains("dzen.ru", timeout=10)
            
            with allure.step("Проверить что открылась страница Дзена"):
                current_url = main_page.get_current_url()
                assert "dzen.ru" in current_url, f"Ожидался URL содержащий 'dzen.ru', получен: {current_url}"
            
            with allure.step("Закрыть новое окно и вернуться на главную"):
                main_page.close_current_window()
                main_page.switch_to_window(original_window)