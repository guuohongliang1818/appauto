# 姓名：郭宏亮
# 时间：2023/5/13 17:35
import allure
import pytest

from src.pages.main_page import MainPage

"""
注意:测试PO的地址链接为
1.https://github.com/guuohongliang1818/appauto/blob/master/src/pages/main_page.py
2.https://github.com/guuohongliang1818/appauto/blob/master/src/pages/search_advance.py
"""


class TestSearchAdvance:
    def setup_class(self):
        self.main_page = MainPage()

    def setup_method(self):
        self.search_advance = self.main_page.goto_search_advance()

    @pytest.mark.parametrize("keyword", ["selenium", "appium", "自动化"])
    @allure.title("(关键字)-(话题)")
    def test_keyword(self, keyword):
        assert keyword in str(
            self.search_advance.keyword_search(keyword).select_type_search(1).get_search_result().search_result[0])

    @pytest.mark.parametrize("select_type", [1, 2, 3], ids=["话题/帖子", "类别/标签", "用户"])
    @pytest.mark.parametrize("keyword", ["selenium", "appium", "自动化"])
    @allure.title("(关键字)-(话题/类别/用户)")
    def test_select(self, keyword, select_type):
        # search_result结果不为空断言为True，如果为空断言失败
        assert bool(self.search_advance.keyword_search(keyword).select_type_search(
            select_type).get_search_result().search_result)

    @pytest.mark.parametrize("select_type", [1, 2, 3], ids=["话题/帖子", "类别/标签", "用户"])
    @pytest.mark.parametrize("category_type", range(1, 6))
    @allure.title("(高级：分类)-(话题/类别/用户)")
    def test_category_search(self, select_type, category_type):
        # search_result结果不为空断言为True，如果为空断言失败
        assert bool(self.search_advance.category_search(category_type).select_type_search(
            select_type).get_search_result().search_result)

    @pytest.mark.parametrize("select_type", [1, 2, 3], ids=["话题/帖子", "类别/标签", "用户"])
    @pytest.mark.parametrize("top_status_type", range(1, 4))
    @allure.title("高级：话题-(话题/类别/用户)")
    def test_topic_status_search(self, select_type, top_status_type):
        # search_result结果不为空断言为True，如果为空断言失败
        assert bool(self.search_advance.topic_status_search(top_status_type).select_type_search(
            select_type).get_search_result().search_result)

    @pytest.mark.parametrize("select_type", [1, 2, 3], ids=["话题/帖子", "类别/标签", "用户"])
    @pytest.mark.parametrize("category_type", range(1, 4))
    @pytest.mark.parametrize("top_status_type", range(1, 4))
    @allure.title("高级：分类+话题-(话题/类别/用户)")
    def test_category_topic_status_search(self, select_type, category_type, top_status_type):
        # search_result结果不为空断言为True，如果为空断言失败
        assert bool(self.search_advance.category_search(category_type).topic_status_search(
            top_status_type).select_type_search(select_type).get_search_result().search_result)

    @pytest.mark.parametrize("select_type", [1, 2, 3], ids=["话题/帖子", "类别/标签", "用户"])
    @pytest.mark.parametrize("own_tag", range(1, 4))
    @allure.title("高级：拥有该标签-(话题/类别/用户)")
    def test_own_tag_search(self, select_type, own_tag):
        # search_result结果不为空断言为True，如果为空断言失败
        assert bool(self.search_advance.own_tag_search(own_tag).select_type_search(
            select_type).get_search_result().search_result)

    @pytest.mark.parametrize("select_type", [1, 2, 3], ids=["话题/帖子", "类别/标签", "用户"])
    @pytest.mark.parametrize("category_type", range(1, 4))
    @pytest.mark.parametrize("top_status_type", range(1, 4))
    @pytest.mark.parametrize("own_tag", range(1, 4))
    @allure.title("高级：分类，话题状态，拥有该标签-(话题/类别/用户)")
    def test_category_topic_status_own_tag_search(self, select_type, category_type, top_status_type, own_tag):
        # search_result结果不为空断言为True，如果为空断言失败
        assert bool(self.search_advance.category_search(category_type).topic_status_search(
            top_status_type).own_tag_search(own_tag).select_type_search(select_type).get_search_result().search_result)

    @pytest.mark.parametrize("only_back_type", range(1, 4))
    @allure.title("高级：只返回-(话题)")
    def test_only_back_search(self, only_back_type):
        # search_result结果不为空断言为True，如果为空断言失败
        assert bool(self.search_advance.only_back_search(only_back_type).get_search_result().search_result)

    @pytest.mark.parametrize("select_type", [1, 2, 3], ids=["话题/帖子", "类别/标签", "用户"])
    @pytest.mark.parametrize("post_person", [["bbbbbbb", "张三"], ["dddd", "ccccc", "王五"]])
    @allure.title("高级：发帖人-(话题/类别/用户)")
    def test_post_person_search(self, post_person, select_type):
        # search_result结果不为空断言为True，如果为空断言失败
        assert bool(self.search_advance.post_person_search(post_person).select_type_search(
            select_type).get_search_result().search_result)

    @pytest.mark.parametrize("select_type", [1, 2, 3], ids=["话题/帖子", "类别/标签", "用户"])
    @pytest.mark.parametrize("date", ["0020230516", "0020220516", "0020221212", "0020231412"])
    @allure.title("高级：日期-(话题/类别/用户)")
    def test_date_search(self, select_type, date):
        # search_result结果不为空断言为True，如果为空断言失败
        assert bool(
            self.search_advance.date_search(date).select_type_search(select_type).get_search_result().search_result)
