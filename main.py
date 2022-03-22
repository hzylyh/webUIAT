"""
Description:
Author: John Holl
Github: https://github.com/hzylyh
Date: 2022-03-19 10:57:29
LastEditors: John Holl
LastEditTime: 2022-03-19 14:50:16
"""
# from selenium import webdriver
import logging

from core import engine

# driver = webdriver.Chrome(
#     executable_path='/Users/houzheyu/Workspace/personal/code/python/chromedriver/99.0.4844.51/chromedriver')
# driver.get('http://www.baidu.com')
# driver.maximize_window()

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

if __name__ == '__main__':
    logging.basicConfig(filename='log/webUIAT.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
    engine.run()
