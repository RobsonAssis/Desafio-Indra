from Pyautomators.contrib.scenario_autoretry import scenario_retry
from selenium import webdriver
from pages.pages.Submarino_page import Home

def before_all(context):
		context.driver = webdriver.Chrome('driver/chromedriver.exe')
		context.Submarino_page = Home(context.driver)

def after_all(context):
		context.driver.quit()	
		
"""def before_feature(context,feature):
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
		pass"""




