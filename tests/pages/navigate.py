"""
This module contains DesignHomePage.
"""

from selenium.webdriver.common.by import By


class DesignHomePage:

  # URL

  URL = 'https://khwbn789.github.io/site-web-home-design/'

  # LOCATORS

  SHOP_BUTTON = (By.LINK_TEXT, 'BOUTIQUE')

  # Initializer

  def __init__(self, browser):
    self.browser = browser

  # Intercation Methods
    
  def load(self):
    self.browser.get(self.URL)
    
  
  def navigate(self):
    shop_btn = self.browser.find_element(*self.SHOP_BUTTON)
    shop_btn.click()
