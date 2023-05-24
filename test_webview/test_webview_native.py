# 姓名：郭宏亮
# 时间：2023/5/24 20:41
from time import sleep

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait


class TestWebviewNative:

    def setup_class(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = "io.appium.android.apis.ApiDemos"
        caps["appium:settings[waitForIdleTimeout]"] = 0
        caps["appium:ensureWebviewsHavePages"] = True
        caps["appium:nativeWebScreenshot"] = True
        caps["appium:newCommandTimeout"] = 3600
        caps["appium:connectHardwareKeyboard"] = True
        caps["chromedriverExecutableDir"] = "./"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)

    # def teardown_class(self):
    #     self.driver.close()

    # 使用原生定位
    def test1(self):
        self.driver.find_element(by=AppiumBy.XPATH,
                                 value="//android.widget.TextView[@content-desc='Views']").click()
        size = self.driver.get_window_size()
        width_max = size['width']
        height_max = size['height']

        def swipe_to(driver):
            self.driver.swipe(width_max * 0.5, height_max * 0.8, width_max * 0.5, height_max * 0.2)
            return self.driver.find_element(by=AppiumBy.XPATH,
                                            value="//android.widget.TextView[@content-desc='WebView']")

        ele = WebDriverWait(self.driver, 10).until(swipe_to)
        print(ele)
        ele.click()
        for i in range(5):
            sleep(1)
            print(self.driver.contexts)
            print(self.driver.page_source)

        # 没有切换上文，使用原生定位，XPATH
        # self.driver.find_element(by=AppiumBy.ID, value="i_am_a_textbox").send_keys("ceshiren.com")
        self.driver.find_element(by=AppiumBy.XPATH,
                                 value="//android.widget.EditText[@text='i has no focus']").send_keys("ceshiren.com")

    # webview使用上下文切换
    def test2(self):
        self.driver.find_element(by=AppiumBy.XPATH,
                                 value="//android.widget.TextView[@content-desc='Views']").click()
        size = self.driver.get_window_size()
        width_max = size['width']
        height_max = size['height']

        def swipe_to(driver):
            self.driver.swipe(width_max * 0.5, height_max * 0.8, width_max * 0.5, height_max * 0.2)
            return self.driver.find_element(by=AppiumBy.XPATH,
                                            value="//android.widget.TextView[@content-desc='WebView']")

        ele = WebDriverWait(self.driver, 10).until(swipe_to)
        print(ele)
        ele.click()
        print("切换前", self.driver.page_source)
        print("contexts:", self.driver.contexts)
        WebDriverWait(self.driver, 10).until(lambda x: len(self.driver.contexts) == 2)
        print("等待出现两个webview：contexts:", self.driver.contexts)
        # 开始下文切换
        web_view = self.driver.contexts[-1]
        self.driver.switch_to.context(web_view)
        print("切换后", self.driver.page_source)
