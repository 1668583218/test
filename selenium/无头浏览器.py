# -*-coding=utf-8
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 设置谷歌对象
chrome_options = webdriver.ChromeOptions()
# 方法一
# chrome_options.set_headless()
# 方法二
# chrome_options.headless=False
# 方法三
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=chrome_options)
file_path = 'file:///' + os.path.abspath('02.html')
driver.get(file_path)
time.sleep(2)
# 先定位到下拉框
m = driver.find_element(By.ID, "ShippingMethod")  # 再点击下拉框下的选项
m.find_element(By.XPATH, "//option[@value='10.69']").click()
driver.get_screenshot_as_file('01.png')
time.sleep(3)
driver.quit()
