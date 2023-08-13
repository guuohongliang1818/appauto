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
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_dsw_180():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # 该网址经常打不开，需要保存源码
    driver.get("https://sahitest.com/demo/selectTest.htm")
    sleep(2)
    # 创建一个select对象
    select_ele = driver.find_element(By.ID, 's1Id')
    select_object = Select(select_ele)
    # 通过索引
    select_object.select_by_index(1)
    sleep(2)

    # 通过value属性值
    select_object.select_by_value("o2")
    sleep(2)
    # 通过选项文本
    select_object.select_by_visible_text("o3")
    sleep(2)

    # 检查所有被选择的选项
    # 选中的所有选项
    print(select_object.all_selected_options)
    # 选中的第一个选项
    print(select_object.first_selected_option)
    # 下拉的所有选项
    print(select_object.options)

    # 取消所有选中的选项，仅使用于多选列表
    mutil_select_ele = driver.find_element(By.ID, "s4Id")
    mutil_select_object = Select(mutil_select_ele)
    print(mutil_select_object.is_multiple)
    print("进行多选操作")
    mutil_select_object.select_by_index(1)
    mutil_select_object.select_by_index(2)
    mutil_select_object.select_by_index(3)
    sleep(2)
    print(mutil_select_object.all_selected_options)

    print("通过选项的索引取消")
    mutil_select_object.deselect_by_index(1)
    mutil_select_object.deselect_by_value("o3val")
    sleep(2)

    mutil_select_object.deselect_all()
    sleep(2)


if __name__ == '__main__':
    pytest.main(['-v'])
