import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.test_data import RENTAL_DATA, METRO_STATIONS


@allure.epic("Яндекс.Самокат")
@allure.feature("Заказ самоката")
class TestOrder:
    
    @allure.title("Заказ самоката - {entry_point} кнопка, {name} {surname}")
    @allure.story("Полный флоу позитивного сценария заказа")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("entry_point,name,surname,address,phone", [
        ("верхняя", "Иван", "Иванов", "Москва, Красная площадь", "89991112233"),
        ("верхняя", "Петр", "Петров", "Санкт-Петербург, Невский проспект", "89994445566"),
        ("нижняя", "Иван", "Иванов", "Москва, Красная площадь", "89991112233"),
        ("нижняя", "Петр", "Петров", "Санкт-Петербург, Невский проспект", "89994445566")
    ])
    def test_scooter_order(self, driver, entry_point, name, surname, address, phone):
        """Параметризованный тест заказа самоката"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()
        
        with allure.step(f"Нажать {entry_point} кнопку 'Заказать'"):
            if entry_point == "верхняя":
                main_page.click_order_button_top()
            else:
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