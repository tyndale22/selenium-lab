from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest

@pytest.mark.smoke
def test_tablesort(browser_select):
    driver = browser_select
    driver.get('https://rahulshettyacademy.com/seleniumPractise/#/offers')
    driver.maximize_window()
    browserSortedVeggies = []  # empty list
    dropdown = Select(driver.find_element(By.CSS_SELECTOR, '#page-menu'))
    dropdown.select_by_visible_text('20')

    # soring the column 1
    driver.find_element(By.XPATH, '//tr/th[1]').click()
    # collect sorted veggies in list
    veggieElements = driver.find_elements(By.XPATH, '//tr/td[1]')
    # extract the text into list
    for veggie in veggieElements:
        browserSortedVeggies.append(veggie.text)

    originalList = browserSortedVeggies.copy()
    browserSortedVeggies.sort()
    assert originalList == browserSortedVeggies
    print(originalList)
    print(browserSortedVeggies)
    print('The table is sorted correctly')