import pytest
import allure
from pages.main_page import MainPage as MP
from data import FAQ_EXPECTED_ANSWERS


class TestFAQ:

    @allure.title('Проверка раздела FAQ, на соответсвие вопрос-ответ')
    @allure.description('Тест: по нажатию на стрелочку, появляется соответвующий текст')
    @pytest.mark.parametrize("index, expected", list(enumerate(FAQ_EXPECTED_ANSWERS)))
    def test_faq_dropdown(self, driver, index, expected):

        page = MP(driver)

        page.scroll_to_bottom_page()
        page.click_faq_question(index)
        text = page.get_faq_answer_text(index)
        assert expected in text
