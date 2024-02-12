"""
This module contains ConnexionPage.
"""

from selenium.webdriver.common.by import By


class ConnexionPage:

  # URL

  URL = 'https://khwbn789.github.io/site-web-home-design/connexion.html'

  # LOCATORS

  USERNAME = (By.ID, 'name')
  PASSWORD = (By.ID, 'pwd')
  SIGNIN = (By.XPATH, '/html/body/div/form/div[7]/button')
  ALLERT_ERROR = (By.ID, 'alert-error')

  # Initializer

  def __init__(self, browser):
    self.browser = browser

  # Intercation Methods
    
  def load(self):
    self.browser.get(self.URL)
    
  
  def enter_username(self, name):
    username_input = self.browser.find_element(*self.USERNAME)
    username_input.clear()
    username_input.send_keys(name)


  def enter_password(self, p_word):
    password_input = self.browser.find_element(*self.PASSWORD)
    password_input.clear()
    password_input.send_keys(p_word)
    

  def signin(self):
    login_btn = self.browser.find_element(*self.SIGNIN)
    login_btn.click()


  def wrong_login(self, user):
    username_input = self.browser.find_element(*self.USERNAME)
    password_input = self.browser.find_element(*self.PASSWORD)
    username_input.clear()
    username_input.send_keys(user[0])
    password_input.clear()
    password_input.send_keys(user[1])
    self.signin()

  def error(self):
    alert_error = self.browser.find_element(*self.ALLERT_ERROR)
    print("Error message is:", alert_error.text)
    self.browser.save_screenshot('error_message.png')
