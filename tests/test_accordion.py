import allure
import pytest
from pages.main_page import MainPage
from data.test_data import ACCORDION_DATA


@allure.epic("Яндекс.Самокат")
@allure.feature("Аккордеон с вопросами")
class TestAccordion:
    @allure.title("Проверка аккордеона: вопрос №{question_number}")
    @allure.story("Открытие ответов на вопросы")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("question_number,expected_answer", ACCORDION_DATA)
    def test_accordion_question_opens_correct_answer(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)
        
        with allure.step("Открыть главную страницу и принять куки"):
            main_page.open_main_page()
        
        with allure.step(f"Кликнуть на вопрос №{question_number}"):
            main_page.click_question(question_number)
        
        with allure.step("Проверить текст ответа"):
            actual_answer = main_page.get_answer_text(question_number)
            assert actual_answer == expected_answer, f"Ожидался: {expected_answer}, Получен: {actual_answer}"