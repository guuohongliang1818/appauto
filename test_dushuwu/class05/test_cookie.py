# 姓名：郭宏亮
# 时间：2023/8/18 10:11
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# chrome使用debug模式，
def test_debug_driver():
    # os.popen("d:/start.bat")
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("http://novel.hctestedu.com/")
    wait = WebDriverWait(driver, 5)

    username = "18894687777"
    passwd = "123456"

    # driver.find_element(By.XPATH, "//a[text()='登录']").click()
    # wait.until(expected_conditions.text_to_be_present_in_element((By.XPATH, "//h3[text()='登陆读书屋']"), "登陆读书屋"))
    # driver.find_element(By.ID, "txtUName").send_keys(username)
    # driver.find_element(By.ID, "txtPassword").send_keys(passwd)
    # driver.find_element(By.ID, "btnLogin").click()

    driver.add_cookie({"name": "HMACCOUNT_BFESS", "value": "5D8755D9182165D8"})
    driver.add_cookie({"name": "Hm_lvt_ecc8b50a3122e6d5e09be7a9e5383e07", "value": "1692437551"})
    driver.add_cookie({"name": "BIDUPSID", "value": "4DA68D0BFBA5D40DE656B2853F8622DA"})
    driver.add_cookie({"name": "Authorization",
                       "value": "eyJhbGciOiJIUzUxMiJ9.eyJleHAiOjE2OTMwNDIzNzEsInN1YiI6IntcImlkXCI6MTU4NjEzODIzNjM4NDU1MDkxMixcInVzZXJuYW1lXCI6XCIxODg5NDY4Nzc3N1wiLFwibmlja05hbWVcIjpcIjE4ODk0Njg3Nzc3XCJ9IiwiY3JlYXRlZCI6MTY5MjQzNzU3MTgyMH0.5TlkOYm40rz73acNU8zyk2n6RZXe9ovndNku-7yTa9Wywjc8xGDf7uQafWsTIVVL8XBx8e7AJMPNhtht4c2V0g"})
    driver.add_cookie({"name": "userClientMarkKey", "value": "b920cd135a0f43d3b52ab0d4aaa16561"})

    driver.refresh()

    print(driver.get_cookies())
    sleep(10)
