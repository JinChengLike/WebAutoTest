#coding=utf-8
from BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest


class indexPage(BasePage):
    url = "／"

    messageButton_loc = (By.XPATH, "//a[@title='信息动态']")

    def open(self):
        self._open(self.base_url, self.pagetitle)

    def Click_Message(self):
        self.find_element(*self.messageButton_loc).click()

