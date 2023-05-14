# 姓名：郭宏亮
# 时间：2023/5/13 17:35
import pytest

from src.pages.main_page import MainPage


class TestSearchAdvance:
    def setup_class(self):
        self.main_page = MainPage()

    def setup_method(self):
        self.search_advance = self.main_page.goto_search_advance()

    @pytest.mark.parametrize("keyword", ["selenium", "appium", "自动化"])
    def test_keyword(self, keyword):
        assert keyword in str(self.search_advance.keyword_search(keyword).goto_topic_posts_search()[0]).lower()

    @pytest.mark.parametrize("keyword", ["selenium", "appium", "自动化"])
    @pytest.mark.parametrize("select_type", [1, 2, 3])
    def test_select(self, keyword, select_type):
        if select_type == 1:
            # 获取话题帖子选项
            assert self.search_advance.keyword_search(keyword).goto_topic_posts_search()
        elif select_type == 2:
            assert self.search_advance.keyword_search(keyword).goto_category_tag_search()
        elif select_type == 3:
            assert self.search_advance.keyword_search(keyword).goto_username_search()

    @pytest.mark.parametrize("select_type", [1, 2, 3])
    @pytest.mark.parametrize("category_type", range(2, 9))
    def test_category_search(self, select_type, category_type):
        if select_type == 1:
            # 获取话题帖子选项
            assert self.search_advance.category_search(select_type, category_type).goto_topic_posts_search()
        elif select_type == 2:
            assert self.search_advance.category_search(select_type, category_type).goto_category_tag_search()
        elif select_type == 3:
            assert self.search_advance.category_search(select_type, category_type).goto_username_search()
