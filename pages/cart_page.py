from utilities.logger import Logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class CartPage(Base):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    #  locators
    assert_test_text = '/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1'
    go_to_cart_button = '/html/body/div[4]/div[9]/div[5]/div[2]/div[3]/div[2]/div[2]/div[2]/a[2]'
    input_city = '//*[@id="frm"]/div/div[3]/table/tbody/tr[1]/td[3]/div[2]/input[1]'
    confirm_link_input_city = '//*[@id="frm"]/div/div[3]/table/tbody/tr[1]/td[3]/div[2]/div/span[1]'
    make_order_button = '//*[@id="frm"]/div/div[3]/table/tbody/tr[3]/td[5]/div/div/input'
    assert_url_for_test = 'https://trial-sport.ru/order.php'

    #  getters

    def get_assert_test_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.assert_test_text)))

    def get_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_city)))

    def get_confirm_link_input_city(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.confirm_link_input_city)))

    def get_make_order_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.make_order_button)))

    def get_assert_url_for_test(self):
        return self.driver.find_element(By.XPATH, self.assert_url_for_test)

    #  actions

    def set_city(self, city):
        self.get_city().send_keys(city)
        print('Input city delivery')

    def click_confirm_link_city(self):
        self.get_confirm_link_input_city().click()
        print('Click confirm link input city')

    def click_make_order_button(self):
        self.get_make_order_button().click()
        print('Click make order button')

    # methods

    def get_cart(self):
        Logger.add_start_step(method='get_cart')
        self.get_current_url()
        self.assert_text(self.get_assert_test_text(), 'Оформление заказа')
        self.driver.execute_script("window.scrollTo(0, 700)")
        self.set_city('Москва, Москва')
        self.click_confirm_link_city()
        self.click_make_order_button()
        self.assert_url(self.assert_url_for_test)
        Logger.add_end_step(url=self.driver.current_url, method='get_cart')
