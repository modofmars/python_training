# -*- coding: utf-8 -*-


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, credentials):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("login").click()
        wd.find_element_by_name("login").clear()
        wd.find_element_by_name("login").send_keys(credentials.username)
        wd.find_element_by_id("form_password").click()
        wd.find_element_by_id("form_password").clear()
        wd.find_element_by_id("form_password").send_keys(credentials.password)
        wd.find_element_by_css_selector("button.form-button.form-button_submit").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_class_name("Profile-exit-2_").click()
