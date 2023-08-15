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
    # 原始窗口句柄id
    original_hd = driver.current_window_handle
    print("原始窗口句柄id", original_hd)
    sleep(2)
    # 打印所有的其他页签
    print(driver.window_handles)
    assert len(driver.window_handles) == 1


if __name__ == '__main__':
    pytest.main(['-v'])
