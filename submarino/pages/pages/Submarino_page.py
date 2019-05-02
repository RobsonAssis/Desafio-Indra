import time

class Home:
    def __init__(self,driver):
        self.search = 'Celular'
        self.URL = 'https://www.submarino.com.br/'
        self.driver = driver
        self.celular = 'Motorola X4'
        self.cep = '06763390'
        
    def go_home(self):
        self.driver.get(self.URL)

    def pesquisar_c(self):
          element = self.driver.find_element_by_id('h_search-input')
          element.click()
          element.send_keys(self.celular)
          element.submit()
          time.sleep(7)
    def selecionar_c(self):
          element = self.driver.find_element_by_xpath('//*[@id="content-middle"]/div[5]/div/div/div/div[1]/div[1]/div')
          element.click()
    def calcular_cep(self):
          element = self.driver.find_element_by_xpath('//*[@id="input-freight-product"]')
          element.send_keys(self.cep)
          time.sleep(5)
          element = self.driver.find_element_by_xpath('//*[@id="bt-freight-product"]/div/span')
          element.click()
          time.sleep(7)
    def comprar(self):
          element = self.driver.find_element_by_xpath('//*[@id="btn-buy"]/div')
          element.click()
            
    def continuar(self):
          element = self.driver.find_element_by_xpath('//*[@id="btn-continue"]/div')
          element.click()
   

        
        
