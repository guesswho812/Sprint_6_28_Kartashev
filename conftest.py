import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import os


@pytest.fixture(scope="function")
def driver():
    # Настройка Firefox опций
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    
    try:
        # Поиск geckodriver
        geckodriver_paths = [
            "C:\\WebDriver\\bin\\geckodriver.exe",
            "C:\\Program Files\\Mozilla Firefox\\geckodriver.exe",
            "geckodriver.exe",
        ]
        
        service = None
        for path in geckodriver_paths:
            if os.path.exists(path):
                service = Service(executable_path=path)
                print(f"Используем geckodriver: {path}")
                break
        
        if service is None:
            service = Service()
            print("Используем системный geckodriver")
        
        driver = webdriver.Firefox(service=service, options=options)
        driver.implicitly_wait(10)
        driver.maximize_window()
        
        yield driver
        
        driver.quit()
        
    except Exception as e:
        print(f"Ошибка при запуске драйвера: {e}")
        raise


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Хук для скриншотов при падении тестов"""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )