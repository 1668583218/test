# coding=utf-8
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 脚本要与 upload_file.html 同一目录
file_path = 'file:///' + os.path.abspath('01.html')
driver.get(file_path)
# 定位上传按钮，添加本地文件
driver.find_element(By.NAME, "file").send_keys(r'C:/Users/caojingwei/Desktop/计划.txt')
time.sleep(2)
driver.quit()
