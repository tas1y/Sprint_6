from selenium.webdriver.common.by import By


class OrderPageLocators:
    FIRST_NAME_INPUT = By.XPATH, './/input[@placeholder="* Имя"]'
    LAST_NAME_INPUT = By.XPATH, './/input[@placeholder="* Фамилия"]'
    ADDRESS_INPUT = By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]'
    METRO_FIELD = By.CSS_SELECTOR, 'input[placeholder="* Станция метро"]'
    METRO_OPTION = By.XPATH, '//div[text()="{}"]'
    PHONE_INPUT = By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]'
    NEXT_BUTTON = By.XPATH, './/button[text()="Далее"]'
