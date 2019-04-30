class shopping_car:
    def __init__(self, driver):
        self.driver = driver
        
    def remove_item(self):
        self.link = self.driver.find_element_by_xpath('/html/body/div[4]/section/section/div[1]/div[1]/section/ul/li/div[2]/div[2]/a')
        self.link.click()