# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver

import unittest

class newMail(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_newMail(self):
        success = True
        wd = self.wd
        wd.get("https://mail.rambler.ru/")
        wd.find_element_by_name("login").click()
        wd.find_element_by_name("login").clear()
        wd.find_element_by_name("login").send_keys("slyaquarius")
        wd.find_element_by_id("form_password").click()
        wd.find_element_by_id("form_password").clear()
        wd.find_element_by_id("form_password").send_keys("Ykolomeicev1990")
        wd.find_element_by_css_selector("button.form-button.form-button_submit").click()
        wd.find_element_by_css_selector("div._Button-label-3x").click()
        wd.find_element_by_id("receivers").click()
        wd.find_element_by_id("receivers").clear()
        wd.find_element_by_id("receivers").send_keys("slyaquarius@rambler.ru")
        wd.find_element_by_id("subject").click()
        wd.find_element_by_id("subject").clear()
        wd.find_element_by_id("subject").send_keys("test1")
        wd.find_element_by_class_name("_Button-label-3x").click()
        wd.find_element_by_link_text("LALALExanderLALALExanderasdfret2 LALALExanderLALALExanderasdfret2").click()
        wd.find_element_by_link_text("Выйти").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
