# -*- coding: utf-8 -*-
'''
Created on Apr 23, 2021

@author: flba
'''
from base.test_base import TestBase
from data.test_data import DRAFT_NAME, SENDER_NAME
from libs.commons import retry_until_func_passes


class PageGmail(TestBase):

    USERNAME = "//input[@id='identifierId']"
    PASSWORD = "//input[@name='password']"
    NEXT_BUTTON = "//button[1]/div[2]"
    COMPOSE_BUTTON = "//div[contains(text(),'Compose')]"
    YAMM_MAIL = f"(//span[contains(text(),'{DRAFT_NAME}')])[2]"
    YAMM_SENDER = f"//span[contains(text(),'{SENDER_NAME}')]"

    def set_username(self, value):
        self.type_into_item(self.USERNAME, value)

    @retry_until_func_passes(10, 0.1)
    def click_next(self):
        self.click_on_item(self.NEXT_BUTTON)

    def set_password(self, value):
        self.type_into_item(self.PASSWORD, value)

    def check_gmail_loaded(self):
        self.check_element_present(self.COMPOSE_BUTTON, timeout=10)

    def open_last_yamm_mail(self):
        self.click_on_item(self.YAMM_MAIL)

    def check_sender_correct(self):
        self.check_element_present(self.YAMM_SENDER)
