# -*- coding: utf-8 -*-
'''
Created on Apr 24, 2021

@author: flba
'''
from base.test_base import TestBase
from time import sleep
from libs.commons import retry_until_func_passes


class Yamm(TestBase):

    FIRST_FRAME = "//iframe[contains(@src,'iframedAppPanel')]"
    SECOND_FRAME = "sandboxFrame"
    THIRD_FRAME = "userHtmlFrame"
    CONTINUE_BUTTON = "//button[contains(text(),'Continue')]"
    SENDER = "senderName_input"
    DRAFT = "drafts_list"
    TRACKING_CHECKBOX = "readReceiptCheckbox"
    SEND_BUTTON = "sendButton"
    MAILS_SENT_MESSAGE = "//div[contains(text(),'All emails have been sent!')]"

    def switch_to_first_iframe(self):
        self.switch_to_frame(self.FIRST_FRAME, timeout=10)

    def switch_to_second_iframe(self):
        self.switch_to_frame(self.SECOND_FRAME)

    def switch_to_third_iframe(self):
        self.switch_to_frame(self.THIRD_FRAME)

    def click_continue(self):
        self.click_on_item(self.CONTINUE_BUTTON, timeout=30)

    def set_sender(self, value):
        self.type_into_item_by_id(self.SENDER, value)

    @retry_until_func_passes(20, 1)
    def set_draft(self, value):
        self.click_on_item_by_id(self.DRAFT)
        self.type_into_item_by_id(self.DRAFT, value)

    def uncheck_tracking_checkbox(self):
        self.unselect_checkox_by_id(self.TRACKING_CHECKBOX)

    def click_send(self):
        self.click_on_item_by_id(self.SEND_BUTTON)

    def is_mails_sent_message_present(self):
        self.check_element_present(self.MAILS_SENT_MESSAGE, timeout=20)
