from data import Data, Url
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:
    #Вход по кнопке "Войти в аккаунт" на главной странице
    def test_login_from_main_page(self, driver):
        driver.get(Url.main_page)
        driver.find_element(*Locators.login_button_main_page).click()
        driver.find_element(*Locators.input_email).send_keys(Data.email)
        driver.find_element(*Locators.input_password).send_keys(Data.password)
        driver.find_element(*Locators.login_button_login_page).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.order_button))
        assert driver.find_element(*Locators.order_button).is_displayed()


    #Вход через кнопку «Личный кабинет»
    def test_login_via_account_button(self, driver):
        driver.get(Url.main_page)
        driver.find_element(*Locators.account_button).click()
        driver.find_element(*Locators.input_email).send_keys(Data.email)
        driver.find_element(*Locators.input_password).send_keys(Data.password)
        driver.find_element(*Locators.login_button_login_page).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.order_button))
        assert driver.find_element(*Locators.order_button).is_displayed()


    #Вход через кнопку в форме регистрации
    def test_login_via_registration_page(self, driver):
        driver.get(Url.registration_page)
        driver.find_element(*Locators.login_button_registration_page).click()
        driver.find_element(*Locators.input_email).send_keys(Data.email)
        driver.find_element(*Locators.input_password).send_keys(Data.password)
        driver.find_element(*Locators.login_button_login_page).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.order_button))
        assert driver.find_element(*Locators.order_button).is_displayed()


    #Вход через кнопку в форме восстановления пароля
    def test_login_via_password_recovery(self, driver):
        driver.get(Url.main_page)
        driver.find_element(*Locators.login_button_main_page).click()
        driver.find_element(*Locators.forgot_password_button).click()
        driver.find_element(*Locators.login_button_registration_page).click()
        driver.find_element(*Locators.input_email).send_keys(Data.email)
        driver.find_element(*Locators.input_password).send_keys(Data.password)
        driver.find_element(*Locators.login_button_login_page).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.order_button))
        assert driver.find_element(*Locators.order_button).is_displayed()

