import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.main_page_locators import MainPageLocators as MPL
from pages.base_page import BasePage as BP


class MainPage(BP):
    def go_to(self, link):
        self.driver.get(link)

    def get_faq_question_element(self, index):
        return self.driver.find_elements(*MPL.FAQ_QUESTIONS)[index]

    def get_faq_answer_element(self, index):
        return self.driver.find_elements(*MPL.FAQ_ANSWERS)[index]

    @allure.step('Клик по вопросу')
    def click_faq_question(self, index):
        elem = self.get_faq_question_element(index)
        WebDriverWait(self.driver, 10).until(EC.visibility_of(elem))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
        elem.click()
        answer = self.get_faq_answer_element(index)
        WebDriverWait(self.driver, 5).until(EC.visibility_of(answer))

    @allure.step('Получаем текст ответа')
    def get_faq_answer_text(self, index):
        elem = self.get_faq_answer_element(index)
        return elem.text

    @allure.step('Принимаем куки')
    def click_cookie_button(self, locator=MPL.COOKIE_BUTTON):
        self.wait_for_visible_element(locator)
        self.click_on_element(locator)

    @allure.step('Клик по кнопке "Заказать" сверху страницы')
    def click_order_button_in_top(self):
        self.wait_for_visible_element(MPL.TOP_ORDER_BUTTON).click()

    @allure.step('Клик по кнопке "Заказать" внизу страницы')
    def click_order_button_in_bottom(self):
        self.scroll_and_click_with_wait(MPL.BOTTOM_ORDER_BUTTON).click()
