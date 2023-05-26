# 姓名：郭宏亮
# 时间：2023/5/24 20:41
import os.path
from time import sleep

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from test_webview import get_project


class TestAppBrowser:

    def setup_class(self):
        caps = {}
        caps["platformName"] = "Android"
        # caps["appPackage"] = "io.appium.android.apis"
        # caps["appActivity"] = "io.appium.android.apis.ApiDemos"
        caps["browserName"] = "chrome"
        caps["appium:settings[waitForIdleTimeout]"] = 0
        caps["appium:ensureWebviewsHavePages"] = True
        caps["appium:nativeWebScreenshot"] = True
        caps["appium:newCommandTimeout"] = 3600
        caps["appium:connectHardwareKeyboard"] = True
        # caps["chromedriverExecutableDir"] = os.path.join(get_project(), "bin")
        caps["chromedriverExecutableDir"] = "D:/pythoncode/appauto/test_webview"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.get("https://ceshiren.com")

    # def teardown_class(self):
    #     self.driver.close()

    # 使用原生定位
    def test1(self):
        pass

    def test2(self):
        pass
