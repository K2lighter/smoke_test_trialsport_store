import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class LoginPage(Base):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    #  locators

    account_button = '//span[@class="profile_lnk"]'
    close_banner = '//a[@class="close button"]'
    login_email = '//*[@id="idLogForm"]/table/tbody/tr/td[1]/table/tbody/tr[1]/td[2]/div/input'
    password = '//*[@id="idLogForm"]/table/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/div/input'
    enter_button = '//input[@type="submit"]'

    #  getters

    def get_account_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.account_button)))

    def get_confirm_banner(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.close_banner)))

    def get_login_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_email)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    #  actions

    def click_close_banner(self):
        self.get_confirm_banner().click()
        print('Click close banner')

    def click_account_button(self):
        self.get_account_button().click()
        print('Click account button')

    def set_user_name(self, login_email):
        self.get_login_email().send_keys(login_email)
        print('Input user name')

    def set_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_enter_button(self):
        self.get_login_button().click()
        print('Click login button')

    # methods

    def authorization(self):
        with allure.step('Authorization'):
            Logger.add_start_step(method='authorization')
            self.click_close_banner()
            self.click_account_button()
            self.get_current_url()
            self.set_user_name('k2lighter@gmail.com')
            self.set_password('selenium')
            self.click_enter_button()
            Logger.add_end_step(url=self.driver.current_url, method='authorization')
