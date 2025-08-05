from selenium.webdriver.common.by import By


class OrderSecondStepLocators:
    DATE_FIELD = By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'
    CHOOSE_DATE = By.CLASS_NAME, 'react-datepicker__day--today'
    RENT_DURATION_DROPDOWN = By.CLASS_NAME, "Dropdown-control"
    RENT_DURATION_OPTION = By.XPATH, './/div[@class = "Dropdown-option" and text()="двое суток"]'
    COLOR_CHECKBOX = By.XPATH, './/input[@id="{}"]/parent::label'
    BLACK_COLOR = By.ID, 'black'
    COMMENT_FIELD = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    ORDER_BUTTON = By.XPATH, './/*[contains(@class,"Order_Buttons")]//button[text()="Заказать"]'
    CONFIRM_BUTTON = By.XPATH, './/button[text()="Да"]'
    ORDER_COMPLETE = By.XPATH, './/*[contains(@class,"Order_ModalHeader")]'
