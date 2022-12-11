import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class LoginPage(Base):
    url = 'https://trial-sport.ru/'

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    #  locators
    confirm_banner = '//a[@class="close button"]'
    client_button = '//span[@class="profile_lnk"]'
    login_email = '//*[@id="idLogForm"]/table/tbody/tr/td[1]/table/tbody/tr[1]/td[2]/div/input'
    password = '//*[@id="idLogForm"]/table/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/div/input'
    enter_button = '//input[@type="submit"]'
    # personal_area_button = '//*[@id="asc"]/div[1]/div/div[2]/div/a[1]/span'
    # main_text = '//*[@id="asc"]/div[1]/div/div[2]/div/a[1]/span'

    #  getters

    def get_confirm_banner(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_banner)))

    def get_client_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.client_button)))

    def get_login_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_email)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    # def get_personal_area_button(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.personal_area_button)))
    #
    # def get_main_text(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_text)))

    #  actions

    def click_confirm_banner(self):
        self.get_confirm_banner().click()
        print('click confirm')

    def click_client_button(self):
        self.get_client_button().click()
        print('Click client button')

    def set_user_name(self, login_email):
        self.get_login_email().send_keys(login_email)
        print('Input user name')

    def set_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_enter_button(self):
        self.get_login_button().click()
        print('Click login button')
    #
    # def click_personal_area_button(self):
    #     self.get_personal_area_button().click()
    #     print('click personal area button')

    # methods

    def authorization(self):
        Logger.add_start_step(method='authorization')
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        time.sleep(1)
        self.click_confirm_banner()
        self.driver.refresh()
        self.click_client_button()
        self.set_user_name('k2lighter@gmail.com')
        self.set_password('selenium')
        self.click_enter_button()
        Logger.add_end_step(url=self.driver.current_url, method='authorization')

