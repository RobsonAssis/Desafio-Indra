from Pyautomators.contrib.scenario_autoretry import scenario_retry
from selenium import webdriver
from pages.pages.home import home
from pages.pages.product import product
from pages.pages.shopping_car import shopping_car

def before_all(context):
	context.driver = webdriver.Chrome('driver\chromedriver.exe')
	#Entra na página inicial
	#Enter in home page
	context.home_page = home(context.driver)
	context.home_page.go_home()
	#Seleciona um produto
	#Select a product 
	context.home_page.select_product()
	#Instanciando carrinho
	#Create an instance of shopping_car
	context.sh_car = shopping_car(context.driver)
	pass

def before_feature(context,feature):
	pass

def before_scenario(context,scenario):
	pass

def before_tag(context,tag):
	pass

def after_tag(context,tag):
	pass

def before_step(context,step):
	pass

def after_step(context,step):
	pass

def after_scenario(context,scenario):
	pass

def after_feature(context,feature):
	pass

def after_all(context):
	context.driver.close()
	pass

