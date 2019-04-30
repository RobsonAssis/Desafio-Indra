class Login:
    def __init__(self, driver):
        self.URL = 'https://www.submarino.com.br/'
        self.driver = driver

    def go_login(self):
        self.driver.get(self.URL)

    def go_login(self):
        self.element = self.driver.find_element_by_xpath('/html/body/header/div[2]/div[2]/div[1]/div[3]/span[2]/a/span[1]')
        self.element.click()
        self.button = self.driver.find_element_by_xpath('//*[@id="h_usr-signin"]')
        self.button.click()