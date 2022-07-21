# -*-coding=utf-8
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('02.html')
driver.get(file_path)
time.sleep(2)
# 先定位到下拉框
m = driver.find_element(By.ID, "ShippingMethod")  # 再点击下拉框下的选项
m.find_element(By.XPATH, "//option[@value='10.69']").click()
time.sleep(3)
driver.quit()
