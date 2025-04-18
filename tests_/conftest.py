from pytest import fixture
from time import sleep
from selenium import webdriver
from pages.a_loginpage import LoginPage
@fixture
def set_tear():
    driver=webdriver.Chrome()
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    sleep(10)
    yield driver
    driver.quit()
@fixture
def login(set_tear):
      login = LoginPage(set_tear)
      login.login("poojamg246@gmail.com","Pooja@123")
      return set_tear