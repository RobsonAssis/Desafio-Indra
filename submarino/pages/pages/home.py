class home:
    def __init__(self, driver):
        self.URL = 'https://www.submarino.com.br/'
        self.driver = driver

    def go_home(self):
        self.driver.get(self.URL)

    def go_login(self):
        self.element = self.driver.find_element_by_xpath('/html/body/header/div[2]/div[2]/div[1]/div[3]/span[2]/a/span[1]')
        self.element.click()
        self.button = self.driver.find_element_by_xpath('//*[@id="h_usr-signin"]')
        self.button.click()

    def go_signup(self):
        self.element = self.driver.find_element_by_xpath('/html/body/header/div[2]/div[2]/div[1]/div[3]/span[2]/a/span[1]')
        self.element.click()
        self.link = self.drive.find_element_by_xpath('/html/body/header/div[2]/div[2]/div[1]/div[3]/span[2]/div/a[2]')
        self.link.click()

    def select_product(self):
        self.link = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/div/section/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/section/a')
        self.link.click()