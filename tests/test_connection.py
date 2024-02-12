"""
These tests cover user connection.
"""
import time
from pages.connection import ConnexionPage
from pages.admin import AdminPage


def test_connection(browser):
  connection_page = ConnexionPage(browser)
  admin_page = AdminPage(browser)
  USER_NAME = "admin"
  USER_PASSWORD = "admin"
  PAGE_NAME = "DASHBOARD"
  
  # Given the connection page is displayed
  connection_page.load()

  # When the user signin 
  connection_page.enter_username(USER_NAME)
  connection_page.enter_password(USER_PASSWORD)
  connection_page.signin()
  time.sleep(3)

  # Then the result page title contains "dashboard"
  assert PAGE_NAME in admin_page.title()

  # And the user can logout from dashboard page
  admin_page.logout()
