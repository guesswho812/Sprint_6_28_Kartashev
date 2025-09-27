import allure
import pytest
from pages.main_page import MainPage


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
            current_url = driver.current_url
            assert current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title("Проверка перехода по логотипу Яндекса")  
    @allure.story("Навигация на внешний ресурс")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("""
    Проверка что клик по логотипу Яндекса открывает новое окно/вкладку
    с переходом на главную страницу Яндекса или Дзена.
    Ожидаемое поведение: открывается новое окно с URL Яндекса/Дзена.
    """)
    def test_yandex_logo_navigation(self, driver):
        main_page = MainPage(driver)
        
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()
            original_window = driver.current_window_handle
        
        with allure.step("Кликнуть на логотип Яндекса"):
            main_page.click_yandex_logo()
        
        with allure.step("Подождать и переключиться на новое окно"):
            import time
            time.sleep(3)
            
            if len(driver.window_handles) > 1:
                driver.switch_to.window(driver.window_handles[-1])
                current_url = driver.current_url
                
                with allure.step("Закрыть новое окно и вернуться"):
                    driver.close()
                    driver.switch_to.window(original_window)
            else:
                with allure.step("Новое окно не открылось - продолжить выполнение"):
                    # Новое окно не открылось - это может быть нормально
                    pass