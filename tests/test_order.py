import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.epic("Яндекс.Самокат")
@allure.feature("Заказ самоката")
class TestOrder:
    @allure.title("Заказ самоката через {order_button} кнопку")
    @allure.story("Полный флоу позитивного сценария заказа")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("order_button,name,surname,address,phone", [
        ("верхнюю", "Иван", "Иванов", "Москва, Красная площадь", "89991112233"),
        ("нижнюю", "Петр", "Петров", "Санкт-Петербург, Невский проспект", "89994445566")
    ])
    def test_scooter_order_positive_flow(self, driver, order_button, name, surname, address, phone):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()
        
        with allure.step(f"Нажать {order_button} кнопку 'Заказать'"):
            if order_button == "верхнюю":
                main_page.click_order_button_top()
            else:
                main_page.click_order_button_bottom()
        
        with allure.step("Заполнить данные клиента"):
            order_page.fill_customer_info(name, surname, address, phone)
            order_page.select_metro_station("Алек")
            order_page.click_next()
        
        with allure.step("Заполнить данные аренды"):
            order_page.fill_rental_info(
                rental_period_text="сутки",
                color="black",
                comment="Тестовый заказ"
            )
            order_page.click_order()
        
        with allure.step("Подтвердить заказ"):
            order_page.confirm_order()
        
        with allure.step("Проверить успешное оформление"):
            success_text = order_page.get_success_text()
            assert "Заказ оформлен" in success_text