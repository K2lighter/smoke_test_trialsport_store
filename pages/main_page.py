import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class MainPage(Base):
    url = 'https://trial-sport.ru/'

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    #  locators
    main_menu_snowboards = '//*[@id="cm4"]/span'
    submenu_snowboards = '//*[@id="cm4_sub"]/div/div/div/div[1]/div/div[1]/a[4]/p'
    brand_radiobutton = '//*[@id="filter_form"]/div[1]/div[3]/div[5]/h4'
    sub_brand_checkbox = '//*[@id="brand2278"]'
    snowboard_nitro_prime = '//a[@title="PRIME X DD"]'
    add_to_cart_button = '//a[@class="item_im_buy__but js-show-buy-params"]'
    add_to_cart_button_confirm = '/html/body/div[4]/div[6]/div[11]/div[2]/div[2]/form/div/div/div/input'


    #  getters

    def get_menu_snowboards(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_menu_snowboards)))

    def get_submenu_snowboards(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.submenu_snowboards)))

    def get_brand_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand_radiobutton)))

    def get_sub_brand_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sub_brand_checkbox)))

    def get_snowboard_nitro_prime(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.snowboard_nitro_prime)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_add_to_cart_button_confirm(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button_confirm)))

    #  actions

    def click_main_menu_snowboards(self):
        self.get_menu_snowboards().click()
        print('click confirm')

    def click_submenu_snowboards(self):
        self.get_submenu_snowboards().click()
        print('Click submenu snowboards')

    def click_brand_radiobutton(self):
        self.get_submenu_snowboards().click()
        print('Click brand radiobutton')

    def click_sub_brand_checkbox(self):
        self.get_sub_brand_checkbox().click()
        print('Click sub brand checkbox')

    def click_snowboard_nitro_prime(self):
        self.get_snowboard_nitro_prime().click()
        print('Click snowboard nitro prime')

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print('Click add to cart button')

    def click_add_to_cart_button_confirm(self):
        self.get_add_to_cart_button_confirm().click()
        print('Click add to cart confirm button')

    # methods

    def choice_snowboards(self):
        self.get_current_url()
        time.sleep(1)
        self.click_main_menu_snowboards()
        self.click_submenu_snowboards()
        self.driver.execute_script("window.scrollTo(0, 500)")
        self.click_snowboard_nitro_prime()
        self.click_add_to_cart_button()
        self.click_add_to_cart_button_confirm()