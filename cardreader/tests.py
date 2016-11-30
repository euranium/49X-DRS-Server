from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests, datetime
import time
from .models import Student
from cardreader import views

url = 'http://127.0.0.1:8000/'

class StudentTestCase(TestCase):

    def testCreateStudent(self):
        w_num = "0000004"
        views.processUserLogging(w_num)
        query = Student.objects.filter(w_num=w_num).filter(out_time=None).last()
        self.assertTrue(query)

    def testRapidSwipes(self):
        w_num = "0000005"
        views.processUserLogging(w_num)
        query = Student.objects.filter(w_num=w_num).filter(out_time=None).last()
        in_time = query.in_time
        views.processUserLogging(w_num)
        views.processUserLogging(w_num)
        query = Student.objects.filter(w_num=w_num)
        self.assertEqual(query.count(), 1)

    def testLogOutStudent(self):
        w_num = "00000007"
        views.processUserLogging(w_num)
        query = Student.objects.filter(w_num=w_num).last()
        query.in_time = (datetime.datetime.now() - datetime.timedelta(minutes=1)).time()
        query.save()
        views.processUserLogging(w_num)
        query = Student.objects.filter(w_num=w_num).last()
        self.assertTrue(query.out_time)

    def testInvalidId(self):
        w_num = "painandsuffering"
        match = views.isValidId(w_num)
        self.assertFalse(match)
        w_num = "010101"
        match = views.isValidId(w_num)
        self.assertFalse(match)
        w_num = "01047q01"
        match = views.isValidId(w_num)
        self.assertFalse(match)
        w_num = "0104701"
        match = views.isValidId(w_num)
        self.assertFalse(match)
        w_num = "01047165"
        match = views.isValidId(w_num)
        self.assertTrue(match)

    def testEditStudent(self):
        w_num = "0000008"
        views.processUserLogging(w_num)
        query = Student.objects.filter(w_num=w_num).filter(out_time=None).last()
        in_time = query.in_time
        new_in_time = datetime.datetime.now()
        query.in_time = new_in_time
        query.save()
        query = Student.objects.filter(w_num=w_num, in_time=in_time)
        self.assertEqual(query.count(), 0)
        query = Student.objects.filter(w_num=w_num, in_time=new_in_time)
        self.assertEqual(query.count(), 1)

    def testCapturePage(self):
        driver = webdriver.Firefox()
        driver.get(url)
        driver.save_screenshot('screenshotFireFox.png')
        driver.quit()

    def testInput(self):
        driver = webdriver.Firefox()
        driver.get(url)
        elem = driver.find_element_by_id('num')
        elem.clear()
        elem.send_keys("W01111111")
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        assert "logging in" in driver.page_source
        elem = driver.find_element_by_id('num')
        elem.clear()
        elem.send_keys("W01111111")
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        assert "You are already logged in" in driver.page_source

    def testLinks(self):
        driver = webdriver.Firefox()
        driver.get(url)
        for elem in driver.find_elements_by_tag_name('a'):
            link = url + elem.get_attribute('href')
            r = requests.get(link)
            assert r.status_code == 200
