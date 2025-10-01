import json
import pytest
from PageObject.Loginpage import LoginPage

test_path = "/Users/tyndalepraveen/PycharmProjects/PythonSelenium/Data/test_e2eTestFramework.json"
with open(test_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]
@pytest.mark.smoke
@pytest.mark.parametrize("testList", test_list)
def test_e2eDemo(browser_select, testList):
    driver = browser_select
    loginpage = LoginPage(driver)
    print(loginpage.getTitle())
    shoppage = loginpage.login(testList["userName"], testList["userPassword"])
    shoppage.additems(testList["productName"])
    print(shoppage.getTitle())
    checkoutpage = shoppage.gotocart()
    print(checkoutpage.getTitle())
    checkoutpage.quantity_validation(testList["productQuantity"])
    checkoutpage.final_checkout()
    checkoutpage.delivery_address(testList["countryValue"])
    checkoutpage.validate()


