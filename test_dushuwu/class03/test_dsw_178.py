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


def test_dsw_178():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://novel.hctestedu.com")
    sleep(2)
    username = "18899991234"
    passwd = "123456"

    driver.find_element(By.XPATH, "//a[text()='登录']").click()

    driver.find_element(By.ID, "txtUName").send_keys(username)
    driver.find_element(By.ID, "txtPassword").send_keys(passwd)
    driver.find_element(By.ID, "btnLogin").click()
    sleep(2)

    driver.find_element(By.LINK_TEXT, "爱是大雾散尽时").click()
    driver.find_element(By.XPATH, "//a[text()='点击阅读']").click()
    sleep(2)


if __name__ == '__main__':
    pytest.main(['-v'])
