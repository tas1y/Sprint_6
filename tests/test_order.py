import allure
import pytest
from pages.main_page import MainPage as MP
from pages.order_page import OrderPage as OP
from pages.order_second_step_page import OrderSecondPage as OSP
from data import OrderData as OD
from locators.main_page_locators import MainPageLocators as MPL


class TestOrderPage:

    @allure.title('Проверка флоу позитивного сценария оформления заказа')
    @allure.description('Тесты оформления заказа из двух точек входа')
    @pytest.mark.parametrize(
        'entry_point, user_data, order_details',
        [
            (MPL.TOP_ORDER_BUTTON, OD.user_order_1, OD.user_second_order_1),
            (MPL.BOTTOM_ORDER_BUTTON, OD.user_order_2, OD.user_second_order_2),
        ]
    )
    def test_successful_order_flow(self, driver, entry_point, user_data, order_details):
        main_page = MP(driver)
        order_page = OP(driver)
        order_second_page = OSP(driver)

        main_page.click_cookie_button()
        order_page.click_on_element(entry_point)
        order_page.wait_for_first_name_field()
        order_page.fill_user_data_form(
            user_data.name,
            user_data.last_name,
            user_data.address,
            user_data.metro,
            user_data.phone)
        order_second_page.fill_order_details_and_submit(
            order_details.color,
            order_details.comment)
        confirmation_text = order_second_page.get_order_confirmation_text()
        assert 'Заказ оформлен' in confirmation_text
