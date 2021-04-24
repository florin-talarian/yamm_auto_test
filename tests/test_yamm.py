# -*- coding: utf-8 -*-
'''
Created on Apr 23, 2021

@author: flba
'''
import pytest
from steps.steps_yamm import StepsYamm


class TestYamm(StepsYamm):

    @pytest.mark.dependency(name="merge_mails")
    def test_merge_mails(self):
        self.given_login_into_google()
        self.and_populate_and_open_spreadsheets()
        self.and_open_yamm_mail_merge()
        self.then_mail_merge_is_started()
        self.and_mails_are_sent()
        self.and_status_is_updated_in_the_spreadsheet()

    @pytest.mark.dependency(depends=["merge_mails"])
    def test_check_mail_was_sent(self):
        self.given_login_into_google()
        self.then_yamm_mail_is_present_in_inbox()
