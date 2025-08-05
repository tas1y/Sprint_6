from selenium.webdriver.common.by import By


class MainPageLocators:

    FAQ_QUESTIONS = By.XPATH, "//div[contains(@class,'accordion__button')]"
    FAQ_ANSWERS = By.XPATH, "//div[contains(@class,'accordion__panel')]"
    COOKIE_BUTTON = By.ID, 'rcc-confirm-button'
    TOP_ORDER_BUTTON = By.XPATH, './/div[contains(@class,"Header_Nav")]//button[text()="Заказать"]'
    BOTTOM_ORDER_BUTTON = By.XPATH, './/div[contains(@class,"Home_FinishButton")]//button[text()="Заказать"]'
