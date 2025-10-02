from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BroswerUtils.BrowserUtility import BrowserUtil

class CheckoutPage(BrowserUtil):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.quantity_locator = (By.CSS_SELECTOR, "input[class='form-control']")
        self.final_checkout_locator = (By.CSS_SELECTOR, 'button[class*="btn btn-success"]')
        self.countryname_locator = (By.ID, 'country')
        self.checkbox_locator = (By.CSS_SELECTOR, '.checkbox-primary')
        self.purchase_button_locator = (By.CSS_SELECTOR, "input[type='submit']")
        self.validate_locator = (By.CSS_SELECTOR, '.alert-success')

    def quantity_validation(self, productquantity):
        # Wait for quantity input to be visible and fetch its current value
        quantity = self.wait.until(EC.presence_of_element_located(self.quantity_locator))
        current_qty = quantity.get_attribute('value')

        # Change quantity if it's not already 1
        if current_qty != "1":
            quantity.clear()
            quantity.send_keys(productquantity)

    def final_checkout(self):
        self.driver.find_element(*self.final_checkout_locator).click()

    def delivery_address(self, countryname):
        # Start entering shipping details
        self.driver.find_element(*self.countryname_locator).send_keys(countryname)
        # Wait and select the suggested country
        self.wait.until(EC.presence_of_element_located(self.countryname_locator))
        self.driver.find_element(*self.countryname_locator).click()
        # Agree to terms and submit the order
        self.driver.find_element(*self.checkbox_locator).click()
        self.driver.find_element(*self.purchase_button_locator).click()

    def validate(self):
        # Verify success message
        msg = self.driver.find_element(*self.validate_locator).text
        assert "Success!" in msg
        print(msg)