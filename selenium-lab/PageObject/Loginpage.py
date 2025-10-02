from selenium.webdriver.common.by import By
from BroswerUtils.BrowserUtility import BrowserUtil
from PageObject.Shoppage import ShopPage

class LoginPage(BrowserUtil):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_locator = (By.ID, 'username')
        self.password_locator = (By.ID, 'password')
        self.button_locator = (By.ID, 'signInBtn')

    def login(self, username, password):
        self.driver.find_element(*self.username_locator).send_keys(username)
        self.driver.find_element(*self.password_locator).send_keys(password)
        self.driver.find_element(*self.button_locator).click()
        shoppage = ShopPage(self.driver)
        return shoppage