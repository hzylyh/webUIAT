'''
Description: 
Author: John Holl
Github: https://github.com/hzylyh
Date: 2022-03-19 13:44:11
LastEditors: John Holl
LastEditTime: 2022-03-19 15:12:43
'''

import time
from selenium.webdriver.remote.webdriver import WebDriver
from core import case_handler
from core import parse_po
from entity.case_entity import CaseEntity
from typing import List, Dict
from selenium import webdriver
from entity.po_entity import POEntity
from constant.constant import *


def load_case() -> List[CaseEntity]:
    return case_handler.from_csv()


def load_po() -> Dict:
    return parse_po.load_project()


def execute(driver: WebDriver, handle: POEntity):
    ele = driver.find_element(by=handle.type, value=handle.value)
    if handle.action == 'input':
        ele.send_keys('ddd')
    elif handle.action == 'click':
        ele.click()


def run():
    cases = load_case()
    po_manager = load_po()
    driver = webdriver.Chrome(
        executable_path=APP['selenium']['driver-path'])
    driver.get('https://www.baidu.com')
    for case in cases:
        handle = po_manager[case.page][case.step]
        ele = driver.find_element(by=handle.type, value=handle.value)
        if handle.action == 'input':
            ele.send_keys('ddd')
        elif handle.action == 'click':
            ele.click()
            time.sleep(10)
