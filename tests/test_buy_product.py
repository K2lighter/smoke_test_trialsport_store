from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.cart_page import CartPage
from pages.select_product_page import SelectProductPage
from pages.finish_page import FinishPage
from pages.filters_product_page import FiltersProductPage
from pages.login_page import LoginPage
from pages.title_page import TitlePage


def test_select_product(set_up, set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # driver = webdriver.Chrome(executable_path='D:\\selenium_pr\\chromedriver.exe')
    driver = webdriver.Firefox(executable_path='D:\\chromedriver\\geckodriver.exe.exe')

    print('STATUS TEST BUY PRODUCT: START')

    tp = TitlePage(driver)
    tp.load_website()

    login = LoginPage(driver)
    login.authorization()

    fpp = FiltersProductPage(driver)
    fpp.filter_product()

    spp = SelectProductPage(driver)
    spp.select_product()

    cp = CartPage(driver)
    cp.get_cart()

    dp = FinishPage(driver)
    dp.get_delivery()

    print('STATUS TEST BUY PRODUCT: FINISH')

    driver.quit()
