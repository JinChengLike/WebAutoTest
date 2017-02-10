#coding=utf-8
import unittest
from Page_Object import indexPage
from selenium import webdriver
import config


class index_page_Test_Case(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.url = config.index_url

    def test_login_mail(self):
        index_Page = indexPage.indexPage(self.driver, self.url, u"借贷宝官网-专业熟人借贷平台，直投熟人更高明")
        index_Page.open()
        index_Page.Click_Message()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
