"""
This module contains AdminPage.
"""

from selenium.webdriver.common.by import By


class AdminPage:

  #LOCATORS

  LOGOUT_BUTTON = (By.XPATH, '/html/body/nav/div[2]/ul/li[3]/a/img')
  
  # Initializer

  def __init__(self, browser):
    self.browser = browser
  
  # Interaction Methods

  def logout(self):
    logout_btn = self.browser.find_element(*self.LOGOUT_BUTTON)
    logout_btn.click()


  def title(self):
    return self.browser.title
 