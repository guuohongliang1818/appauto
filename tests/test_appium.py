# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

caps = {}
caps["platformName"] = "android"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

el17 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Clock")
el17.click()
el18 = driver.find_element(by=AppiumBy.XPATH,
                           value="//androidx.appcompat.app.ActionBar.Tab[@content-desc='Clock']/android.widget.TextView")
el18.click()
el19 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Cities")
el19.click()

# el20 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ImageButton[@content-desc='Cities']")
# el20.click()

el21 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Search")
el21.click()

el22 = driver.find_element(by=AppiumBy.ID, value="com.android.deskclock:id/search_src_text")
el22.send_keys("Shanghai")

el23 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Shanghai")
el23.click()

el24 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
el24.click()

driver.quit()
