"""
This module contains ShopPage,
the page object for the result page after navigating fom homedesign page.
"""

from selenium.webdriver.common.by import By


class ShopPage:

  #LOCATORS

  CATEGORY_TITLES = (By.CSS_SELECTOR, '.design-category')

  PRICE = (By.CSS_SELECTOR, '.product-price')
  
  # Interaction Methods

  def __init__(self, browser):
    self.browser = browser

  def category_titles(self):
    categories = self.browser.find_elements(*self.CATEGORY_TITLES)
    return categories
  
  def price_values(self):
    prices = self.browser.find_elements(*self.PRICE)
    return prices

  def title(self):
    return self.browser.title
 