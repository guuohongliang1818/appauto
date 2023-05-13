# 姓名：郭宏亮
# 时间：2023/5/13 15:19
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SearchPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def close(self):
        self.driver.close()

    # return SearchPage
    def search(self, keyword):
        self.driver.find_element(By.CSS_SELECTOR, "input.search-query").click()
        query = self.driver.find_element(By.CSS_SELECTOR, "input.search-query")
        query.clear()
        query.send_keys(keyword)
        return self

    # 获取返回结果
    def get_search_result(self):
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary.search-cta").click()
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".topic-title")))
        print(self.driver.find_elements(By.CSS_SELECTOR, ".topic-title"))
        titles = []
        for element in self.driver.find_elements(By.CSS_SELECTOR, ".topic-title"):
            titles.append(element.text)
        return titles
