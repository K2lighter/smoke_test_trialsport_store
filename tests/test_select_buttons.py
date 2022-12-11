import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.buttons_page import ButtonsPage
from pages.cart_page import CartPage
from pages.delivery_info_page import DeliveryPage
from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_select_buttons(set_up, set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # driver = webdriver.Chrome(executable_path='D:\\selenium_pr\\chromedriver.exe')
    driver = webdriver.Firefox(executable_path='D:\\chromedriver\\geckodriver.exe.exe')

    print('STATUS TEST SELECT BUTTONS: START')

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.click_main_menu_snowboards()
    mp.click_submenu_snowboards()

    bp = ButtonsPage(driver)
    bp.select_buttons()

    print('STATUS TEST SELECT BUTTONS: FINISH')
    driver.quit()













