import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.cart_page import CartPage
from pages.delivery_info_page import DeliveryPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from base.base_class import Base


def test_select_product_1(set_up, set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # driver = webdriver.Chrome(executable_path='D:\\selenium_pr\\chromedriver.exe')
    driver = webdriver.Firefox(executable_path='D:\\chromedriver\\geckodriver.exe.exe')

    print('STATUS TEST BUY PRODUCT: START')

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.choice_snowboards()

    cp = CartPage(driver)
    cp.get_cart()

    dp = DeliveryPage(driver)
    dp.get_delivery()

    print('STATUS TEST BUY PRODUCT: FINISH')

    driver.quit()



