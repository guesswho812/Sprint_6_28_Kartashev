from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)
    
    def find_element(self, locator):
        """Найти элемент с ожиданием его видимости"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element
        except Exception as e:
            raise Exception(f"Element not found: {locator}, error: {e}")
    
    def find_element_clickable(self, locator):
        """Найти кликабельный элемент"""
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def scroll_to_element(self, locator):
        """Прокрутить страницу к элементу"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("window.scrollBy(0, -50);")
        return element
    
    def click_element(self, locator):
        """Кликнуть на элемент с прокруткой"""
        element = self.scroll_to_element(locator)
        self.driver.execute_script("arguments[0].click();", element)
    
    def input_text(self, locator, text):
        """Ввести текст в поле"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Получить текст элемента"""
        return self.find_element(locator).text
    
    def accept_cookies(self):
        """Принять куки если баннер присутствует"""
        cookie_button = ["id", "rcc-confirm-button"]
        try:
            self.click_element(cookie_button)
        except:
            # Баннер куки не найден - это нормально
            pass