# 姓名：郭宏亮
# 时间：2023/8/15 21:08
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def test_confirm():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://novel.hctestedu.com")
    sleep(2)
    # 打开一个新页签
    driver.switch_to.new_window("tab")
    driver.get("https://www.baidu.com")
    sleep(2)
    # 打开一个新窗口
    driver.switch_to.new_window("window")
    driver.get("https://www.taobao.com/")
    sleep(2)


if __name__ == '__main__':
    pytest.main(['-v'])
