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
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By


def test_dsw_182():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://novel.hctestedu.com")
    sleep(2)
    username = "18899991234"
    passwd = "123456"
    # 定位搜索框
    ele = driver.find_element(By.XPATH, '//*[@id="searchKey"]')
    ActionChains(driver) \
        .move_to_element(ele) \
        .pause(1) \
        .click_and_hold() \
        .pause(1) \
        .send_keys("你好") \
        .perform()
    # 按下shift键
    ActionChains(driver) \
        .key_down(Keys.LEFT_SHIFT) \
        .send_keys("zzzz") \
        .perform()

    # 释放所有action

    ActionChains(driver).send_keys("zzzzz").perform()
    ActionBuilder(driver).clear_actions()
    sleep(5)


if __name__ == '__main__':
    pytest.main(['-v'])
