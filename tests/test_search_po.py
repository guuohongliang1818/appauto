# 姓名：郭宏亮
# 时间：2023/5/13 15:21
from tests.page.main_page import MainPage


class TestSearchPO:

    def setup_class(self):
        self.main_page = MainPage()

    def setup_method(self):
        self.search = self.main_page.to_search_advance()

    def teardown_class(self):
        self.main_page.close()

    def test_search(self):
        assert "selenium" in str(self.search
                                 .search("selenium")
                                 .get_search_result()[0].lower())

    def test_search2(self):
        assert "appium" in str(self.search
                               .search("appium")
                               .get_search_result()[0].lower())
