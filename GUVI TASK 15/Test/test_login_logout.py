import pytest
from pages1.loginpage1 import LoginPage
from driver_setup import get_driver
from pages1.homepage1 import HomePage
from utils1.utils_excel import write_result, get_test_data

file_path = "/Users/kavinnilaaj/Downloads/Task 15 Test Data"
sheet_name = "Sheet1"

test_data = get_test_data(file_path, sheet_name)

@pytest.mark.parametrize("username,password", test_data)
def test_cases(username, password):
    driver = get_driver()
    login = LoginPage(driver)
    home = HomePage(driver)

    try:
        login.open_login()
        login.enter_credentials(username, password)
        login.signin()

        try:
            home.verify_login()
            home.Logout_Page()
            actual = "Passed"
        except Exception:
            login.invalid_login()
            actual = "Failed"

        row_index = test_data.index((username, password)) + 2
        write_result(file_path, sheet_name, row_index, tester="Kavinnilaa", actual_result=actual)

    finally:
        driver.quit()

