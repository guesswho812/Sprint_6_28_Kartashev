import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.test_data import RENTAL_DATA, METRO_STATIONS


@allure.epic("Яндекс.Самокат")
@allure.feature("Заказ самоката")
class TestOrder:
    
    @allure.title("Заказ самоката через верхнюю кнопку - Иван Иванов")
    @allure.story("Полный флоу позитивного сценария заказа")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_scooter_order_through_top_button_ivan(self, driver):
        """Тест заказа через верхнюю кнопку для Ивана Иванова"""
        self._execute_order_flow_top(driver, "Иван", "Иванов", "Москва, Красная площадь", "89991112233")
    
    @allure.title("Заказ самоката через верхнюю кнопку - Петр Петров")  
    @allure.story("Полный флоу позитивного сценария заказа")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_scooter_order_through_top_button_petr(self, driver):
        """Тест заказа через верхнюю кнопку для Петра Петрова"""
        self._execute_order_flow_top(driver, "Петр", "Петров", "Санкт-Петербург, Невский проспект", "89994445566")
    
    @allure.title("Заказ самоката через нижнюю кнопку - Иван Иванов")
    @allure.story("Полный флоу позитивного сценария заказа")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_scooter_order_through_bottom_button_ivan(self, driver):
        """Тест заказа через нижнюю кнопку для Ивана Иванова"""
        self._execute_order_flow_bottom(driver, "Иван", "Иванов", "Москва, Красная площадь", "89991112233")
    
    @allure.title("Заказ самоката через нижнюю кнопку - Петр Петров")
    @allure.story("Полный флоу позитивного сценария заказа")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_scooter_order_through_bottom_button_petr(self, driver):
        """Тест заказа через нижнюю кнопку для Петра Петрова"""
        self._execute_order_flow_bottom(driver, "Петр", "Петров", "Санкт-Петербург, Невский проспект", "89994445566")
    
    def _execute_order_flow_top(self, driver, name, surname, address, phone):
        """Флоу заказа через верхнюю кнопку"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()
        
        with allure.step("Нажать верхнюю кнопку 'Заказать'"):
            main_page.click_order_button_top()
        
        with allure.step("Заполнить данные клиента"):
            order_page.fill_customer_info(name, surname, address, phone)
            order_page.select_metro_station(METRO_STATIONS["александровский_сад"])
            order_page.click_next()
        
        with allure.step("Заполнить данные аренды"):
            order_page.fill_rental_info(
                rental_period_text=RENTAL_DATA["rental_period"],
                color=RENTAL_DATA["color"],
                comment=RENTAL_DATA["comment"]
            )
            order_page.click_order()
        
        with allure.step("Подтвердить заказ"):
            order_page.confirm_order()
        
        with allure.step("Проверить успешное оформление"):
            success_text = order_page.get_success_text()
            assert "Заказ оформлен" in success_text, f"Ожидался текст 'Заказ оформлен', получен: {success_text}"
    
    def _execute_order_flow_bottom(self, driver, name, surname, address, phone):
        """Флоу заказа через нижнюю кнопку"""  
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()
        
        with allure.step("Нажать нижнюю кнопку 'Заказать'"):
            main_page.click_order_button_bottom()
        
        with allure.step("Заполнить данные клиента"):
            order_page.fill_customer_info(name, surname, address, phone)
            order_page.select_metro_station(METRO_STATIONS["александровский_сад"])
            order_page.click_next()
        
        with allure.step("Заполнить данные аренды"):
            order_page.fill_rental_info(
                rental_period_text=RENTAL_DATA["rental_period"],
                color=RENTAL_DATA["color"],
                comment=RENTAL_DATA["comment"]
            )
            order_page.click_order()
        
        with allure.step("Подтвердить заказ"):
            order_page.confirm_order()
        
        with allure.step("Проверить успешное оформление"):
            success_text = order_page.get_success_text()
            assert "Заказ оформлен" in success_text, f"Ожидался текст 'Заказ оформлен', получен: {success_text}"