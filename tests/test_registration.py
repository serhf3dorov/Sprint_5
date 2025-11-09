from data import Data, Url, RandomUser
import pytest
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:
    #Успешная регистрация
    def test_registration_success(self, driver):
        driver.get(Url.registration_page)
        driver.find_element(*Locators.input_name).send_keys(RandomUser.name)
        driver.find_element(*Locators.input_email).send_keys(RandomUser.email)
        driver.find_element(*Locators.input_password).send_keys(RandomUser.password)
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.header_login))
        assert driver.find_element(*Locators.header_login).text == 'Вход'


    #Регистрация без Имя
    def test_registration_without_name(self, driver):
        driver.get(Url.registration_page)
        driver.find_element(*Locators.input_email).send_keys(RandomUser.email)
        driver.find_element(*Locators.input_password).send_keys(RandomUser.password)
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.registration_button))
        assert driver.find_element(*Locators.header_registration).text == 'Регистрация'


    #Регистрация без Email
    def test_registration_without_email(self, driver):
        driver.get(Url.registration_page)
        driver.find_element(*Locators.input_name).send_keys(RandomUser.name)
        driver.find_element(*Locators.input_password).send_keys(RandomUser.password)
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.registration_button))
        assert driver.find_element(*Locators.header_registration).text == 'Регистрация'


    # Регистрация без Пароль
    def test_registration_without_password(self, driver):
        driver.get(Url.registration_page)
        driver.find_element(*Locators.input_name).send_keys(RandomUser.name)
        driver.find_element(*Locators.input_email).send_keys(RandomUser.email)
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.registration_button))
        assert driver.find_element(*Locators.header_registration).text == 'Регистрация'


    #Регистрация с паролем менее 6 символов
    @pytest.mark.parametrize('password', ['1', '12345'])
    def test_registration_password_less_6_symbols(self, driver, password):
        driver.get(Url.registration_page)
        driver.find_element(*Locators.input_name).send_keys(RandomUser.name)
        driver.find_element(*Locators.input_email).send_keys(RandomUser.email)
        driver.find_element(*Locators.input_password).send_keys(password)
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.header_incorrect_password))
        assert driver.find_element(*Locators.header_incorrect_password).text == 'Некорректный пароль'


    #Регистрация с Email вне формата логин@домен
    @pytest.mark.parametrize('email', ['@yandex.ru', 'sergeyfedorov35292'])
    def test_registration_with_incorrect_email(self, driver, email):
        driver.get(Url.registration_page)
        driver.find_element(*Locators.input_name).send_keys(RandomUser.name)
        driver.find_element(*Locators.input_email).send_keys(email)
        driver.find_element(*Locators.input_password).send_keys(RandomUser.password)
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.header_exist_user))
        assert driver.find_element(*Locators.header_exist_user).text == 'Такой пользователь уже существует'


    #Регистрация уже существующего пользователя
    def test_registration_with_exist_user(self, driver):
        driver.get(Url.registration_page)
        driver.find_element(*Locators.input_name).send_keys(Data.name)
        driver.find_element(*Locators.input_email).send_keys(Data.email)
        driver.find_element(*Locators.input_password).send_keys(Data.password)
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.header_exist_user))
        assert driver.find_element(*Locators.header_exist_user).text == 'Такой пользователь уже существует'

