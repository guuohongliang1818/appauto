# 姓名：郭宏亮
# 时间：2023/8/12 15:50
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
sleep(2)
# 代开网址
driver.get("http://novel.hctestedu.com")
sleep(2)

# 通过ID进行元素定位
# el = driver.find_element(By.ID, "searchKey").send_keys("测试文章名")
# sleep(2)
# 通过name进行元素定位
# el = driver.find_element(By.NAME, "searchKey").send_keys("测试name")
# sleep(2)
# 通过classname
# el = driver.find_element(By.CLASS_NAME, "s_int").send_keys("测试classname")
# sleep(2)
# 通过tagname
# el = driver.find_element(By.TAG_NAME, "input").send_keys("测试tagname")
# sleep(2)
# 通过超链接LINK_TEXT(精准查找)
# driver.find_element(By.LINK_TEXT, "爱是大雾散尽时").click()
# sleep(2)

# 通过超链接PARTIAL_LINK_TEXT(模糊查找)
# driver.find_element(By.PARTIAL_LINK_TEXT, "大雾散尽时").click()
# sleep(2)

# xpath定位
# 01.单属性定位
driver.find_element(By.XPATH, '//div[@class="leftBox"]//a[text()="爱是大雾散尽时"]').click()
# 02.多属性定位
# //a[starts-with(@href,'/tag')]
# //a[contains(@href,'/tag')]
driver.find_element(By.XPATH, '//label[@class="search_btn" and @id="btnSearch"]')

# 通过文本定位元素
# //a[text()="你好"]
# //a[starts-with(text(),"你好")]
# //a[contains(text(),"你好")]
