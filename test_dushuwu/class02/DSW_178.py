# 姓名：郭宏亮
# 时间：2023/8/12 21:31
"""
点击加入书架，会加入到我的书架中
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.find_element(By.XPATH, "//a[text()='登录']").click()

driver.find_element(By.ID, "txtUName").send_keys("")
driver.find_element(By.ID, "txtPassword").send_keys("")
driver.find_element(By.ID, "btnLogin").click()
