class product:
    def __init__(self, driver):
        self.driver = driver

    def buy_product(self):
        self.button = self.driver.find_element_by_xpath('//*[@id="btn-buy"]')
        self.button.click()