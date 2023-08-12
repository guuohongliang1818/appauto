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

# 找到输入框
el = driver.find_element(By.XPATH, '//*[@id="searchKey"]')
driver.execute_script(
    "arguments[0].setAttribute('style',arguments[1]);",
    el,
    "border:5px solid black;"
)

sleep(20)
