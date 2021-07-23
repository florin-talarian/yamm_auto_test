# -*- coding: utf-8 -*-
'''
Created on Apr 23, 2021

@author: flba
'''

import pytest
from selenium.webdriver.common.by import By


class TestBase():

    @pytest.fixture(scope="function", autouse=True)
    def instance_of_sb(self, sb):
        self._sb = sb

    def open_page(self, url):
        self._sb.open(url)

    def maximize_window(self):
        self._sb.maximize_window()

    def open_new_tab(self):
        self._sb.open_new_window()

    def click_on_item(self, selector, timeout=None):
        self._sb.click(selector, timeout=timeout)

    def click_on_item_by_id(self, selector, timeout=None):
        self._sb.click(selector, by=By.ID, timeout=timeout)

    def type_into_item(self, selector, text, timeout=None):
        self._sb.type(selector, text=text, timeout=timeout)

    def type_into_item_by_id(self, selector, text, timeout=None):
        self._sb.type(selector, text=text, by=By.ID, timeout=timeout, retry=True)

    def check_element_present(self, selector, timeout=None):
        self._sb.assert_element_present(selector, timeout=timeout)

    def hoover_on_item(self, selector, timeout=None):
        self._sb.hover_on_element(selector, timeout=timeout)

    def switch_to_frame(self, selector, timeout=None):
        self._sb.switch_to_frame(selector, timeout=timeout)

    def unselect_checkox_by_id(self, selector):
        self._sb.unselect_if_selected(selector, by=By.ID)
