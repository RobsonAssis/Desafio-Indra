from Pyautomators.contrib.scenario_autoretry import scenario_retry
from selenium import webdriver

from pages.pages.home import home
from pages.pages.product import product
#Importação de carrinho de compras
from pages.pages.shopping_car import shopping_car

def before_all(context):
	context.wait_seg = webdriver.support.ui.WebDriverWait
	context.driver = webdriver.Chrome(executable_path='.\driver\chromedriver.exe')
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

