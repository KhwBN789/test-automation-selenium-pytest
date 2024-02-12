"""
These tests cover user connection error.
"""

from pages.connection import ConnexionPage


def test_connection_error(browser):
  connection_page = ConnexionPage(browser)
  USER = ("admnn", "12345")

  # Given the connection page is displayed
  connection_page.load()

  # When the user enters incorrect username and password and tries to signin
  connection_page.wrong_login(USER)

  # Then verify the error message is appeared
  connection_page.error()
    
