# -*- coding: utf-8 -*-
'''
Created on Apr 23, 2021

@author: flba
'''
from base.test_base import TestBase


class GoogleSpreadSheet(TestBase):

    ADD_ONS = "//div[@id='docs-extensions-menu']"
    YAMM_ADDON = "//span[contains(text(),'Yet Another Mail Merge: Mail Merge for Gmail')]"
    START_MAIL_MERGE = "//div[contains(text(),'Start Mail Merge')]"

    def click_add_ons(self):
        self.click_on_item(self.ADD_ONS, timeout=1)

    def click_yamm_addon(self):
        self.click_on_item(self.YAMM_ADDON, timeout=1)

    def click_start_mail_merge(self):
        self.click_on_item(self.START_MAIL_MERGE, timeout=1)
