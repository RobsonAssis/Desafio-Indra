class Login:
    def __init__(self, driver):
        self.URL = 'https://www.submarino.com.br/'
        self.driver = driver

    def go_login(self):
        self.driver.get(self.URL)
