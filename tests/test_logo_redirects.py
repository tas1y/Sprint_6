import allure
from urls import BASE_URL, DZEN_URL
from pages.logo_page import LogoPage as LP
from pages.main_page import MainPage as MP
from pages.order_page import OrderPage as OP


class TestHeaderPage:

    @allure.title('Проверка перехода на главную страницу по нажатию на логотип "Самокат"')
    @allure.description('Выполняется переход со страницы заказа на главную по нажатию на логотип "Самокат"')
    def test_scooter_logo(self, driver):

        main_page = MP(driver)
        order_page = OP(driver)
        logo_page = LP(driver)

        main_page.click_cookie_button()
        main_page.click_order_button_in_top()
        order_page.wait_for_first_name_field()
        logo_page.click_on_scooter_logo()
        result_url = logo_page.get_current_url()
        assert result_url == BASE_URL


    @allure.title('Проверка открытие через редирект страницы Дзан по нажатию на логотип "Яндекс"')
    @allure.description('По нажатию на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена".')
    def test_yandex_logo(self, driver):

        main_page = MP(driver)
        logo_page = LP(driver)
        
        main_page.click_cookie_button()
        logo_page.click_on_yandex_logo()
        logo_page.switch_pages()
        result_url = logo_page.get_current_url()
        assert result_url == DZEN_URL
