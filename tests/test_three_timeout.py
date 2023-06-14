# 姓名：郭宏亮
# 时间：2023/6/14 10:39
from time import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestThreeTimeout:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get("C:/Users/guohongliang/Desktop/test.html")
        self.driver.set_window_size(1056, 814)
        self.driver.implicitly_wait(5)

    # def find_element(self, path, timeout):
    #     start = time()
    #     while True:
    #         try:
    #             return self.driver.find_element(By.XPATH, path)
    #         except Exception as e:
    #             end = time()
    #             if end - start > timeout:
    #                 print("超时未找到元素")
    #                 break
    #             else:
    #                 print("耗时：", (end - start))
    #
    # def test_find_element_two(self):
    #     self.find_element("//pp", 2)

    def test_find_element(self):
        start = time()
        try:
            print("==========", self.driver.title)
            # WebDriverWait(self.driver, 2).until(
            #     expected_conditions.visibility_of_element_located((By.XPATH, "//pp")))
            self.driver.find_elements(By.XPATH, "//pp")
        except Exception as e:
            print("抛出异常", e)
        finally:
            end = time()
            print("执行时间为：", (end - start))
