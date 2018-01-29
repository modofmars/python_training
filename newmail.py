# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver

import unittest
import time
from credentials import Credentials
from mail import Mail

class newMail(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_NewMail(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, Credentials(username="slyaquarius", password="Ykolomeicev1990"))
        self.create_new_mail(wd)
        self.field_and_send_message(wd, Mail(email="slyaquarius@rambler.ru", subject="TEST SUBJECT"))
        time.sleep(1)
        self.exit_from_profile(wd)

    def test_another_subject_Mail(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, Credentials(username="slyaquarius", password="Ykolomeicev1990"))
        self.create_new_mail(wd)
        self.field_and_send_message(wd, Mail(email="slyaquarius@rambler.ru", subject="ALERT! ALERT!"))
        time.sleep(1)
        self.exit_from_profile(wd)

    def open_home_page(self, wd):
        wd.get("https://mail.rambler.ru/")

    def login(self, wd, credentials):
        wd.find_element_by_name("login").click()
        wd.find_element_by_name("login").clear()
        wd.find_element_by_name("login").send_keys(credentials.username)
        wd.find_element_by_id("form_password").click()
        wd.find_element_by_id("form_password").clear()
        wd.find_element_by_id("form_password").send_keys(credentials.password)
        wd.find_element_by_css_selector("button.form-button.form-button_submit").click()

    def create_new_mail(self, wd):
        wd.find_element_by_css_selector("div._Button-label-3x").click()

    def field_and_send_message(self, wd, mail):
        # fill out the sender's field
        wd.find_element_by_id("receivers").click()
        wd.find_element_by_id("receivers").clear()
        wd.find_element_by_id("receivers").send_keys(mail.email)
        # fill out the subject field
        wd.find_element_by_id("subject").click()
        wd.find_element_by_id("subject").clear()
        wd.find_element_by_id("subject").send_keys(mail.subject)
        # send message
        wd.find_element_by_css_selector("#compose > div > div.Compose-send-O- > div > div > button > div").click()
        time.sleep(2)

    def exit_from_profile(self, wd):
        wd.find_element_by_class_name("Profile-exit-2_").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
