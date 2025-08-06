import allure
from locators.main_page_locators import MainPageLocators as MPL
from pages.base_page import BasePage as BP


class MainPage(BP):

    @allure.step('Клик по вопросу')
    def click_faq_question(self, index):
        method, locator = MPL.FAQ_QUESTIONS
        locator = locator.format(index)
        self.wait_for_visible_element((method, locator))
        self.click_on_element((method, locator))

    @allure.step('Получаем текст ответа')
    def get_faq_answer_text(self, index):
        method, locator = MPL.FAQ_ANSWERS
        locator = locator.format(index)
        element = self.wait_for_visible_element((method, locator))
        return self.get_text_from_element(element)

    @allure.step('Принять cookies')
    def click_cookie_button(self, locator=MPL.COOKIE_BUTTON):
        self.wait_for_visible_element(locator)
        self.click_on_element(locator)

    @allure.step('Клик по кнопке "Заказать" в шапке страницы')
    def click_order_button_in_top(self):
        self.wait_for_visible_element(MPL.TOP_ORDER_BUTTON).click()

    @allure.step('Клик по кнопке "Заказать" снизу страницы')
    def click_order_button_in_bottom(self):
        self.scroll_and_click_with_wait(MPL.BOTTOM_ORDER_BUTTON).click()
