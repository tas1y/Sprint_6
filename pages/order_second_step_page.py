import allure
from locators.order_second_step_locators import OrderSecondStepLocators as OSSL
from pages.base_page import BasePage as BP

class OrderSecondPage(BP):
    
    @allure.step('Выбор даты аренды из календаря')
    def select_calendar_date(self):
        self.click_on_element(OSSL.DATE_FIELD)
        self.click_on_element(OSSL.CHOOSE_DATE)

    @allure.step('Выбор продолжительноси аренды')
    def select_rent_duration(self):
        self.click_on_element(OSSL.RENT_DURATION_DROPDOWN)
        self.click_on_element(OSSL.RENT_DURATION_OPTION)

    @allure.step('Выбор цвета самоката: {color_name}')
    def select_scooter_color(self, color_name):
        method, locator_template = OSSL.COLOR_CHECKBOX
        locator = locator_template.format(color_name)
        self.click_on_element((method, locator))

    @allure.step('Ввод комментария: "{comment}"')
    def enter_commnet(self, comment):
        self.set_text_to_form(OSSL.COMMENT_FIELD, comment)

    @allure.step('Заполнение формы деталей заказа данными')
    def fill_order_details_and_submit(self, color_name, comment):
        self.select_calendar_date()
        self.select_rent_duration()
        self.select_scooter_color(color_name)
        self.enter_commnet(comment)
        self.click_on_element(OSSL.ORDER_BUTTON)
        self.click_on_element(OSSL.CONFIRM_BUTTON)

    @allure.step('Получение текста подтверждения заказа')
    def get_order_confirmation_text(self):
        element = self.wait_for_visible_element(OSSL.ORDER_COMPLETE)
        return self.get_text_from_element(element)
