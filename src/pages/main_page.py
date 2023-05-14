# 姓名：郭宏亮
# 时间：2023/5/13 16:47
from selenium import webdriver
from selenium.webdriver.common.by import By

from src.pages.search_advance import SearchAdvance


class MainPage:
    pass

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")
        self.driver.set_window_size(1056, 814)

    def setup_method(self):
        pass

    def goto_search_advance(self):
        self.driver.find_element(By.CSS_SELECTOR, "#search-button[title=搜索]").click()
        self.driver.find_element(By.CSS_SELECTOR, ".show-advanced-search").click()
        return SearchAdvance(self.driver)
