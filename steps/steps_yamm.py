# -*- coding: utf-8 -*-
'''
Created on Apr 23, 2021

@author: flba
'''
import pytest
from pages.gmail import PageGmail
from pages.yamm import Yamm
from pages.spreadsheet import GoogleSpreadSheet
from data.test_data import GMAIL_URL, SPREADSHEET_URL, SENDER_NAME, TEST_MAIL,\
    TEST_MAIL_PASS, DRAFT_NAME, SPREADSHEET_NAME
from libs.commons import retry_until_func_passes, open_spreadheet
from libs.gmail_api_lib import GMailApi


class StepsYamm(PageGmail, GoogleSpreadSheet, Yamm):

    @pytest.fixture(scope="function", autouse=True)
    def open_gmail(self):
        self.open_page(GMAIL_URL)
        self.maximize_window()

    @pytest.fixture(scope="function", autouse=True)
    def cleanup_after_test(self):
        yield
        if hasattr(self, "draft_id"):
            self.and_draft_is_deleted()

    def given_login_into_google(self):
        # self.set_username(TEST_MAIL)
        # self.click_next()
        # self.set_password(TEST_MAIL_PASS)
        # self.click_next()
        self.check_gmail_loaded()

    def and_a_draft_message_is_saved(self):
        g_api = GMailApi()
        g_api.create_message("", "", "TestDraftAuto", "TestDraftAuto")
        self.draft_id = g_api.save_draft()

    def and_draft_is_deleted(self):
        GMailApi().delete_draft(self.draft_id)

    def and_populate_and_open_spreadsheets(self):
        g_spreadheet = open_spreadheet(SPREADSHEET_NAME)
        g_spreadheet.delete_rows(2, 3)
        g_spreadheet.insert_row(["barbuflorinadrian@gmail.com", "Barbu Florin", "Mr", "Florin", "Barbu", "Flo", "Google", "71233412"], 2)
        g_spreadheet.insert_row([TEST_MAIL, "Florin Barbu", "Sir", "Barbu", "Florin", "B", "Apple", "32432423"], 3)
        self.open_new_tab()
        self.open_page(SPREADSHEET_URL)

    @retry_until_func_passes(20, 1)
    def and_open_yamm_mail_merge(self):
        self.click_add_ons()
        self.click_yamm_addon()
        self.click_start_mail_merge()

    def then_mail_merge_is_started(self):
        self.switch_to_first_iframe()
        self.switch_to_second_iframe()
        self.switch_to_third_iframe()
        self.click_continue()
        self.set_sender(SENDER_NAME)
        self.set_draft(DRAFT_NAME + "\n")
        self.uncheck_tracking_checkbox()
        self.click_send()

    def then_yamm_mail_is_present_in_inbox(self):
        self.open_last_yamm_mail()
        self.check_sender_correct()

    def and_mails_are_sent(self):
        self.is_mails_sent_message_present()

    def and_status_is_updated_in_the_spreadsheet(self):
        for row in open_spreadheet(SPREADSHEET_NAME).get_all_records():
            assert row["Merge status"] == "EMAIL_SENT"

    def then_mail_can_be_sent(self):
        self.click_send()

    def and_message_sent_popup_is_displayed(self):
        self.check_message_sent()

    def and_mail_contains_correct_data(self):
        g_api = GMailApi()
        messages = g_api.list_messages(query="subject: testdraftauto newer_than:1d")
        last_message = g_api.get_message(messages["messages"][0]["id"])
        assert last_message["snippet"] == DRAFT_NAME
        assert f"{SENDER_NAME} <{TEST_MAIL}>" in str(last_message["payload"]["headers"])
