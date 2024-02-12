# test-automation-selenium-pytest
This repository contains the companion project for the
*WebSite Automation using Selenium WebDriver with Python (and pytest)*
web site url : [Home Design](https://khwbn789.github.io/site-web-home-design/).
These tests contain basic Web UI test automation solution using Python and Selenium WebDriver.

# Setup Instructions

## Python Setup

It's required to install Python 3.8 or higher.
You can download the latest Python version from [Python.org](https://www.python.org/downloads/).

Also installing virtual environment is recommended.
To install venv, run `python3 -m venv virtual` from the command line:
Then activate it under your directory by running:
`source virtual/bin/activate`

You should also have a Python editor/IDE of your choice.
Good choices include [Visual Studio Code](https://code.visualstudio.com/docs/languages/python)
and [PyCharm](https://www.jetbrains.com/pycharm/).

## WebDriver Setup

For Web UI testing, need to install the latest versions of
[Google Chrome](https://www.google.com/chrome/)

Also need to install the latest versions of the WebDriver executables:
[ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) for Chrome

or run the following command from the command line (ubuntu):
`sudo apt-get install chromium-chromedriver`

## Project Setup

1. Clone this repository.
2. Run `cd test-automation-selenium-pytest` to enter the project.
3. Run `python3 -m venv virtual` to install venv.
4. Run `source virtual/bin/activate` to activate virtual environment
5. Run `pip install pytest` to install pytest framework then `pytest --version` to valid installation
6. Run `pip3 install selenium` to install Selenium WebDriver package for Python
7. Create a branch for your code changes.

# Writing Web UI Test

Test cases are written in [Gherkin](https://automationpanda.com/2017/01/26/bdd-101-the-gherkin-language/).

It consists of navigating from the Home page to the Shop page and retrieve the items prices displayed on the page.
Then validate the user's connection with a correct username and password, 
And finally check for an invalid connection and verify the displayed error message.

**page objects** are defined in this project (a Python package named `pages`) to make low-level Selenium WebDriver calls
so that tests can make short, readable calls instead of complex ones.


# Running Tests

To run the tests, type the following command:
`pytest tests`

And to run a specific test case, type the indicated test, for example:
`pytest tests/test_error_connection.py`

* titles.txt, values.txt and error_message.png are outputs after running the tests.
