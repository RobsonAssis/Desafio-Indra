class Submarino:
    def __init__(self,driver):
        self.driver=driver
        self.SITE='https://www.submarino.com.br/'

    def go_inicial(self):
        self.driver.get(self.SITE)

    def mais_info(self):
        botao=self.driver.find_element_by_id("btn-expanded")
        botao.click()
    
    def link_hoteis(self):
        link=self.driver.find_element_by_link_text("Hotéis")
        link.click()
    

        
        