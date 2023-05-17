# 姓名：郭宏亮
# 时间：2023/5/13 16:48
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SearchAdvance:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.topics = []
        self.categories = []
        self.usernames = []
        self.search_result = []

    def web_driver_wait_xpath(self, xpath):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, xpath)))

    # 通过关键字搜索查询
    def keyword_search(self, keyword):
        self.driver.find_element(By.CSS_SELECTOR, ".search-query").click()
        query = self.driver.find_element(By.CSS_SELECTOR, ".search-query")
        query.clear()
        query.send_keys(keyword)
        return self

    # 下拉切换-话题/帖子-类别/标签-用户搜索
    def select_type_search(self, select_type):
        self.driver.find_element(By.XPATH, "//summary[@id='search-type-header']").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-type-body']"
                                           "/ul[@class='select-kit-collection']/li[" + str(select_type) + "]").click()
        return self

    """
    以下搜素功能是点击"高级筛选器"之后才能使用
    """

    # 点击"高级筛选器"
    def click_advance_selector(self):
        try:
            self.driver.find_element(By.XPATH, "//details[@open]")
        except BaseException as e:
            # print("NoSuchElementException", e)
            self.driver.find_element(By.XPATH, "//*[text()='高级筛选器']").click()

    # 高级筛选器：分类
    def category_search(self, category_type):
        self.click_advance_selector()
        try:
            # 如果有可以x掉的元素,如果找不到可能会报错
            self.driver.find_element(By.XPATH,
                                     "//summary[@id='search-in-category-header']" +
                                     "/div[@class='select-kit-header-wrapper']/button").click()
        except BaseException as e:
            pass

        self.driver.find_element(By.XPATH, "//summary[@id='search-in-category-header']").click()
        self.driver.find_element(By.XPATH,
                                 "//div[@id='search-in-category-body']/ul[@class='select-kit-collection']/li[" +
                                 str(category_type) + "]").click()
        return self

    # 高级筛选器：话题(状态)
    def topic_status_search(self, top_status_type):
        self.click_advance_selector()
        try:
            # 如果有可以x掉的元素,如果找不到可能会报错
            self.driver.find_element(By.XPATH,
                                     "//summary[@id='search-status-options-header']" +
                                     "/div[@class='select-kit-header-wrapper']/button").click()
        except BaseException as e:
            pass
        self.driver.find_element(By.XPATH, "//summary[@id='search-status-options-header']").click()
        self.driver.find_element(By.XPATH,
                                 "//div[@id='search-status-options-body']/ul[@class='select-kit-collection']/li[" +
                                 str(top_status_type) + "]").click()
        return self

    # 高级筛选器：拥有该标签
    def own_tag_search(self, count):
        self.click_advance_selector()
        self.driver.find_element(By.XPATH, "//summary[@id='search-with-tags-header']").click()

        # 如果有可以x掉的元素,如果找不到可能会报错，将多选的元素全部去掉,这样不停的实时获取元素，可能会报错stale element reference
        while True:
            try:
                # 循环删除被选中的元素，从头开始删除，如果找不到元素，说明已被全部删除，捕获异常跳出循环
                self.driver.find_element(By.XPATH, "//div[@id='search-with-tags-body']"
                                                   "/div[@class='selected-content']/button[1]").click()
            except BaseException as e:
                # print("===异常===", e)
                break

        for i in range(1, count + 1):
            self.web_driver_wait_xpath("//div[@id='search-with-tags-body']" +
                                       "/ul[@class='select-kit-collection']/li[1]")
            self.driver.find_element(By.XPATH,
                                     "//div[@id='search-with-tags-body']" +
                                     "/ul[@class='select-kit-collection']/li[1]").click()
        return self

    # 高级筛选器：发帖人
    def post_person_search(self, post_person):

        self.click_advance_selector()
        # 弹出搜索框
        self.driver.find_element(By.XPATH, "//summary[@id='search-posted-by-header']").click()

        # 如果有，清空之前所选的元素
        try:
            self.driver.find_element(By.XPATH,
                                     "//div[@id='search-posted-by-body']" +
                                     "/div[@class='selected-content']/button").click()
        except BaseException as e:
            pass
        for person in post_person:
            try:
                # 先清空之前填的内容
                search_word = self.driver.find_element(By.XPATH, "//input[@name='filter-input-search']")
                search_word.clear()
                # 输入内容
                search_word.send_keys(person)
                # 获取查询结果
                self.web_driver_wait_xpath("//div[@id='search-posted-by-body']/ul[@class='select-kit-collection']/li "
                                           " | //span[@class='no-content']")
                # 如果有下拉，获取第一个，没有下拉，则抛出异常，继续查询
                self.driver.find_element(By.XPATH,
                                         "//div[@id='search-posted-by-body']" +
                                         "/ul[@class='select-kit-collection']/li[1]").click()
                break
            except BaseException as e:
                # print("BaseException", e)
                continue

        return self

    # 高级筛选器：只返回
    def only_back_search(self, only_back_type):
        self.click_advance_selector()
        try:
            self.driver.find_element(By.XPATH,
                                     "//summary[@id='in-header']" +
                                     "/div[@class='select-kit-header-wrapper']/button").click()
        except BaseException as e:
            pass

        self.driver.find_element(By.XPATH, "//summary[@id='in-header']").click()
        self.driver.find_element(By.XPATH, "//div[@id='in-body']/ul[@class='select-kit-collection']/li[" + str(
            only_back_type) + "]").click()
        return self

    # 高级筛选器：早于，晚于
    def early_late(self):

        button = self.driver.find_element(By.XPATH, "//summary[@id='postTime-header']")
        value = button.get_attribute("data-value")
        button.click()
        print("===value===", value)
        if value == "before":
            self.driver.find_element(By.XPATH, "//div[@id='postTime-body']/ul/li[@data-value='after']").click()
        else:
            self.driver.find_element(By.XPATH, "//div[@id='postTime-body']/ul/li[@data-value='before']").click()

    # 高级筛选器：日期查询
    def date_search(self):
        # 打开高级筛选框
        self.click_advance_selector()
        self.early_late()

        return self

    def get_search_result(self):
        # 点击搜索按钮
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary.search-cta").click()
        # 话题帖子，类别/标签，用户的搜索结果
        result_path = "//span[@class='topic-title'] " \
                      "| //span[@class='category-name'] | //a[starts-with(@href,'/tag')] " \
                      "| //span[@class='username'] " \
                      "| //h3[text()='找不到结果。']" \
                      "| //div[text()='您的搜索词过短。']"
        result_xpath1 = "//span[@class='topic-title' or @class='category-name' or @class='username'] " \
                        "| //a[starts-with(@href,'/tag')] " \
                        "| //h3[text()='找不到结果。']" \
                        "| //div[text()='您的搜索词过短。']"
        # self.web_driver_wait_xpath(result_path)
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_any_elements_located((By.XPATH, result_path)))
        for item in self.driver.find_elements(By.XPATH, result_path):
            self.search_result.append(item.text)
        # 打印出的search_result列表会有空字符串
        # 例如['', '求助AppCrawler IOS XPATH中存在特殊属性@value=‘Password_#9; ’ 查找失败', '开源项目']
        print("search_result", self.search_result)
        return self

    # 该方法已废弃
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

    # 该方法已废弃
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

    # 该方法已废弃
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
