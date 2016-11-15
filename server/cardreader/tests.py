from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from .models import Student

url = 'http://127.0.0.1:8000/'

class StudentTestCase(TestCase):
    def setUp(self):

    def testInput(self):

    def testAdmin(self):

    def testAuth(self):

    def capturePage(self):
        driver = webdriver.Firefox()
        driver.get(url)
        driver.save_screenshot('screenshotFireFox.png')
        driver.quit()
        driver = webdriver.Chrome()
        driver.get(url)
        driver.save_screenshot('screenshotChrome.png')
        driver.quit()

    def testInput(self):
        driver = webdriver.Firefox()
        driver.get(url)
        elem = driver.find_element_by_id('num')
        elem.clear()
        elem.send_keys("W01111111")
        elem.send_keys(Keys.RETURN)
        assert "logging in, 01111111" in driver.page_source
        elem = driver.find_element_by_id('num')
        elem.clear()
        elem.send_keys("W01111111")
        elem.send_keys(Keys.RETURN)
        assert "logging out, 01111111" in driver.page_source

    def testLinks(self):
        driver = webdriver.Firefox()
        driver.get(url)
        for elem in driver.find_elements_by_tag_name('a'):
            link = url + elem.get_attribute('href')
            r = requests.get(link)
            assert r.response_code == 200
