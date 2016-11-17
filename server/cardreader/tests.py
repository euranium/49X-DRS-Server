from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests, datetime
from .models import Student

url = 'http://127.0.0.1:8000/'

class StudentTestCase(TestCase):

    # def setUp(self):
        
    # def testAdmin(self):

    # def testAuth(self):

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
