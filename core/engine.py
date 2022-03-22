"""
Description:
Author: John Holl
Github: https://github.com/hzylyh
Date: 2022-03-19 13:44:11
LastEditors: John Holl
LastEditTime: 2022-03-19 15:12:43
"""
import logging
import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from core import case_handler
from core import po_handler
from entity.case_entity import CaseEntity
from typing import List, Dict
from selenium import webdriver
from constant.constant import *


def load_case() -> List[CaseEntity]:
    """
    加载用例
    :rtype: object
    """
    return case_handler.from_csv()


def load_po() -> Dict:
    """
    加载po
    :rtype: object
    """
    return po_handler.load_project()


def execute(driver: WebDriver, handle: Dict, case: CaseEntity):
    """
    核心执行逻辑
    :rtype: object
    """
    # ele = driver.find_element(by=handle['type'], value=handle['value'])
    ele = WebDriverWait(driver, 15).until(lambda x: x.find_element(by=handle['type'], value=handle['value']))
    if handle['action'] == 'input':
        logging.info("input")
        ele.send_keys(case.val)
    elif handle['action'] == 'click':
        logging.info("click")
        ele.click()


def run():
    """
    总执行方法
    :rtype: object
    """
    cases = load_case()
    po_manager = load_po()
    driver = webdriver.Chrome(
        executable_path=PROJECT['selenium']['driver-path'])
    driver.get(PROJECT['selenium']['web-url'])
    driver.maximize_window()
    for case in cases:
        handle = po_manager[case.page][case.step]
        execute(driver, handle, case)

