from selenium.webdriver.common.by import By


class MainPageLocators:

    FAQ_QUESTIONS = By.ID, 'accordion__heading-{}'
    FAQ_ANSWERS = By.ID, 'accordion__panel-{}'
    COOKIE_BUTTON = By.ID, 'rcc-confirm-button'
    TOP_ORDER_BUTTON = By.XPATH, './/div[contains(@class,"Header_Nav")]//button[text()="Заказать"]'
    BOTTOM_ORDER_BUTTON = By.XPATH, './/div[contains(@class,"Home_FinishButton")]//button[text()="Заказать"]'
