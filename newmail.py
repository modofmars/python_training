# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class newmail(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_newmail(self):
        success = True
        wd = self.wd
        wd.get("https://mail.rambler.ru/")
        wd.find_element_by_name("login").click()
        wd.find_element_by_name("login").clear()
        wd.find_element_by_name("login").send_keys("slyaquarius")
        wd.find_element_by_id("form_password").click()
        wd.find_element_by_id("form_password").clear()
        wd.find_element_by_id("form_password").send_keys("Y4019753s")
        wd.find_element_by_css_selector("button.form-button.form-button_submit").click()
        wd.find_element_by_css_selector("div.Header-main-jB").click()
        wd.find_element_by_css_selector("p.Header-newLetter-3Y").click()
        wd.find_element_by_id("receivers").click()
        wd.find_element_by_id("receivers").clear()
        wd.find_element_by_id("receivers").send_keys("slyaquarius@rambler.ru")
        wd.find_element_by_id("subject").click()
        wd.find_element_by_id("subject").clear()
        wd.find_element_by_id("subject").send_keys("test1")
        wd.switch_to_frame()
        wd.find_element_by_xpath("//html").click()
        wd.switch_to_default_content()
        wd.find_element_by_id("js").click()
        wd.find_element_by_xpath("//div[@class='Compose-content-2V']//button[.='Отправить письмо']").click()
        wd.find_element_by_link_text("LALALExanderLALALExanderasdfret2 LALALExanderLALALExanderasdfret2").click()
        wd.find_element_by_link_text("Выйти").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
