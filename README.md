# 4GCapital_Pytest
Automation Testing for a website
**Project Title**

This project is a Python test automation framework designed to automate testing of the Saucedemo website using pytest-bdd, Selenium WebDriver, and Chrome browser. It includes BDD-style test scenarios for both happy and unhappy paths, covering login functionality and product cart management.
Table of Contents

    Introduction
    Prerequisites
    Installation
    Usage
    Tests
    Contributing
    Challenges Faced
    Future Work
    License

Introduction

This test automation framework aims to automate testing of the Saucedemo website to ensure its functionality meets the expected requirements. It leverages pytest-bdd for writing BDD-style tests, Selenium WebDriver for interacting with web elements, and Chrome browser for test execution.
Prerequisites

Before running the tests, ensure you have the following prerequisites installed:

    Python (version X.X.X)
    pytest (version X.X.X)
    pytest-bdd (version X.X.X)
    Selenium WebDriver
    Chrome browser

Installation

To install the necessary dependencies, follow these steps:

    Clone this repository to your local machine.
    Navigate to the project directory.
    Install dependencies using pip:

bash

pip install -r requirements.txt

Usage

To run the tests, execute the following command:

bash

pytest

This will execute all the test scenarios defined in the project.
Tests

The test scenarios included in this project cover the following cases:

    Happy Path: User can login and add a product to cart.
    Unhappy Path: User receives error message on incorrect login.

For more details on how to run the tests and interpret the results, refer to the Usage section.
Contributing

Contributions to this project are welcome! If you encounter any issues, have suggestions for improvements, or would like to contribute code, please feel free to open an issue or submit a pull request.
Challenges Faced

During the development of this project, several challenges were encountered, including:

    Difficulty in handling dynamic elements on the web page.
    Issues with test stability due to timing issues.
    Learning curve associated with pytest-bdd and Selenium WebDriver integration.

Future Work

There are several potential areas for future work and improvement, including:

    Enhancing test coverage to include additional features of the Saucedemo website.
    Implementing parallel execution to improve test execution time.
    Refactoring test code to improve readability and maintainability.
    Exploring integration with CI/CD pipelines for automated testing and deployment.

License

This project is licensed under the MIT License.
