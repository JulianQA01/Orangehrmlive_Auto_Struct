from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

  def __init__(self, driver):
    self.driver = driver
    self.username_field = (By.NAME, "username")
    self.password_field = (By.NAME, "password")
    self.login_button = (By.CSS_SELECTOR, "button.oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button")
    self.error_message = (By.CSS_SELECTOR, "p.oxd-text.oxd-text--p.oxd-alert-content-text")

  def link_fully_visible(self):
      WebDriverWait(self.driver, 10).until(
    EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
)

  def enter_username(self, username):
      WebDriverWait(self.driver,10).until(
         EC.visibility_of_element_located(self.username_field)
         ).send_keys(username)

  def enter_password(self, password):
      WebDriverWait(self.driver,10).until(
         EC.visibility_of_element_located(self.password_field)
         ).send_keys(password)

  def click_login(self):
     WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(self.login_button)
     ).click()

  def login_link_visible(self):
      WebDriverWait(self.driver, 10).until(
         EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
      )

  def get_error_message(self):
      return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.error_message)
        ).text  
      # Invalid credentials