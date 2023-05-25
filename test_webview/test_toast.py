# 姓名：郭宏亮
# 时间：2023/5/25 23:04
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait


class TestToast:
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
        # caps["chromedriverExecutableDir"] = os.path.join(get_project(), "bin")
        caps["chromedriverExecutableDir"] = "D:/pythoncode/appauto/test_webview"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)
        self.driver.find_element(by=AppiumBy.XPATH,
                                 value="//android.widget.TextView[@content-desc='Views']").click()
        size = self.driver.get_window_size()
        width_max = size['width']
        height_max = size['height']

        def swipe_to(driver):
            self.driver.swipe(width_max * 0.5, height_max * 0.8, width_max * 0.5, height_max * 0.2)
            return self.driver.find_element(by=AppiumBy.XPATH,
                                            value="//android.widget.TextView[@content-desc='Popup Menu']")

        WebDriverWait(self.driver, 10).until(swipe_to).click()

    def test_toast(self):
        self.driver.find_element(by=AppiumBy.XPATH,
                                 value="//android.widget.Button[@content-desc='Make a Popup!']").click()
        self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[1]").click()
        context = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Toast").text
        print(context)
