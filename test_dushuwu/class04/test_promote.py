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
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get("http://www.selenium.dev/selenium/web/alerts.html")
    sleep(2)
    # 点击弹框
    driver.find_element(By.ID, "prompt").click()
    sleep(2)
    # 显示等待处理弹框
    # alert = wait.until(expected_conditions.alert_is_present())
    alert = driver.switch_to.alert
    # 获取弹框的文本信息
    alert.send_keys("郭宏亮你好")
    # 点击弹框确认
    alert.accept()
    # 点击取消
    # alert.dismiss()
    sleep(2)

    # 另一种获取弹框的方法，使用Alert类
    # select = Select(元素)
    driver.find_element(By.ID, "prompt").click()
    alert = Alert(driver)
    alert.send_keys("selenium hello")
    # 点击弹框确认
    alert.accept()
    # 点击取消
    # alert.dismiss()
    sleep(2)




if __name__ == '__main__':
    pytest.main(['-v'])
