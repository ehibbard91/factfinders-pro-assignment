import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("browser", ["chrome", "firefox", "edge"])
def test_homepage_title(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()

    driver.get("https://www.topcashback.com")
    print(f"Homepage title on {browser}:", driver.title)
    driver.quit()

@pytest.mark.parametrize("browser", ["chrome", "firefox", "edge"])
def test_login_page_title(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()

    driver.get("https://www.topcashback.com")
    sign_in_button = driver.find_element(By.XPATH, '//*[@id="ctl00_BodyMain_SignINButton"]')
    sign_in_button.click()
    print(f"Login page title on {browser}:", driver.title)
    driver.quit()

