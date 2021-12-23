from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from random import random
import time

from core.browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


# Classe responsável por abrigar os comandos do Selenium pré configurados
class Instagram_Core(Browser):
    ignore_list = (TimeoutException, ElementNotVisibleException, ElementClickInterceptedException)

    def access_mainpage(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

    def get_element(self, locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def get_elements(self, locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        return self.driver.find_elements(By.CSS_SELECTOR, locator)

    def get_element_class(self, locator):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, locator)))
        return self.driver.find_element(By.CLASS_NAME, locator)

    def get_elements_class(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, locator)))
            return self.driver.find_elements(By.CLASS_NAME, locator)
        except TimeoutException:
            print("Elemento não encontrado")

    def get_input(self, locator, element):
        input = self.get_element(locator)
        input.send_keys(Keys.CONTROL, 'a')
        '''input.send_keys(element)'''
        for i in element:
            t = random()
            time.sleep(t)
            input.send_keys(i)

    def login_visibility(self, locator):
        try:
            wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1, ignored_exceptions=self.ignore_list)
            return wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))

        except TimeoutException:
            return False

    def get_text(self, locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        return self.driver.find_element(By.CSS_SELECTOR, locator).text

    # Aperta ESC
    def key_escape(self):
        ActionChains(self.driver).send_keys(Keys.ESCAPE)

    '''def test_erro(self, locator):
        time.sleep(1)
        return self.driver.find_element(By.CSS_SELECTOR, locator)'''

    '''def test_visibility2(self, locator):
        wait = WebDriverWait(self.driver, 10, 1)
        try:
            if wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, locator))):
                return True
            else:
                print("Não achou")
        except TimeoutException:
            print("Elemento não foi achado")'''
