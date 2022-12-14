import allure
from configuration import SERVICE_URL
from base.base_class import Base

'''Go to the Quicksilver website'''


class TitlePage(Base):
    url = SERVICE_URL

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def load_website(self):
        with allure.step('Load website'):
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            print('website loaded')
