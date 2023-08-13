# 姓名：郭宏亮
# 时间：2023/8/13 20:21
# 姓名：郭宏亮
# 时间：2023/8/12 22:28
# 姓名：郭宏亮
# 时间：2023/8/12 21:31
"""
点击加入书架，会加入到我的书架中
"""
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By


def test_dsw_180():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://novel.hctestedu.com")
    sleep(2)
    username = "18899991234"
    passwd = "123456"

    ele = driver.find_element(By.XPATH, '//*[@id="searchKey"]')
    ele.clear()
    ele.send_keys("你好" + keys.Keys.ENTER)

    sleep(2)


if __name__ == '__main__':
    pytest.main(['-v'])
