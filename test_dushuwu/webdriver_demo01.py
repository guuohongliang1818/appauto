# 姓名：郭宏亮
# 时间：2023/8/11 22:31
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# 浏览器初始化
driver = webdriver.Chrome()
sleep(3)
# 代开网址
driver.get("http://novel.hctestedu.com")
sleep(3)

# 输入书名，并按回车键
driver.find_element(By.XPATH, '//*[@id="searchKey"]').send_keys("你好")
driver.find_element(By.XPATH, '//*[@id="btnSearch"]/i').click()
sleep(3)

driver.quit()
