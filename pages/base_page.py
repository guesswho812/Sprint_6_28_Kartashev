from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import allure
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)
    
    @allure.step("Найти элемент: {locator}")
    def find_element(self, locator):
        """Найти элемент с ожиданием его видимости"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element
        except Exception as e:
            raise Exception(f"Element not found: {locator}, error: {e}")
    
    @allure.step("Найти кликабельный элемент: {locator}")
    def find_element_clickable(self, locator):
        """Найти кликабельный элемент"""
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    @allure.step("Прокрутить страницу к элементу: {locator}")
    def scroll_to_element(self, locator):
        """Прокрутить страницу к элементу"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("window.scrollBy(0, -50);")
        return element
    
    @allure.step("Кликнуть на элемент: {locator}")
    def click_element(self, locator):
        """Кликнуть на элемент с прокруткой"""
        element = self.scroll_to_element(locator)
        self.driver.execute_script("arguments[0].click();", element)
    
    @allure.step("Ввести текст '{text}' в поле: {locator}")
    def input_text(self, locator, text):
        """Ввести текст в поле"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator):
        """Получить текст элемента"""
        return self.find_element(locator).text
    
    @allure.step("Принять куки если баннер присутствует")
    def accept_cookies(self):
        """Принять куки если баннер присутствует"""
        cookie_button = ["id", "rcc-confirm-button"]
        try:
            self.click_element(cookie_button)
        except:
            # Баннер куки не найден - это нормально
            pass
    
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        """Получить текущий URL страницы"""
        return self.driver.current_url
    
    @allure.step("Переключиться на окно: {window_handle}")
    def switch_to_window(self, window_handle):
        """Переключиться на указанное окно"""
        self.driver.switch_to.window(window_handle)
    
    @allure.step("Получить список всех окон")
    def get_window_handles(self):
        """Получить список всех окон"""
        return self.driver.window_handles
    
    @allure.step("Закрыть текущее окно")
    def close_current_window(self):
        """Закрыть текущее окно"""
        self.driver.close()
    
    @allure.step("Получить текущее окно")
    def get_current_window_handle(self):
        """Получить handle текущего окна"""
        return self.driver.current_window_handle
    
    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self):
        """Переключиться на новое окно"""
        windows = self.driver.window_handles
        if len(windows) > 1:
            self.driver.switch_to.window(windows[-1])
            return True
        return False
    
    @allure.step("Ждать открытия нового окна")
    def wait_for_new_window(self, original_window, timeout=10):
        """Ждать открытия нового окна"""
        start_time = time.time()
        while time.time() - start_time < timeout:
            if len(self.driver.window_handles) > 1:
                return True
            time.sleep(0.5)
        return False
    
    @allure.step("Ждать пока URL содержит '{text}'")
    def wait_for_url_contains(self, text, timeout=10):
        """Ждать пока URL содержит указанный текст"""
        try:
            return self.wait.until(EC.url_contains(text))
        except TimeoutException:
            return False