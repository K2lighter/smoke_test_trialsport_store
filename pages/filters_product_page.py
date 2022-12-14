import allure
from selenium.webdriver import ActionChains
from utilities.logger import Logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class FiltersProductPage(Base):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    #  locators

    main_menu_snowboards = '//*[@id="cm4"]/span'
    submenu_snowboards = '//*[@id="cm4_sub"]/div/div/div/div[1]/div/div[1]/a[4]/p'
    brand_radiobutton = '//*[@id="filter_form"]/div[1]/div[3]/div[5]/h4'
    sub_brand_checkbox = '//*[@id="filter_form"]/div[1]/div[3]/div[5]/div[3]/label'
    slide_bar_left = '//*[@id="filter_form"]/div[1]/div[3]/div[2]/div/div[1]/div/a[1]/i'
    slide_bar_right = '//*[@id="filter_form"]/div[1]/div[3]/div[2]/div/div[1]/div/a[2]/i'
    confirm_button = '//*[@id="filter_form"]/div[1]/div[3]/div[13]/div/input'
    test_text_snowboard_page = '/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1'
    sorting_button = '//*[@id="ui-sort_select"]/span[1]'
    key_setting = '//*[@id="select1-group"]/ul/li[2]/a'

    #  getters

    def get_menu_snowboards(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_menu_snowboards)))

    def get_submenu_snowboards(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.submenu_snowboards)))

    def get_brand_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand_radiobutton)))

    def get_sub_brand_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sub_brand_checkbox)))

    def get_slide_bar_left_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.slide_bar_left)))

    def get_slide_bar_right_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.slide_bar_right)))

    def get_confirm_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_button)))

    def get_sorting_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sorting_button)))

    def get_text_for_assert_test(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.test_text_snowboard_page)))

    def get_key_setting(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.key_setting)))

    #  actions

    def click_main_menu_snowboards(self):
        self.get_menu_snowboards().click()
        print('Click menu snowboards')

    def click_submenu_snowboards(self):
        self.get_submenu_snowboards().click()
        print('Click submenu snowboards')

    def click_brand_radiobutton(self):
        self.get_brand_button().click()
        print('Click brand radiobutton')

    def click_sub_brand_checkbox(self):
        self.get_sub_brand_checkbox().click()
        print('Click sub brand checkbox')

    def move_slide_bar_left_button(self, limit):
        action = ActionChains(self.driver)
        action.click_and_hold(self.get_slide_bar_left_button()).move_by_offset(limit, 0).release().perform()
        print('Move slide bar left')

    def move_slide_bar_right_button(self, limit):
        action = ActionChains(self.driver)
        action.click_and_hold(self.get_slide_bar_right_button()).move_by_offset(limit, 0).release().perform()
        print('Move slide bar right')

    def click_confirm_button(self):
        self.get_confirm_button().click()
        print('Click confirm button')

    def click_sorting_button(self):
        self.get_sorting_button().click()
        print('Click sorting button')

    def click_key_setting(self):
        self.get_key_setting().click()
        print('Click key setting')

    # methods

    def filter_product(self):
        with allure.step('Filter product'):
            Logger.add_start_step(method='filter_product')
            self.get_current_url()
            self.click_main_menu_snowboards()
            self.click_submenu_snowboards()
            self.assert_text(self.get_text_for_assert_test(), 'Сноуборды')
            self.driver.execute_script("window.scrollTo(0, 500)")
            self.click_brand_radiobutton()
            self.move_slide_bar_left_button(21)
            self.click_sub_brand_checkbox()
            self.move_slide_bar_right_button(-55)
            self.click_confirm_button()
            self.click_sorting_button()
            self.click_key_setting()
            Logger.add_end_step(url=self.driver.current_url, method='filter_product')
