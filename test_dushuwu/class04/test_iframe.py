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
    driver.get("https://www.selenium.dev/selenium/web/click_tests/click_in_iframe.html")
    sleep(2)
    # 定位方式一
    # iframe = driver.find_element(By.ID, "ifr")
    # driver.switch_to.frame(iframe)
    # 通过id或者name的值定位
    # driver.switch_to.frame("ifr")
    # 基于索引切换到第一个iframe，从0开始
    driver.switch_to.frame(0)
    driver.find_element(By.ID, "link").click()
    sleep(2)

    # 退出iframe，切换到默认的内容
    driver.switch_to.default_content()


if __name__ == '__main__':
    pytest.main(['-v'])
