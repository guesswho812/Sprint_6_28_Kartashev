from .base_page import BasePage
from config.urls import BASE_URL


class MainPage(BasePage):
    # Локаторы вопросов
    QUESTION_1 = ["id", "accordion__heading-0"]
    QUESTION_2 = ["id", "accordion__heading-1"]
    QUESTION_3 = ["id", "accordion__heading-2"]
    QUESTION_4 = ["id", "accordion__heading-3"]
    QUESTION_5 = ["id", "accordion__heading-4"]
    QUESTION_6 = ["id", "accordion__heading-5"]
    QUESTION_7 = ["id", "accordion__heading-6"]
    QUESTION_8 = ["id", "accordion__heading-7"]
    
    ANSWER_1 = ["id", "accordion__panel-0"]
    ANSWER_2 = ["id", "accordion__panel-1"]
    ANSWER_3 = ["id", "accordion__panel-2"]
    ANSWER_4 = ["id", "accordion__panel-3"]
    ANSWER_5 = ["id", "accordion__panel-4"]
    ANSWER_6 = ["id", "accordion__panel-5"]
    ANSWER_7 = ["id", "accordion__panel-6"]
    ANSWER_8 = ["id", "accordion__panel-7"]
    
    # Кнопки заказа
    ORDER_BUTTON_TOP = ["xpath", "//button[text()='Заказать' and not(contains(@class, 'UltraBig'))]"]
    ORDER_BUTTON_BOTTOM = ["xpath", "//button[text()='Заказать' and contains(@class, 'UltraBig')]"]
    
    # Логотипы
    SCOOTER_LOGO = ["xpath", "//img[@alt='Scooter']"]
    YANDEX_LOGO = ["xpath", "//img[@alt='Yandex']"]
    
    def open_main_page(self):
        """Открыть главную страницу и принять куки"""
        self.driver.get(BASE_URL)
        self.accept_cookies()
    
    def click_question(self, question_number):
        """Клик на вопрос по номеру (1-8)"""
        locator = getattr(self, f"QUESTION_{question_number}")
        self.click_element(locator)
    
    def get_answer_text(self, answer_number):
        """Получить текст ответа по номеру (1-8)"""
        locator = getattr(self, f"ANSWER_{answer_number}")
        return self.get_text(locator)
    
    def click_order_button_top(self):
        """Кликнуть верхнюю кнопку заказа"""
        self.click_element(self.ORDER_BUTTON_TOP)
    
    def click_order_button_bottom(self):
        """Кликнуть нижнюю кнопку заказа"""
        self.click_element(self.ORDER_BUTTON_BOTTOM)
    
    def click_scooter_logo(self):
        """Кликнуть логотип Самоката"""
        self.click_element(self.SCOOTER_LOGO)
    
    def click_yandex_logo(self):
        """Кликнуть логотип Яндекса"""
        self.click_element(self.YANDEX_LOGO)