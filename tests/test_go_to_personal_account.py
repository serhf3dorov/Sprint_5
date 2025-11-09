from data import Data, Url
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestPersonalAccount:
    def test_go_to_personal_account(self, driver):
        driver.get(Url.main_page)
        driver.find_element(*Locators.account_button).click()
        driver.find_element(*Locators.input_email).send_keys(Data.email)
        driver.find_element(*Locators.input_password).send_keys(Data.password)
        driver.find_element(*Locators.login_button_login_page).click()
        driver.find_element(*Locators.account_button).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.header_profile))
        assert driver.current_url == Url.profile_page

