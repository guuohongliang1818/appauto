# 姓名：郭宏亮
# 时间：2023/8/13 20:21
# 姓名：郭宏亮
# 时间：2023/8/12 22:28
# 姓名：郭宏亮
# 时间：2023/8/12 21:31
"""
点击加入书架，会加入到我的书架中
"""
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.by import By


def test_dsw_182():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://selenium.dev/selenium/web/single_text_input.html")
    sleep(2)
    username = "18899991234"
    passwd = "123456"
    # 定位搜索框
    # ele = driver.find_element(By.XPATH, '//*[@id="searchKey"]')
    ActionChains(driver) \
        .key_down(Keys.SHIFT) \
        .send_keys("abcd") \
        .perform()
    sleep(2)
    ActionChains(driver) \
        .key_up(Keys.SHIFT) \
        .send_keys("eft") \
        .perform()
    sleep(2)
    # 按下shift键
    # ActionChains(driver) \
    #     .key_down(Keys.LEFT_SHIFT) \
    #     .send_keys("zzzz") \
    #     .perform()

    # 释放所有action

    # ActionChains(driver).send_keys("zzzzz").perform()
    # ActionBuilder(driver).clear_actions()
    # sleep(5)


def test_send_keys_to_active_element():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://selenium.dev/selenium/web/single_text_input.html")
    sleep(2)
    ActionChains(driver) \
        .send_keys("abcd") \
        .perform()
    sleep(2)
    print(driver.find_element(By.XPATH, "//input").get_attribute("value"))
    assert driver.find_element(By.XPATH, "//input").get_attribute("value") == 'abcd'


def test_send_keys_to_element():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://selenium.dev/selenium/web/single_text_input.html")
    driver.find_element(By.TAG_NAME, "body").click()
    sleep(2)

    ele = driver.find_element(By.XPATH, "//input")
    ActionChains(driver).send_keys_to_element(ele, "acdv").perform()

    print(driver.find_element(By.XPATH, "//input").get_attribute("value"))
    assert driver.find_element(By.XPATH, "//input").get_attribute("value") == 'acdv'
    sleep(2)


def test_click_and_hold():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://selenium.dev/selenium/web/mouse_interaction.html")

    clickable_ele = driver.find_element(By.XPATH, "//input[@id='clickable']")
    ActionChains(driver) \
        .click_and_hold(clickable_ele) \
        .perform()

    assert driver.find_element(By.XPATH, "//strong[@id='click-status']").text == "focused"


# 常规的点击操作
def test_click_and_release():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://selenium.dev/selenium/web/mouse_interaction.html")

    clickable_ele = driver.find_element(By.XPATH, "//a[@id='click']")
    ActionChains(driver) \
        .click(clickable_ele) \
        .perform()
    sleep(2)
    # assert driver.find_element(By.XPATH, "//strong[@id='click-status']").text == "focused"


# 单击右键
def test_context_click():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://selenium.dev/selenium/web/mouse_interaction.html")

    clickable_ele = driver.find_element(By.XPATH, "//input[@id='clickable']")
    ActionChains(driver) \
        .context_click(clickable_ele) \
        .perform()

    assert driver.find_element(By.XPATH, "//strong[@id='click-status']").text == "context-clicked"


def test_back_click():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://selenium.dev/selenium/web/mouse_interaction.html")

    clickable_ele = driver.find_element(By.XPATH, "//a[@id='click']")
    ActionChains(driver) \
        .click(clickable_ele) \
        .perform()
    sleep(2)

    action = ActionBuilder(driver)
    action.pointer_action.pointer_down(MouseButton.BACK)
    action.pointer_action.pointer_up(MouseButton.BACK)
    action.perform()
    sleep(2)


def test_scroll_to_element():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://selenium.dev/selenium/web/scrolling_tests/frame_with_nested_scrolling_frame_out_of_view.html")

    sleep(2)
    # 定位到底部的frame
    iframe = driver.find_element(By.TAG_NAME, "iframe")

    ActionChains(driver) \
        .scroll_to_element(iframe) \
        .perform()

    sleep(2)


# Scroll by given amount指定数值滚动
"""
负值：向右和向下
正直：向上和向左
"""


def test_scroll_by_given_amount():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://selenium.dev/selenium/web/scrolling_tests/frame_with_nested_scrolling_frame_out_of_view.html")

    sleep(2)
    # 定位到底部的frame
    footer = driver.find_element(By.TAG_NAME, "footer")
    print(footer.rect)
    delta_y = footer.rect["y"]
    print(type(delta_y))

    ActionChains(driver).scroll_by_amount(0, int(delta_y)).perform()
    sleep(3)


if __name__ == '__main__':
    pytest.main(['-v'])
