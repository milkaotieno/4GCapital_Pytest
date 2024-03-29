# test_saucedemo.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest_bdd import scenario, given, when, then


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@scenario('saucedemo.feature', 'User can login and add a product to cart')
def test_login_and_add_product():
    pass


@scenario('saucedemo.feature', 'User receives error message on incorrect login')
def test_incorrect_login_message():
    pass


@given('the user is on the login page')
def login_page(browser):
    browser.get("https://www.saucedemo.com/")
    assert "Swag Labs" in browser.title


@when('the user logs in with correct credentials')
def login_with_correct_credentials(browser):
    username = browser.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    password = browser.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    login_button = browser.find_element(By.ID, "login-button")
    login_button.click()


@then('the user should be able to add a product to cart')
def add_product_to_cart(browser):
    product = browser.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(1) .btn_inventory")
    product.click()
    cart_button = browser.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
    cart_button.click()
    assert "Sauce Labs Backpack" in browser.page_source


@when('the user logs in with incorrect credentials')
def login_with_incorrect_credentials(browser):
    username = browser.find_element(By.ID, "user-name")
    username.send_keys("invalid_user")
    password = browser.find_element(By.ID, "password")
    password.send_keys("invalid_password")
    login_button = browser.find_element(By.ID, "login-button")
    login_button.click()


@then('the user should receive an error message')
def check_error_message(browser):
    error_message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message-container h3"))
    )
    assert error_message.text == "Epic sadface: Username and password do not match any user in this service"
