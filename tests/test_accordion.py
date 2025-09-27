import allure
import pytest
from pages.main_page import MainPage


@allure.epic("Яндекс.Самокат")
@allure.feature("Аккордеон с вопросами")
class TestAccordion:
    @allure.title("Проверка аккордеона: вопрос №{question_number}")
    @allure.story("Открытие ответов на вопросы")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("question_number,expected_answer", [
        (1, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (2, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        (3, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        (4, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        (5, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        (6, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
        (7, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        (8, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
    ])
    def test_accordion_question_opens_correct_answer(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)
        
        with allure.step("Открыть главную страницу и принять куки"):
            main_page.open_main_page()
        
        with allure.step(f"Кликнуть на вопрос №{question_number}"):
            main_page.click_question(question_number)
        
        with allure.step("Проверить текст ответа"):
            actual_answer = main_page.get_answer_text(question_number)
            assert actual_answer == expected_answer, f"Ожидался: {expected_answer}, Получен: {actual_answer}"