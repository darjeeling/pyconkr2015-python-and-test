from selenium import webdriver
import unittest
import time, os

class TestBBS(unittest.TestCase):
    def setUp(self):
        os.popen('cd tdd && ./manage.py flush --noinput ').read()
        os.popen('cd tdd && ./manage.py migrate --noinput').read()
        self.browser = webdriver.Firefox()
        self.base_url = "http://127.0.0.1:8000/"
        pass

    def tearDown(self):
        self.browser.quit()

    def test_list_web(self):
        list_url = "%s/%s" % ( self.base_url, 'bbs/list/')
        aa = self.browser.get(list_url)
        self.assertIn("hahaha", self.browser.page_source)
