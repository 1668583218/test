# coding=utf-8
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps = {
    # 需要连接的手机的平台(不限制大小写)
    'platformName': 'Android',
    # 需要连接的手机的设备号(andoird平台下，可以随便写，但是不能不写)
    'deviceName': 'emulator-5554',
    # 需要连接的手机的版本号(比如 5.2.1 的版本可以填写 5.2.1 或 5.2 或 5 ，以此类推)
    'platformVersion': '7.1.2',
    # 需要启动的程序的包名
    'appPackage': 'com.tencent.mm',
    # 需要启动的程序的界面名
    'appActivity': '.ui.LauncherUI',
    # 设置可以输入中文
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    # 设置不用再重置（不然微信、qq每次都要重新登录）
    "noReset": True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
# driver.find_element(By.XPATH, '//android.widget.Button[contains(@text, "登录")]').click()
# driver.find_element(By.XPATH, '//android.widget.Button[contains(@text, "用微信号/QQ号/邮箱登录")]').click()
# driver.find_element(By.XPATH, '//android.widget.EditText[contains(@text, "请填写微信号/QQ号/邮箱")]').send_keys('')
driver.find_element(By.XPATH, '//android.view.View[contains(@text, "大号")]').click()
driver.find_element(By.XPATH, '//*[contains(@content-desc, "聊天信息")]').click()
driver.find_element(By.XPATH, '//*[contains(@resource-id, "com.tencent.mm:id/h8t")]').click()
driver.find_element(By.XPATH, '//android.widget.TextView[contains(@text, "朋友圈")]').click()
# 获取 FrameLayout
items = driver.find_elements(By.ID, 'com.tencent.mm:id/be9')
# 滑动
driver.swipe(300, 800, 300, 300, 2000)
# 遍历获取
for item in items:
    # text值为空，也没有value，所以gg
    # moment_text = item.find_element(By.ID, 'com.tencent.mm:id/bmr').get_attribute('text')
    # day_text = item.find_element_by_id('com.tencent.mm:id/hxj').text
    # month_text = item.find_element_by_id('com.tencent.mm:id/hyx').text
    # print('抓取到朋友圈数据： %s' % moment_text)
    # print('抓取到发布时间： %s%s' % (month_text, day_text))
    print('没有文字')
sleep(5)
driver.quit()
