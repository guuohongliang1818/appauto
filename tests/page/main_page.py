# 姓名：郭宏亮
# 时间：2023/5/13 15:15
# 每一个页面对应一个page
# 每个页面中的功能（单击事件等），对应一个方法
from selenium import webdriver
from selenium.webdriver.common.by import By

from tests.page.search_page import SearchPage


class MainPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")
        self.driver.set_window_size(1056, 814)

    def close(self):
        self.driver.close()

    def get_topic_list(self):
        pass

    def to_search_advance(self):
        # 调到高级页面
        self.driver.find_element(By.CSS_SELECTOR, "#search-button[title=搜索]").click()
        self.driver.find_element(By.CSS_SELECTOR, ".show-advanced-search").click()
        return SearchPage(self.driver)
