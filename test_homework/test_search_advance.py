# 姓名：郭宏亮
# 时间：2023/5/13 17:35
import allure
import pytest

from src.pages.main_page import MainPage


class TestSearchAdvance:
    def setup_class(self):
        self.main_page = MainPage()

    def setup_method(self):
        self.search_advance = self.main_page.goto_search_advance()

    @pytest.mark.parametrize("keyword", ["selenium", "appium", "自动化"])
    @allure.title("(关键字)-(话题)")
    def test_keyword(self, keyword):
        assert keyword in str(self.search_advance.keyword_search(keyword).goto_topic_posts_search().topics[0]).lower()

    @pytest.mark.parametrize("select_type", [1, 2, 3], ids=["话题/帖子", "类别/标签", "用户"])
    @pytest.mark.parametrize("keyword", ["selenium", "appium", "自动化"])
    @allure.title("(关键字)-(话题/类别/用户)")
    def test_select(self, keyword, select_type):
        if select_type == 1:
            # 获取话题帖子选项
            assert self.search_advance.keyword_search(keyword).goto_topic_posts_search().topics
        elif select_type == 2:
            assert self.search_advance.keyword_search(keyword).goto_category_tag_search().categories
        elif select_type == 3:
            assert self.search_advance.keyword_search(keyword).goto_username_search().usernames

    @pytest.mark.parametrize("select_type", [1, 2, 3], ids=["话题/帖子", "类别/标签", "用户"])
    @pytest.mark.parametrize("category_type", range(1, 9))
    @allure.title("(高级：分类)-(话题/类别/用户)")
    def test_category_search(self, select_type, category_type):
        if select_type == 1:
            # 获取话题帖子选项
            assert self.search_advance.category_search(category_type).goto_topic_posts_search().topics
        elif select_type == 2:
            assert self.search_advance.category_search(category_type).goto_category_tag_search().categories
        elif select_type == 3:
            assert self.search_advance.category_search(category_type).goto_username_search().usernames

    @pytest.mark.parametrize("select_type", [1, 2, 3], ids=["话题/帖子", "类别/标签", "用户"])
    @pytest.mark.parametrize("top_status_type", range(1, 7))
    @allure.title("高级：话题-(话题/类别/用户)")
    def test_topic_status_search(self, select_type, top_status_type):
        if select_type == 1:
            # 获取话题帖子选项
            assert self.search_advance.topic_status_search(top_status_type).goto_topic_posts_search().topics
        elif select_type == 2:
            assert self.search_advance.topic_status_search(top_status_type).goto_category_tag_search().categories
        elif select_type == 3:
            assert self.search_advance.topic_status_search(top_status_type).goto_username_search().usernames

    @pytest.mark.parametrize("select_type", [1, 2, 3], ids=["话题/帖子", "类别/标签", "用户"])
    @pytest.mark.parametrize("category_type", range(1, 9))
    @pytest.mark.parametrize("top_status_type", range(1, 7))
    @allure.title("高级：分类+话题-(话题/类别/用户)")
    def test_category_topic_status_search(self, select_type, category_type, top_status_type):
        if select_type == 1:
            # 获取话题帖子选项
            assert self.search_advance.category_search(category_type).topic_status_search(
                top_status_type).goto_topic_posts_search().topics
        elif select_type == 2:
            assert self.search_advance.category_search(category_type).topic_status_search(
                top_status_type).goto_category_tag_search().categories
        elif select_type == 3:
            assert self.search_advance.category_search(category_type).topic_status_search(
                top_status_type).goto_username_search().usernames

    @pytest.mark.parametrize("own_tag", range(2, 7))
    def test_own_tag_search(self, own_tag):
        self.search_advance.own_tag_search(own_tag).get_keyword()
