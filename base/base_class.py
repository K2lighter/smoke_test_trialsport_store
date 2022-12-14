from datetime import datetime
from enums.global_enums import GlobalErrorMessages


class Base:
    def __init__(self, driver):
        self.driver = driver

    '''current url method'''

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'current url {get_url}')

    '''assert text method'''

    def assert_text(self, text, result):
        value_text = text.text
        assert value_text == result, GlobalErrorMessages.WRONG_TEXT_VALUE.value
        print('ASSERT TEST STATUS: TEXT MATCHED')

    '''screenshot method'''

    def get_screenshot(self):
        now_date = datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('D:\\smoke_test_trialsport\\screen\\' + name_screenshot)

    '''assert url method'''

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result, GlobalErrorMessages.WRONG_URL_VALUE.value
        print('ASSERT TEST STATUS: URL MATCHED')
