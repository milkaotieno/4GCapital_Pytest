# saucedemo.feature

Feature: Saucedemo Website

  Scenario: User can login and add a product to cart
    Given the user is on the login page
    When the user logs in with correct credentials
    Then the user should be able to add a product to cart

  Scenario: User receives error message on incorrect login
    Given the user is on the login page
    When the user logs in with incorrect credentials
    Then the user should receive an error message
