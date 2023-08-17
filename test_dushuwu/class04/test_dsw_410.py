# 姓名：郭宏亮
# 时间：2023/8/12 22:28
# 姓名：郭宏亮
# 时间：2023/8/12 21:31
"""
用例标题：验证能够创建收费的章节的书籍
前置条件：登录作者用户并进入到小说章节内容填写页面
测试步骤：
    1.输入对应的章节名
    2.输入对应的章节内容
    3.是否收费：收费
    4.点击提交按钮
预期结果：
    正确显示输入数据，点击提交后成功新建章节，数据库数据更新
    该数据添加成功；产看本章节需要收费
"""
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_dsw_178():
    driver = webdriver.Chrome()
    driver.set_window_size(1400, 700)
    wait = WebDriverWait(driver, 5)
    driver.get("http://novel.hctestedu.com")
    original_hd = driver.current_window_handle
    print("当前页签的句柄：", original_hd)
    # 用户名登录：
    username = "18894687777"
    passwd = "123456"
    book_name = "三峰游泳完美"
    chap_name = "222222222数据库"
    chap_content = """
        RDBMS 术语
        在我们开始学习MySQL 数据库前，让我们先了解下RDBMS的一些术语：

        数据库: 数据库是一些关联表的集合。
        数据表: 表是数据的矩阵。在一个数据库中的表看起来像一个简单的电子表格。
        列: 一列(数据元素) 包含了相同类型的数据, 例如邮政编码的数据。
        行：一行（元组，或记录）是一组相关的数据，例如一条用户订阅的数据。
        冗余：存储两倍数据，冗余降低了性能，但提高了数据的安全性。
        主键：主键是唯一的。一个数据表中只能包含一个主键。你可以使用主键来查询数据。
        外键：外键用于关联两个表。
        复合键：复合键（组合键）将多个列作为一个索引键，一般用于复合索引。
        索引：使用索引可快速访问数据库表中的特定信息。索引是对数据库表中一列或多列的值进行排序的一种结构。类似于书籍的目录。
        参照完整性: 参照的完整性要求关系中不允许引用不存在的实体。与实体完整性是关系模型必须满足的完整性约束条件，目的是保证数据的一致性。
        MySQL 为关系型数据库(Relational Database Management System), 这种所谓的"关系型"可以理解为"表格"的概念, 一个关系型数据库由一个或数个表格组成, 如图所示的一个表格:
    """
    driver.find_element(By.XPATH, "//a[text()='登录']").click()
    wait.until(expected_conditions.text_to_be_present_in_element((By.XPATH, "//h3[text()='登陆读书屋']"), "登陆读书屋"))
    driver.find_element(By.ID, "txtUName").send_keys(username)
    driver.find_element(By.ID, "txtPassword").send_keys(passwd)
    driver.find_element(By.ID, "btnLogin").click()
    # 使用username作为等待条件
    # wait.until(expected_conditions.text_to_be_present_in_element((By.XPATH, f"//a[text()={username}]"), username))
    # By.LINK_TEXT只有是超链接的时候才能使用
    wait.until(expected_conditions.text_to_be_present_in_element((By.LINK_TEXT, username), username))
    # 断言查看当前的用户名
    assert driver.find_element(By.LINK_TEXT, username).text == username
    # 点击作家专区
    driver.find_element(By.XPATH, "//ul[@id='navModule']//a[text()='作家专区']").click()
    # 断言，当前页签数量为2
    assert wait.until(expected_conditions.number_of_windows_to_be(2))
    # 切换当前窗口
    driver.switch_to.window(driver.window_handles[-1])
    sleep(1)
    # print(driver.page_source)
    tr_list = driver.find_elements(By.XPATH, '//*[@id="bookList"]//tr')

    for index, tr in enumerate(tr_list):
        if book_name in tr.text:
            search_index = index + 1
            break

    print("search_index：", search_index)

    button = (By.XPATH, f'//*[@id="bookList"]/tr[{search_index}]//a[contains(text(),"章节管理")]')
    # 鼠标滚动找到bookname的tr章节管理按钮
    ActionChains(driver) \
        .move_to_element(driver.find_element(*button)) \
        .perform()
    # 点击章节管理按钮
    driver.find_element(*button).click()
    # print(wait.until(expected_conditions.number_of_windows_to_be(3)))
    assert wait.until(expected_conditions.number_of_windows_to_be(3))
    # 切换当前窗口
    driver.switch_to.window(driver.window_handles[-1])
    # print(driver.page_source)
    ele = wait.until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//div[@id='hasContentDiv']//a[text()='新建章节']")))
    ele.click()

    # 打开填写章节名称和章节内容页面
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//h3[text()='小说章节内容填写']")))
    # 章节名称
    driver.find_element(By.ID, "bookIndex").send_keys(chap_name)
    # 章节内容
    driver.find_element(By.ID, "bookContent").send_keys(chap_content)

    # 鼠标滑动找到提交按钮
    ActionChains(driver) \
        .move_to_element(driver.find_element(By.ID, "btnRegister")) \
        .perform()

    # 收费
    driver.find_element(By.XPATH, "//input[@value='1']").click()
    # 点击提交
    driver.find_element(By.ID, "btnRegister").click()
    sleep(2)

    # button = (By.XPATH, "//a[starts-with(text(),'章节管理')]")
    # 点击作家专区打开新页签
    # 等待新页签的出现，校验窗口数为2
    # 获取所有的窗口句柄，并切换到新窗口
    # 等待章节管理按钮出现，并点击

    # elements = driver.find_element(*button)
    # 先滚动到提交按钮，
    # 单选按钮，点击收费
    # 点击提交

    # 非常重要结果检查，章节名称和是否收费
    # 检查阅读详情页： 可以重定向

    # 关闭浏览器


if __name__ == '__main__':
    pytest.main(['-v'])
