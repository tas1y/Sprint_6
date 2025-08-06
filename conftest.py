import pytest
from urls import BASE_URL
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()