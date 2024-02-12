"""
This module contains shared fixtures.
"""

import pytest
from selenium import webdriver


@pytest.fixture
def browser():

  # Initialize the ChromeDriver instance
  b = webdriver.Chrome()

  # Make its calls wait up to 10 seconds for elements to appear
  b.implicitly_wait(10)

  # Maximize the window
  b.maximize_window()

  # Return the WebDriver instance for the setup
  yield b

  # Quit the WebDriver instance for the cleanup
  b.quit()
  