# 姓名：郭宏亮
# 时间：2023/8/11 23:34
import jsonpath as jsonpath
import requests as requests

# chromedriver启动9515端口
url = "http://127.0.0.1:9515/session"
data = {
    "capabilities": {
        "browserName": "chrome"
    }
}
response = requests.post(url=url, json=data)
print(response.json())
session_id = jsonpath.jsonpath(response.json(), "$..sessionId")[0]
print(session_id)

# 打开指定的网站
navigate_to = f"{url}/{session_id}/url"
data = {
    "url": "http://novel.hctestedu.com"
}
response = requests.post(navigate_to, json=data)
print(response.json())

# 元素定位到登录
element = f"{url}/{session_id}/element"
data = {
    "using": "xpath",
    "value": "//a[text()='登录']"
}
response = requests.post(url=element, json=data)
# print(response.json())
element_id = jsonpath.jsonpath(response.json(), "$..element-6066-11e4-a52e-4f735466cecf")[0]
print(element_id)

# 点击元素
click = f"{url}/{session_id}/element/{element_id}/click"
data = {}
response = requests.post(url=click, json=data)
print(response.json())

# 关闭sessionid
delete = f"{url}/{session_id}"
response = requests.delete(url=delete)
