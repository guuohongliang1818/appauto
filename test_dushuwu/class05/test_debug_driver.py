# 姓名：郭宏亮
# 时间：2023/8/18 10:11
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


# chrome使用debug模式，
def test_debug_driver():
    # os.popen("d:/start.bat")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://cart.taobao.com/cart.htm")
    sleep(1)
    driver.find_element(By.ID, "fm-login-id").send_keys("15616246124")
    driver.find_element(By.ID, "fm-login-password").send_keys("huace6666...")
    driver.find_element(By.XPATH, "//button").click()

    sleep(10)
