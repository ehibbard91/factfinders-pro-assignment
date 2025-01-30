import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_home_page_title(driver):
    driver.get("https://www.topcashback.com/")
    title = driver.title
    print("Home page title:", title)
    # assert title == "Expected home page title", f"Expected 'Expected home page title', but got '{title}'"

def test_login_page_title(driver):
    driver.get("https://www.topcashback.com/")
    sign_in_button = driver.find_element(By.XPATH, '//*[@id="ctl00_BodyMain_SignINButton"]')
    sign_in_button.click()
    login_page_title = driver.title
    print("Login page title:", login_page_title)
    # assert login_page_title == "Expected Login Page Title", f"Expected 'Expected Login Page Title', but got '{login_page_title}'"