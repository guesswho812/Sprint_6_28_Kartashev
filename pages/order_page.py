from pages.base_page import BasePage
import time


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://qa-scooter.praktikum-services.ru/order"
    
    def open_order_page(self):
        """Открыть страницу заказа"""
        self.driver.get(self.url)
    
    def fill_customer_info(self, name, surname, address, phone):
        """Заполнить данные клиента"""
        self.driver.find_element("xpath", "//input[@placeholder='* Имя']").send_keys(name)
        self.driver.find_element("xpath", "//input[@placeholder='* Фамилия']").send_keys(surname)
        self.driver.find_element("xpath", "//input[@placeholder='* Адрес: куда привезти заказ']").send_keys(address)
        self.driver.find_element("xpath", "//input[@placeholder='* Телефон: на него позвонит курьер']").send_keys(phone)
    
    def select_metro_station(self, station_partial_name):
        """Выбрать станцию метро по части названия"""
        metro_field = self.driver.find_element("xpath", "//input[@placeholder='* Станция метро']")
        metro_field.click()
        time.sleep(1)
        
        metro_field.send_keys(station_partial_name)
        time.sleep(1)
        
        station_option = self.driver.find_element("xpath", "//li[@class='select-search__row']")
        station_option.click()
    
    def click_next(self):
        """Нажать кнопку 'Далее'"""
        next_button = self.driver.find_element("xpath", "//button[text()='Далее']")
        next_button.click()
        time.sleep(3)
    
    def fill_rental_info(self, rental_period_text, color=None, comment=""):
        """Заполнить данные аренды"""
        # Поле даты
        try:
            date_field = self.driver.find_element("xpath", "//input[@placeholder='* Когда привезти самокат']")
            date_field.click()
            time.sleep(2)
            
            day_element = self.driver.find_element("xpath", "//div[contains(@class, 'react-datepicker__day') and text()='2']")
            day_element.click()
            time.sleep(1)
        except Exception as e:
            raise Exception(f"Ошибка выбора даты: {e}")
        
        # Срок аренды
        try:
            dropdown = self.driver.find_element("xpath", "//div[@class='Dropdown-placeholder' and contains(text(), 'Срок аренды')]")
            dropdown.click()
            time.sleep(1)
            
            option = self.driver.find_element("xpath", f"//div[@class='Dropdown-option' and text()='{rental_period_text}']")
            option.click()
            time.sleep(1)
        except Exception as e:
            raise Exception(f"Ошибка выбора срока аренды: {e}")
        
        # Цвет
        if color:
            try:
                color_checkbox = self.driver.find_element("xpath", f"//input[@id='{color}']")
                color_checkbox.click()
            except Exception as e:
                raise Exception(f"Ошибка выбора цвета: {e}")
        
        # Комментарий
        if comment:
            try:
                comment_field = self.driver.find_element("xpath", "//input[@placeholder='Комментарий для курьера']")
                comment_field.send_keys(comment)
            except Exception as e:
                raise Exception(f"Ошибка ввода комментария: {e}")
    
    def click_order(self):
        """Нажать кнопку 'Заказать'"""
        time.sleep(2)
        
        try:
            order_button = self.driver.find_element("xpath", "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")
            self.driver.execute_script("arguments[0].scrollIntoView();", order_button)
            self.driver.execute_script("arguments[0].click();", order_button)
            time.sleep(3)
        except Exception as e:
            raise Exception(f"Ошибка нажатия кнопки 'Заказать': {e}")
    
    def confirm_order(self):
        """Подтвердить заказ в модальном окне"""
        time.sleep(3)
        
        try:
            confirm_button = self.driver.find_element("xpath", "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Да']")
            self.driver.execute_script("arguments[0].click();", confirm_button)
            time.sleep(3)
        except Exception as e:
            raise Exception(f"Ошибка подтверждения заказа: {e}")
    
    def get_success_text(self):
        """Получить текст успешного заказа"""
        try:
            success_element = self.driver.find_element("xpath", "//div[contains(@class, 'Order_ModalHeader')]")
            return success_element.text
        except:
            return "Текст успеха не найден"