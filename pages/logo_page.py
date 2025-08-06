import allure
from locators.logo_page_locators import LogoPageLocators as LPL
from locators.main_page_locators import MainPageLocators as MPL
from pages.base_page import BasePage as BP


class LogoPage(BP):

    @allure.step('Клик по лого "Яндекс"')
    def click_on_yandex_logo(self):
        self.click_on_element(LPL.YANDEX_LOGO)

    @allure.step('Клик по лого "Самокат"')
    def click_on_scooter_logo(self):
        self.click_on_element(LPL.SCOOTER_LOGO)
        self.wait_for_visible_element(MPL.TOP_ORDER_BUTTON)
