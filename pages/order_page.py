from pages.base_page import BasePage
from config.urls import BASE_URL
import allure


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = BASE_URL + "order"
    
    # ЛОКАТОРЫ
    NAME_FIELD = ["xpath", "//input[@placeholder='* Имя']"]
    SURNAME_FIELD = ["xpath", "//input[@placeholder='* Фамилия']"] 
    ADDRESS_FIELD = ["xpath", "//input[@placeholder='* Адрес: куда привезти заказ']"]
    PHONE_FIELD = ["xpath", "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    METRO_FIELD = ["xpath", "//input[@placeholder='* Станция метро']"]
    METRO_OPTION = ["xpath", "//li[@class='select-search__row']"]
    NEXT_BUTTON = ["xpath", "//button[text()='Далее']"]
    DATE_FIELD = ["xpath", "//input[@placeholder='* Когда привезти самокат']"]
    DATE_DAY = ["xpath", "//div[contains(@class, 'react-datepicker__day') and text()='2']"]
    RENTAL_DROPDOWN = ["xpath", "//div[@class='Dropdown-placeholder' and contains(text(), 'Срок аренды')]"]
    COMMENT_FIELD = ["xpath", "//input[@placeholder='Комментарий для курьера']"]
    ORDER_BUTTON = ["xpath", "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']"]
    CONFIRM_BUTTON = ["xpath", "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Да']"]
    SUCCESS_TEXT = ["xpath", "//div[contains(@class, 'Order_ModalHeader')]"]

    def open_order_page(self):
        """Открыть страницу заказа"""
        self.driver.get(self.url)
    
    @allure.step("Заполнить данные клиента: {name} {surname}")
    def fill_customer_info(self, name, surname, address, phone):
        """Заполнить данные клиента"""
        self.input_text(self.NAME_FIELD, name)
        self.input_text(self.SURNAME_FIELD, surname)
        self.input_text(self.ADDRESS_FIELD, address)
        self.input_text(self.PHONE_FIELD, phone)
    
    @allure.step("Выбрать станцию метро: {station_partial_name}")
    def select_metro_station(self, station_partial_name):
        """Выбрать станцию метро по части названия"""
        metro_field = self.find_element(self.METRO_FIELD)
        metro_field.click()
        # Ждем появления выпадающего списка
        self.find_element(self.METRO_OPTION)
        metro_field.send_keys(station_partial_name)
        # Ждем появления нужного варианта
        station_option = self.find_element(self.METRO_OPTION)
        station_option.click()
    
    @allure.step("Нажать кнопку 'Далее'")
    def click_next(self):
        """Нажать кнопку 'Далее'"""
        self.click_element(self.NEXT_BUTTON)
    
    @allure.step("Заполнить данные аренды: период={rental_period_text}, цвет={color}")
    def fill_rental_info(self, rental_period_text, color=None, comment=""):
        """Заполнить данные аренды"""
        # Дата
        date_field = self.find_element(self.DATE_FIELD)
        date_field.click()
        
        day_element = self.find_element(self.DATE_DAY)
        day_element.click()
        
        # Срок аренды
        dropdown = self.find_element(self.RENTAL_DROPDOWN)
        dropdown.click()
        
        option_locator = ["xpath", f"//div[@class='Dropdown-option' and text()='{rental_period_text}']"]
        option = self.find_element(option_locator)
        option.click()
        
        # Цвет
        if color:
            color_locator = ["xpath", f"//input[@id='{color}']"]
            color_checkbox = self.find_element(color_locator)
            color_checkbox.click()
        
        # Комментарий
        if comment:
            self.input_text(self.COMMENT_FIELD, comment)
    
    @allure.step("Нажать кнопку 'Заказать'")
    def click_order(self):
        """Нажать кнопку 'Заказать'"""
        self.scroll_to_element(self.ORDER_BUTTON)
        self.click_element(self.ORDER_BUTTON)
    
    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        """Подтвердить заказ в модальном окне"""
        self.click_element(self.CONFIRM_BUTTON)
    
    @allure.step("Получить текст успешного заказа")
    def get_success_text(self):
        """Получить текст успешного заказа"""
        return self.get_text(self.SUCCESS_TEXT)