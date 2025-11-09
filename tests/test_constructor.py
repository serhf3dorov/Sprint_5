from data import Url
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructor:
    # Переход к разделу "Булки"
    def test_go_to_buns(self, driver):
        driver.get(Url.main_page)
        driver.find_element(*Locators.sauces_span).click()
        WebDriverWait(driver, 5)
        driver.find_element(*Locators.buns_span).click()
        WebDriverWait(driver, 5)
        assert driver.find_element(*Locators.active_div_in_constructor).text == 'Булки'


    #Переход к разделу "Соусы"
    def test_go_to_sauces(self, driver):
        driver.get(Url.main_page)
        driver.find_element(*Locators.sauces_span).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.sauces_span))
        assert driver.find_element(*Locators.active_div_in_constructor).text == 'Соусы'


    # Переход к разделу "Начинки"
    def test_go_to_fil(self, driver):
        driver.get(Url.main_page)
        driver.find_element(*Locators.fil_span).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.fil_span))
        assert driver.find_element(*Locators.active_div_in_constructor).text == 'Начинки'

