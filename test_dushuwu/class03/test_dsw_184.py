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
from selenium.webdriver.common.by import By


def test_dsw_184():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://novel.hctestedu.com")
    sleep(2)

    driver.back()
    sleep(2)

    driver.forward()
    sleep(2)

    driver.refresh()
    sleep(2)


if __name__ == '__main__':
    pytest.main(['-v'])
