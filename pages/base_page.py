import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import DZEN_URL


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть URL: {link}")
    def open_url(self, link):
        self.driver.get(link)

    @allure.step('Ожидание видимости элемента')
    def wait_for_visible_element(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу')
    def click_on_element(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @staticmethod
    @allure.step('Получение текста элемента')
    def get_text_from_element(element):
        return element.text

    @allure.step('Ввод текста в поле')
    def set_text_to_form(self, locator, text):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Прокрутка к элементу и клик')
    def scroll_and_click_with_wait(self, locator):
        self.driver.execute_script('arguments[0].scrollIntoView();', self.driver.find_element(*locator))
        self.click_on_element(locator)

    @allure.step('Прокрутка страницы вниз')
    def scroll_to_bottom_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step('Получение текущего URL')
    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    @allure.step('Переключение на новую вкладку')
    def switch_pages(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(EC.url_contains(DZEN_URL))
