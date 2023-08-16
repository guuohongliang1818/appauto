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
    driver.maximize_window()
    driver.get("http://novel.hctestedu.com")
    # 原始窗口句柄id
    original_hd = driver.current_window_handle
    print("原始窗口句柄id", original_hd)
    sleep(2)
    # 打印所有的其他页签
    print(driver.window_handles)
    assert len(driver.window_handles) == 1

    # 点击作家专栏
    driver.find_element(By.XPATH, "//div[@id='mainNav']//a[text()='作家专区']").click()
    # 等待新窗口或标签页被打开
    WebDriverWait(driver, 5).until(expected_conditions.number_of_windows_to_be(2))
    sleep(2)
    # 获取所有的窗口页签
    # new_hd = driver.current_window_handle
    # print("当前窗口的句柄id", new_hd)
    print(driver.window_handles)

    # 切换窗口，方式1：循环执行，知道找到新的窗口句柄
    '''
    for hd in driver.window_handles:
        if hd != original_hd:
            driver.switch_to.window(hd)
            break
    print("当前窗口的句柄id", driver.current_window_handle)
    '''
    # 切换窗口，方式1：切换到新打开的窗口
    # n=1，原始的是0，一次类推
    # n=-1，代表最后一个打开的页签
    driver.switch_to.window(driver.window_handles[-1])
    print("当前窗口的句柄id", driver.current_window_handle)

    # 等待新页签完成加载内容，通过标题
    WebDriverWait(driver, 5).until(expected_conditions.title_is("会员登录_读书屋"))
    # 进行登录操作
    username = "18899991234"
    passwd = "123456"

    driver.find_element(By.XPATH, "//a[text()='登录']").click()

    driver.find_element(By.ID, "txtUName").send_keys(username)
    driver.find_element(By.ID, "txtPassword").send_keys(passwd)
    driver.find_element(By.ID, "btnLogin").click()
    sleep(2)
    # 关闭当前页签和窗口
    driver.close()
    # driver.quit()退出浏览器

    # 切回到原始的窗口完成刷新页面，完成加载内容
    driver.switch_to.window(original_hd)
    sleep(2)
    driver.refresh()
    sleep(2)


if __name__ == '__main__':
    pytest.main(['-v'])
