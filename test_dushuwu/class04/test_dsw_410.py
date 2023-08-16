# 姓名：郭宏亮
# 时间：2023/8/12 22:28
# 姓名：郭宏亮
# 时间：2023/8/12 21:31
"""
用例标题：验证能够创建收费的章节的书籍
前置条件：登录作者用户并进入到小说章节内容填写页面
测试步骤：
    1.输入对应的章节名
    2.输入对应的章节内容
    3.是否收费：收费
    4.点击提交按钮
预期结果：
    正确显示输入数据，点击提交后成功新建章节，数据库数据更新
    该数据添加成功；产看本章节需要收费
"""
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_dsw_178():
    driver = webdriver.Chrome()
    driver.set_window_size(1400, 700)
    wait = WebDriverWait(driver, 5)
    driver.get("http://novel.hctestedu.com")
    # 用户名登录：
    username = "18894687777"
    passwd = "123456"
    driver.find_element(By.XPATH, "//a[text()='登录']").click()
    wait.until(expected_conditions.text_to_be_present_in_element(By.LINK_TEXT, "登陆读书屋"))
    driver.find_element(By.ID, "txtUName").send_keys(username)
    driver.find_element(By.ID, "txtPassword").send_keys(passwd)
    driver.find_element(By.ID, "btnLogin").click()
    # 使用username作为等待条件
    wait.until(expected_conditions.text_to_be_present_in_element(By.LINK_TEXT, username))

    button = (By.XPATH, "//a[starts-with(text(),'章节管理')]")
    # 点击作家专区打开新页签
    # 等待新页签的出现，校验窗口数为2
    # 获取所有的窗口句柄，并切换到新窗口
    # 等待章节管理按钮出现，并点击

    elements = driver.find_element(*button)
    # 先滚动到提交按钮，
    # 单选按钮，点击收费
    # 点击提交

    # 非常重要结果检查，章节名称和是否收费
    # 检查阅读详情页： 可以重定向

    # 关闭浏览器


if __name__ == '__main__':
    pytest.main(['-v'])
