import allure
from utilities.logger import Logger
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class FinishPage(Base):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    #  locators

    radiobutton_place_delivery = '//*[@id="frm"]/div/div/div[2]/div[1]/label'
    recipient_of_product = '//*[@id="for_delivery1c"]/table/tbody/tr[1]/td[2]/div/input'
    phone_number_recipient = '//input[@type="tel"]'
    radiobutton_operator_call_needed = '//*[@id="frm"]/div/div/table[1]/tbody/tr/td[2]/div/div[3]/label'
    continue_button = '//*[@id="frm"]/div/div/table[2]/tbody/tr/td[3]/div/div/input'
    finish_mistake = '//span[@id="msgText"]'

    #  getters

    def get_radiobutton_place_delivery(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.radiobutton_place_delivery)))

    def get_recipient_of_product(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.recipient_of_product)))

    def get_phone_number_recipient(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.phone_number_recipient)))

    def get_radiobutton_operator_call_needed(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.radiobutton_operator_call_needed)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    def get_finish_mistake(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.finish_mistake)))

    #  actions

    def click_radiobutton_place_delivery(self):
        self.get_radiobutton_place_delivery().click()
        print('Click radiobutton_place_delivery')

    def set_recipient_of_product(self, last_name, first_name, patronymic):
        self.get_recipient_of_product().send_keys(last_name, first_name, patronymic)
        print('Click recipient_of_product')

    def set_phone_number_recipient(self, number):
        self.get_radiobutton_place_delivery().send_keys(number)
        print('Click phone_number_recipient')

    def click_radiobutton_operator_call_needed(self):
        self.get_radiobutton_operator_call_needed().click()
        print('Click radiobutton_operator_call_needed')

    def click_continue_button(self):
        self.get_continue_button().click()
        print('Click continue_button')

    # methods

    def get_delivery(self):
        with allure.step('Get delivery'):
            Logger.add_start_step(method='get_delivery')
            self.get_current_url()
            self.click_radiobutton_place_delivery()
            self.set_recipient_of_product('Ivanov', ' Ivan', ' Ivanovich')
            self.driver.find_element(By.XPATH, self.continue_button).send_keys(Keys.DOWN)
            # self.set_phone_number_recipient('+7 (991) 657-92-77')
            self.click_radiobutton_operator_call_needed()
            self.click_continue_button()
            self.assert_text(self.get_finish_mistake(), 'Заполните верно поле "Номер телефона получателя заказа".')
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='get_delivery')
