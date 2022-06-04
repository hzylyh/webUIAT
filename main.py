"""
Description:
Author: John Holl
Github: https://github.com/hzylyh
Date: 2022-03-19 10:57:29
LastEditors: John Holl
LastEditTime: 2022-03-19 14:50:16
"""
import logging
from app import create_app
from database.manager import SQLManager

app = create_app()
db = SQLManager()


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

if __name__ == '__main__':
    # logging.basicConfig(filename='log/webUIAT.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
    app.run(debug=True)

