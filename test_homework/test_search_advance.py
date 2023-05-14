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
        assert keyword in str(self.search_advance.keyword_search(keyword).get_topic_result()[0]).lower()

    @pytest.mark.parametrize("keyword", ["selenium", "appium", "自动化"])
    @pytest.mark.parametrize("select_type", [1, 2, 3])
    def test_select(self, keyword, select_type):
        # print("=========", self.search_advance.select_search(keyword, select_type))
        result = self.search_advance.select_search(keyword, select_type)
        assert result

    @pytest.mark.parametrize("select_type", [1, 2, 3])
    @pytest.mark.parametrize("category_type", range(2, 9))
    def test_category_search(self, select_type, category_type):
        # print("=========", self.search_advance.select_search(keyword, select_type))
        assert self.search_advance.category_search(select_type, category_type)
