#Importação da Ferramentas usadas
from Pyautomators.contrib.scenario_autoretry import scenario_retry
from selenium import webdriver


#Importação da página home.
from pages.pages.home import home

#Importação da página produto.
from pages.pages.product import product

#Importação da página produto.
from pages.pages.page_teste import Submarino

#Importação de carrinho de compras.
from pages.pages.shopping_car import shopping_car

def before_all(context):
	#Instanciando objeto para tempo de espera.
	context.wait_seg = webdriver.support.ui.WebDriverWait
	context.driver = webdriver.Chrome(executable_path='.\driver\chromedriver.exe')
	#Instanciando a classe para "home_page" com o driver embutido.	
	context.home_page = home(context.driver)
	#Instanciando a classe para "sh_car" com o driver embutido.	
	context.sh_car = shopping_car(context.driver)
	#Instanciando a classe submarino
	context.submarino=Submarino(context.driver)
	pass


def after_all(context):
	context.driver.close()
	pass

