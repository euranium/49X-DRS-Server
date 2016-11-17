from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests, datetime
import time
from .models import Student

url = 'http://127.0.0.1:8000/'

class StudentTestCase(TestCase):

    def testCreateStudent(self):
        w_num = 01234567
        in_time = datetime.datetime.now()
        student = Student(w_num=w_num, in_time=in_time)
        student.save()
        query = Student.objects.filter(w_num=w_num, in_time=in_time)
        self.assertTrue(query)

    def testRapidSwipes(self):
        w_num = 01234567
        in_time = datetime.datetime.now()
        student = Student(w_num=w_num, in_time=in_time)
        student.save()
        student = Student(w_num=w_num, in_time=in_time)
        student.save()
        student = Student(w_num=w_num, in_time=in_time)
        student.save()
        query = Student.objects.filter(w_num=w_num, in_time=in_time)
        self.assertEqual(query.count(), 1)

    def testLogOutStudent(self):
        w_num = 01234567
        in_time = datetime.datetime.now()
        out_time = datetime.datetime.now()
        student = Student(w_num=w_num, in_time=in_time)
        student.out_time = out_time
        student.save()
        query = Student.objects.filter(w_num=w_num, in_time=in_time)
        self.assertEqual(student.out_time, out_time)

    def testInvalidId(self):
        w_num = "painandsuffering"
        in_time = datetime.datetime.now()
        student = Student(w_num=w_num, in_time=in_time)
        student.save()
        query = Student.objects.filter(w_num=w_num, in_time=in_time)
        self.assertEqual(query.count(), 0)

    def testEditStudent(self):
        w_num = 01234567
        in_time = datetime.datetime.now()
        out_time = datetime.datetime.now()
        student = Student(w_num=w_num, in_time=in_time)
        student.out_time = out_time
        student.save()
        query = Student.objects.filter(w_num=w_num, in_time=in_time)
        student = query.get()
        new_in_time = datetime.datetime.now()
        student.in_time = new_in_time
        student.save()
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
        assert "logging out" in driver.page_source

    def testLinks(self):
        driver = webdriver.Firefox()
        driver.get(url)
        for elem in driver.find_elements_by_tag_name('a'):
            link = url + elem.get_attribute('href')
            r = requests.get(link)
            assert r.status_code == 200
