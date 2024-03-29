# testsuite.py

import pytest

# Import the test scenarios
from test_saucedemo import test_login_and_add_product, test_incorrect_login_message

# Define the test suite
def test_suite():
    # Run the test scenarios
    test_login_and_add_product()
    test_incorrect_login_message()

# Execute the test suite
if __name__ == "__main__":
    pytest.main(["-v", "testsuite.py"])
