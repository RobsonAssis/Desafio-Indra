
import unittest
from unittest import TestCase
from selenium import webdriver


class TestPage(TestCase):
    def setUp(self):
        self.driver = Webdriver.Chrome()
        self.teste=gohome(self.driver)
        self.driver.get('http://google.com.br')

    def test_search(self):
        self.teste.search('outlook.com.br')
        assert self.driver.title == 'pesquisa - Pesquisa Google'
    def tearDown(self):
        self.driver.close_browser()

unittest.main()