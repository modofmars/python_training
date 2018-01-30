# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver
import time
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://mail.rambler.ru/")

    def create_new_mail(self):
        wd = self.wd
        wd.find_element_by_css_selector("div._Button-label-3x").click()

    def field_and_send_message(self, mail):
        wd = self.wd
        self.create_new_mail()
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

    def destroy(self):
        self.wd.quit()
