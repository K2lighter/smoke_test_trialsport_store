import allure
from utilities.logger import Logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class SelectProductPage(Base):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    #  locators

    choice_product = '//*[@id="obj2175093"]/span[2]/a[1]/span'
    add_to_cart_button = '/html/body/div[4]/div[3]/div[6]/div[1]/div[2]/div[3]/div[1]/a[1]/span'
    window_size_product = '//*[@id="ui-undefined"]/span[1]'
    select_size_product = '//*[@id="select1-group"]/ul/li[3]/a'
    add_to_cart_finish_button = '/html/body/div[4]/div[6]/div[11]/div[2]/div[2]/form/div/div/div/input'
    assert_test_text = '/html/body/div[4]/div[9]/div[5]/div[2]/div[3]/div[1]'
    cart_basket_button = '/html/body/div[4]/div[9]/div[5]/div[2]/div[3]/div[2]/div[2]/div[2]/a[2]'

    #  getters

    def get_choice_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choice_product)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_window_size_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.window_size_product)))

    def get_select_size_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_size_product)))

    def get_add_to_cart_finish_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.add_to_cart_finish_button)))

    def get_assert_test_text(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.assert_test_text)))

    def get_cart_basket_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_basket_button)))

    #  actions

    def click_choice_product(self):
        self.get_choice_product().click()
        print('Click choice product')

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print('Click add to cart button')

    def click_window_size_product(self):
        self.get_window_size_product().click()
        print('Click window select size product')

    def click_select_size_product(self):
        self.get_select_size_product().click()
        print('Click select size product')

    def click_add_to_cart_finish_button(self):
        self.get_add_to_cart_finish_button().click()
        print('Click add to cart finish button')

    def click_cart_basket_button(self):
        self.get_cart_basket_button().click()
        print('Click cart basket button')

    #  methods

    def select_product(self):
        with allure.step('Select product'):
            Logger.add_start_step(method='select_product')
            self.get_current_url()
            self.click_choice_product()
            self.driver.execute_script("window.scrollTo(0, 500)")
            self.click_add_to_cart_button()
            self.click_window_size_product()
            self.click_select_size_product()
            self.click_add_to_cart_finish_button()
            self.assert_text(self.get_assert_test_text(), 'Товар добавлен в корзину')
            self.click_cart_basket_button()
            Logger.add_end_step(url=self.driver.current_url, method='select_product')
