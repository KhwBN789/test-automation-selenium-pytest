"""
These tests cover navigattion to home page and shop page.
"""

from pages.navigate import DesignHomePage
from pages.result import ShopPage


def test_basic_homedesign_navigation(browser):
  navigate_page = DesignHomePage(browser)
  result_page = ShopPage(browser)
  PAGE_NAME = "BOUTIQUE"
  
  # Given the home page is displayed
  navigate_page.load()

  # When the user navigates to "boutique" page
  navigate_page.navigate()

  # Then the result page title contains "BOUTIQUE"
  assert PAGE_NAME in result_page.title()

  # And the result page contains categories titles 
  titles = result_page.category_titles()
  f = open("titles.txt", "w")
  f.write('\n'.join(title.text for title in titles))
  f.close()
  
  # And the result page contains price values
  values = result_page.price_values()
  f = open("values.txt", "w")
  f.write('\n'.join(value.text for value in values))
  f.close()
