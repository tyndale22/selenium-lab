from selenium.webdriver.common.by import By
from BroswerUtils.BrowserUtility import BrowserUtil
from PageObject.Checkoutpage import CheckoutPage

class ShopPage(BrowserUtil):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shoplink_locator = (By.CSS_SELECTOR, 'a[href*="shop"]')
        self.productlist_locator = (By.XPATH, '//div[@class="card h-100"]')
        self.checkout_button_locator = (By.CSS_SELECTOR, 'a[class*="btn-primary"]')


    def additems(self, product_name):
        # Find all product cards
        self.driver.find_element(*self.shoplink_locator).click()
        products = self.driver.find_elements(*self.productlist_locator)

        for product in products:
            # Get the product name from each card
            productName = product.find_element(By.XPATH, 'div/h4').text
            if productName == product_name:
                # Click 'Add to Cart' for the matched product
                product.find_element(By.CSS_SELECTOR, "button[class='btn btn-info']").click()
                break


    def gotocart(self):
        # Go to the checkout page
        self.driver.find_element(*self.checkout_button_locator).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage

