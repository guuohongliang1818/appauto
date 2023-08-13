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
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_dsw_179():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # driver.implicitly_wait(4)
    driver.get("http://novel.hctestedu.com")
    # sleep(2)
    username = "18899991234"
    passwd = "123456"

    driver.find_element(By.XPATH, "//a[text()='登录']").click()

    driver.find_element(By.ID, "txtUName").send_keys(username)
    driver.find_element(By.ID, "txtPassword").send_keys(passwd)
    driver.find_element(By.ID, "btnLogin").click()
    # sleep(1)
    # ele = driver.find_element(By.XPATH, "//a[text()='我的书架']")
    ele = WebDriverWait(driver, 5).until_not(
        expected_conditions.visibility_of_element_located((By.XPATH, "//a[text()='登录']")))
    # print(driver.page_source)
    # WebDriverWait(driver, 5).until_not(
    #     expected_conditions.visibility_of(driver.find_element(By.XPATH, "//a[text()='登录']")))
    print(ele)
    driver.find_element(By.XPATH, "//a[text()='我的书架']").click()
    sleep(3)


if __name__ == '__main__':
    pytest.main(['-v'])
