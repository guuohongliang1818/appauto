# 姓名：郭宏亮
# 时间：2023/8/18 10:11
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


# chrome使用debug模式，
# netstat -ano | findstr
# taskkill /f /pid 45116
def test_debug_driver():
    # 使用编写的脚本start.bat,以debug形式启动浏览器
    # 建议通过脚本文件来运行
    # 使用os.system("chrome.exe --remote-debugging-port=9222")
    # os.popen("d:/start.bat")
    # os.system("chrome.exe --remote-debugging-port=9222")
    # sleep(2)
    options = webdriver.ChromeOptions()
    options.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=options)
    # driver.maximize_window()
    # driver.get("https://cart.taobao.com/cart.htm")
    # sleep(1)
    # driver.find_element(By.ID, "fm-login-id").send_keys("ghl807834167")
    # driver.find_element(By.ID, "fm-login-password").send_keys("go35@k0a")
    # driver.find_element(By.XPATH, "//button").click()
    # ele = driver.find_element(By.LINK_TEXT, "维他柠檬茶茶饮料250ml*6盒网红真茶真柠檬家庭囤货聚餐")
    # ele.click()
    # sleep(2)
    current_hd = driver.current_window_handle
    print("current_hd", current_hd)
    print(driver.window_handles)
    for hd in driver.window_handles:
        if current_hd != hd:
            switch_to = hd
            break
    print("switch_to", switch_to)
    driver.switch_to.window(switch_to)
