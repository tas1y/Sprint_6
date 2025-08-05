import allure
from locators.order_page_locators import OrderPageLocators as OPL
from pages.base_page import BasePage as BP


class OrderPage(BP):

    def enter_first_name(self, name):
        self.set_text_to_form(OPL.FIRST_NAME_INPUT, name)

    @allure.step('Ожидаем появления поля "Имя"')
    def wait_for_first_name_field(self):
        self.wait_for_visible_element(OPL.FIRST_NAME_INPUT)

    def enter_last_name(self, last_name):
        self.set_text_to_form(OPL.LAST_NAME_INPUT, last_name)

    def enter_address(self, address):
        self.set_text_to_form(OPL.ADDRESS_INPUT, address)

    def select_metro_station(self, metro):
        self.click_on_element(OPL.METRO_FIELD)
        method, locator = OPL.METRO_OPTION
        locator = locator.format(metro)
        self.scroll_and_click_with_wait((method, locator))

    def enter_phone_number(self, phone_number):
        self.set_text_to_form(OPL.PHONE_INPUT, phone_number)

    @allure.step('Заполняем форму данными пользователя')
    def fill_user_data_form(self, name, last_name, address, metro, phone_number):
        self.enter_first_name(name)
        self.enter_last_name(last_name)
        self.enter_address(address)
        self.select_metro_station(metro)
        self.enter_phone_number(phone_number)
        self.click_on_element(OPL.NEXT_BUTTON)
