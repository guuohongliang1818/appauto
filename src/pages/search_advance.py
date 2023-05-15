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
        self.topics = []
        self.categories = []
        self.usernames = []

    def web_driver_wait_xpath(self, xpath):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, xpath)))

    def keyword_search(self, keyword):
        self.driver.find_element(By.CSS_SELECTOR, ".search-query").click()
        query = self.driver.find_element(By.CSS_SELECTOR, ".search-query")
        query.clear()
        query.send_keys(keyword)
        return self

    """
    以下搜素功能是点击"高级筛选器"之后才能使用
    """

    def click_advance_selector(self):
        try:
            self.driver.find_element(By.XPATH, "//details[@open]")
        except NoSuchElementException as e:
            # print("NoSuchElementException", e)
            self.driver.find_element(By.XPATH, "//*[text()='高级筛选器']").click()

    def category_search(self, category_type):
        self.click_advance_selector()
        try:
            # 如果有可以x掉的元素,如果找不到可能会报错
            self.driver.find_element(By.XPATH,
                                     "//summary[@id='search-in-category-header']" +
                                     "/div[@class='select-kit-header-wrapper']/button").click()
        except NoSuchElementException as e:
            pass

        self.driver.find_element(By.XPATH, "//summary[@id='search-in-category-header']").click()
        self.driver.find_element(By.XPATH,
                                 "//div[@id='search-in-category-body']/ul[@class='select-kit-collection']/li[" +
                                 str(category_type) + "]").click()
        return self

    def topic_status_search(self, top_status_type):
        self.click_advance_selector()
        try:
            # 如果有可以x掉的元素,如果找不到可能会报错
            self.driver.find_element(By.XPATH,
                                     "//summary[@id='search-status-options-header']" +
                                     "/div[@class='select-kit-header-wrapper']/button").click()
        except NoSuchElementException as e:
            pass
        self.driver.find_element(By.XPATH, "//summary[@id='search-status-options-header']").click()
        self.driver.find_element(By.XPATH,
                                 "//div[@id='search-status-options-body']/ul[@class='select-kit-collection']/li[" +
                                 str(top_status_type) + "]").click()
        return self

    def own_tag_search(self, count):
        self.click_advance_selector()
        self.driver.find_element(By.XPATH, "//summary[@id='search-with-tags-header']").click()

        # 如果有可以x掉的元素,如果找不到可能会报错，将多选的元素全部去掉,这样不停的实时获取元素，可能会报错stale element reference
        while True:
            try:
                # 循环删除被选中的元素，从头开始删除，如果找不到元素，说明已被全部删除，捕获异常跳出循环
                self.driver.find_element(By.XPATH, "//div[@class='selected-content']/button[1]").click()
            except BaseException as e:
                print("===异常===", e)
                break

        for i in range(1, count + 1):
            # WebDriverWait(self.driver, 20).until(
            #     expected_conditions.visibility_of_element_located(
            #         (By.XPATH, "//div[@id='search-with-tags-body']/ul")))
            self.web_driver_wait_xpath("//div[@id='search-with-tags-body']/ul")
            self.driver.find_element(By.XPATH,
                                     "//div[@id='search-with-tags-body']" +
                                     "/ul[@class='select-kit-collection']/li[1]").click()
        return self

    def post_person_search(self):
        self.driver.find_element(By.XPATH, "//summary[@id='search-posted-by-header']").click()
        self.driver.find_element(By.XPATH, "//input[@name='filter-input-search']").send_keys("张三")
        self.web_driver_wait_xpath("//div[@id='search-posted-by-body']/ul[@class='select-kit-collection']/li")

    def mutil_search(self):
        pass

    def date_search(self):
        pass

    def goto_topic_posts_search(self):
        self.driver.find_element(By.XPATH, "//details[@id='search-type']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".select-kit-collection>li[title='话题/帖子']").click()
        # 点击搜索按钮
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary.search-cta").click()
        # 显示等待返回结果
        # WebDriverWait(self.driver, 20).until(
        #     expected_conditions.visibility_of_element_located(
        #         (By.XPATH, "//span[@class='topic-title'] | //h3[text()='找不到结果。']")))
        self.web_driver_wait_xpath("//span[@class='topic-title'] | //h3[text()='找不到结果。']")
        # 将列表题返回
        for element in self.driver.find_elements(By.XPATH, "//span[@class='topic-title'] | //h3[text()='找不到结果。']"):
            self.topics.append(element.text)
        print("topics", self.topics)
        return self

    def goto_category_tag_search(self):
        self.driver.find_element(By.XPATH, "//details[@id='search-type']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".select-kit-collection>li[title='类别/标签']").click()
        # 点击搜索按钮
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary.search-cta").click()
        # 显示等待返回结果
        # WebDriverWait(self.driver, 20).until(
        #     expected_conditions.visibility_of_element_located(
        #         (By.XPATH,
        #          "//span[@class='category-name'] | //a[starts-with(@href,'/tag')] | //h3[text()='找不到结果。']")))
        self.web_driver_wait_xpath(
            "//span[@class='category-name'] | //a[starts-with(@href,'/tag')] | //h3[text()='找不到结果。']")
        # print("category", self.driver.find_element(By.CSS_SELECTOR, ".category-items .badge-category").text)
        for cat in self.driver.find_elements(By.XPATH,
                                             "//span[@class='category-name'] " +
                                             "| //a[starts-with(@href,'/tag')] " +
                                             "| //h3[text()='找不到结果。']"):
            self.categories.append(cat.text)
        print("categories", self.categories)
        return self

    def goto_username_search(self):
        self.driver.find_element(By.XPATH, "//details[@id='search-type']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".select-kit-collection>li[title='用户']").click()
        # 点击搜索按钮
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary.search-cta").click()
        # 显示等待返回结果
        # WebDriverWait(self.driver, 20).until(
        #     expected_conditions.visibility_of_element_located(
        #         (By.XPATH, "//span[@class='username'] | //h3[text()='找不到结果。']")))
        self.web_driver_wait_xpath("//span[@class='username'] | //h3[text()='找不到结果。']")
        self.driver.find_elements(By.XPATH, "//span[@class='username'] | //h3[text()='找不到结果。']")
        for user in self.driver.find_elements(By.XPATH, "//span[@class='username'] | //h3[text()='找不到结果。']"):
            self.usernames.append(user.text)
        print("usernames", self.usernames)
        return self

    def get_keyword(self):
        values = self.driver.find_element(By.CSS_SELECTOR, ".search-query").get_attribute("value")
        print("=====values=====", values)


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    lst.clear()
    print("=====", lst)
