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
    with webdriver.Chrome() as driver:
        driver.maximize_window()
        driver.get("http://novel.hctestedu.com")
        sleep(2)
        # 分别获取窗口的宽高
        # 设置窗口大小
        driver.set_window_size(1024, 770)
        sleep(2)
        size = driver.get_window_size()
        print("size", size)
        print("width", size.get("width"))
        print("height", size.get("height"))

        # 获取窗口的位置，浏览器左上角的坐标
        position = driver.get_window_position()
        print("position", position)
        sleep(2)
        # 将窗口移动到主显示器的左上角

        driver.set_window_position(0, 0)
        sleep(2)

        # 最大化
        driver.maximize_window()
        sleep(2)
        # 最小化
        driver.minimize_window()
        sleep(2)
        # 最大化
        driver.maximize_window()
        sleep(2)
        # 全屏
        driver.fullscreen_window()
        sleep(2)


if __name__ == '__main__':
    pytest.main(['-v'])
