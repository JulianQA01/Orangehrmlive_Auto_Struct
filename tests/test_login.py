import pytest
import time

from utils.driver import get_driver, close_driver
from page_objects.login_page import LoginPage

@pytest.fixture
def setup():
    driver = get_driver()
    yield driver
    close_driver(driver)

def test_valid_login(setup):
    driver = setup
    login_page = LoginPage(driver)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") 
    
    # wait until link is fully visible
    login_page.link_fully_visible()
    print("URL is fully loaded and visible!")
    
    # Enter valid username & pwd
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    
    # click login btn
    login_page.click_login()
    
    # assert successfully login and then redirect to dashboard
    login_page.login_link_visible()
    time.sleep(5)
    assert driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"


def test_invalid_login(setup):
    driver = setup
    login_page = LoginPage(driver)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
  
    # Enter valid username and invalid pwd
    login_page.enter_username("Admin")
    login_page.enter_password("wrong01password")

    # click login btn
    login_page.click_login()

    # assert err msg displayed
    err_msg = login_page.get_error_message()
    assert err_msg == "Invalid credentials"