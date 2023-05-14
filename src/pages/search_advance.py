# 姓名：郭宏亮
# 时间：2023/5/13 16:48
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SearchAdvance:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def keyword_search(self, keyword):
        self.driver.find_element(By.CSS_SELECTOR, ".search-query").click()
        query = self.driver.find_element(By.CSS_SELECTOR, ".search-query")
        query.clear()
        query.send_keys(keyword)
        return self

    # def select_search(self, keyword, select_type):
    #     # 获取下拉
    #     # print("#search-type", self.driver.find_element(By.XPATH, "//details[@id='search-type']"))
    #     # self.driver.find_element(By.XPATH, "//details[@id='search-type']").click()
    #     if select_type == 1:
    #         # 获取话题帖子选项
    #         return self.keyword_search(keyword).goto_topic_posts_search()
    #     elif select_type == 2:
    #         return self.keyword_search(keyword).goto_category_tag_search()
    #     elif select_type == 3:
    #         return self.keyword_search(keyword).goto_username_search()

    """
    以下搜素功能是点击"高级筛选器"之后才能使用
    """

    def click_advance_selector(self):
        try:
            self.driver.find_element(By.XPATH, "//details[@open]")
        except NoSuchElementException as e:
            print("NoSuchElementException", e)
            self.driver.find_element(By.XPATH, "//*[text()='高级筛选器']").click()

    def category_search(self, category_type):
        self.click_advance_selector()
        # 清空搜索框中的内容
        query = self.driver.find_element(By.CSS_SELECTOR, ".search-query")
        query.clear()
        self.driver.find_element(By.XPATH, "//details[@id='search-in-category']").click()
        self.driver.find_element(By.XPATH,
                                 "//ul[@class='select-kit-collection']/li[" + str(category_type) + "]").click()
        return self

    def topic_search(self):
        pass

    def tag_search(self):
        pass

    def person_search(self):
        pass

    def mutil_search(self):
        pass

    def date_search(self):
        pass

    def goto_topic_posts_search(self):
        # 默认首次进入首页的查询
        # self.driver.find_element(By.XPATH, "//details[@id='search-type']").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".select-kit-collection>li[title='话题/帖子']").click()
        topic = []
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary.search-cta").click()
        # 显示等待返回结果
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".topic-title")))
        # 将列表题返回
        for element in self.driver.find_elements(By.CSS_SELECTOR, ".topic-title"):
            topic.append(element.text)
        print("topic", topic)
        return topic

    def goto_category_tag_search(self):
        category = []
        self.driver.find_element(By.XPATH, "//details[@id='search-type']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".select-kit-collection>li[title='类别/标签']").click()
        # 点击搜索按钮
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary.search-cta").click()
        # 显示等待返回结果
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH,
                 "//span[@class='category-name'] | //a[starts-with(@href,'/tag')] | //h3[text()='找不到结果。']")))
        # print("category", self.driver.find_element(By.CSS_SELECTOR, ".category-items .badge-category").text)
        for cat in self.driver.find_elements(By.XPATH,
                                             "//span[@class='category-name'] | //a[starts-with(@href,'/tag')] | //h3[text()='找不到结果。']"):
            category.append(cat.text)
        print("category", category)
        return category

    def goto_username_search(self):
        username = []
        self.driver.find_element(By.XPATH, "//details[@id='search-type']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".select-kit-collection>li[title='用户']").click()
        # 点击搜索按钮
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary.search-cta").click()
        # 显示等待返回结果
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//span[@class='username'] | //h3[text()='找不到结果。']")))
        self.driver.find_elements(By.XPATH, "//span[@class='username'] | //h3[text()='找不到结果。']")
        for user in self.driver.find_elements(By.XPATH, "//span[@class='username'] | //h3[text()='找不到结果。']"):
            username.append(user.text)
        print("username", username)
        return username
