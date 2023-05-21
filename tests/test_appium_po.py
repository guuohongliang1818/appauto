from time import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait


class TestAppiumClock:

    def setup_class(self):
        caps = {}
        caps["platformName"] = "android"
        caps["appPackage"] = "com.android.deskclock"
        caps["appActivity"] = "com.android.deskclock.DeskClock"
        caps["settings[waitForIdleTimeout]"] = 0
        caps["appium:ensureWebviewsHavePages"] = True
        caps["appium:nativeWebScreenshot"] = True
        caps["appium:newCommandTimeout"] = 3600
        caps["appium:connectHardwareKeyboard"] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)

    @pytest.mark.parametrize("city", ["shanghai", "beijing"])
    def test_clock(self, city):
        driver = self.driver
        # el17 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Clock")
        # el17.click()
        el18 = driver.find_element(by=AppiumBy.XPATH,
                                   value="//androidx.appcompat.app.ActionBar.Tab[@content-desc='Clock']/android.widget.TextView")
        el18.click()

        el19 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Cities")
        el19.click()

        el21 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Search")
        el21.click()

        el22 = driver.find_element(by=AppiumBy.ID, value="com.android.deskclock:id/search_src_text")
        el22.send_keys(city)

        #
        # el22 = WebDriverWait(driver, 20).until(all_time_click)
        # el22 = driver.find_element(by=AppiumBy.ID, value="com.android.deskclock:id/search_src_text")
        # el22.send_keys("Shanghai")

        el23 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=city.capitalize())
        el23.click()

        el24 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
        el24.click()

    """
        问题是：连续三次点击"Lap"按钮，分段计时三次，很难进行点击操作。
        问题原因：appium基础知识,appium分析页面控件的时候，必须等页面处于一种稳定（或静止）的状态，
                如果页面上有东西一直在动，下一次点击"Lap"事件会一直在等，无法及时进行事件操作，等待超时时间出现
        问题处理：在caps中添加参数"settings[waitForIdleTimeout]"=0，当界面不停变化的时候，不要等界面处于空闲状态
                《本质上是：一个界面里面有一个线程不停地在运行，则另一个线程会尝试的去等待线程结束(即页面稳定之后)，再去进行下一步操作，要不然定位出来得到控件不稳定，可能会消失》
                settings[waitForIdleTimeout]该值默认为10秒，需要设置为0就可以了
    
    """

    def test_stop_watch(self):
        self.driver.find_element(AppiumBy.XPATH,
                                 "//androidx.appcompat.app.ActionBar.Tab[@content-desc='Stopwatch']/android.widget.TextView").click()

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Start").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Lap").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Lap").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Lap").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Pause").click()

    def teardown_class(self):
        self.driver.quit()
