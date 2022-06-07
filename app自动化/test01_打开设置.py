# coding=utf-8
# 导模块
from appium import webdriver

desired_caps = {
    # 需要连接的手机的平台(不限制大小写)
    'platformName': 'Android',
    # 需要连接的手机的设备号(andoird平台下，可以随便写，但是不能不写)
    'deviceName': '127.0.0.1:11509',
    # 需要连接的手机的版本号(比如 5.2.1 的版本可以填写 5.2.1 或 5.2 或 5 ，以此类推)
    'platformVersion': '7.1.2',
    # 需要启动的程序的包名
    'appPackage': 'com.android.settings',
    # 需要启动的程序的界面名
    'appActivity': '.Settings',
    # 设置可以输入中文
    'unicodeKeyboard': True,
    'resetKeyboard': True
}
# 连接appium服务器
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 退出
driver.quit()