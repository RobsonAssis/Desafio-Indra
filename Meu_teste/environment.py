from Pyautomators.contrib.scenario_autoretry import scenario_retry
from pages.pages.page_teste import Submarino
from selenium import webdriver

def before_all(context):
    context.driver=webdriver.Chrome('driver/chromedriver.exe')
    context.submarino=Submarino(context.driver)
def after_all(context):
	context.driver.quit()

