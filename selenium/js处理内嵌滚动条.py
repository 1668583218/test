import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('03.html')
driver.get(file_path)
# 横向底部
js1 = 'document.getElementById("yoyoketang").scrollTop=10000'
driver.execute_script(js1)
time.sleep(5)
# 横向底部
js2 = 'document.getElementById("yoyoketang").scrollTop=0'
driver.execute_script(js2)
time.sleep(5)
# 纵向右部
js3 = 'document.getElementById("yoyoketang").scrollLeft=10000'
driver.execute_script(js3)
time.sleep(5)
# 纵向左部
js4 = 'document.getElementById("yoyoketang").scrollLeft=0'
driver.execute_script(js4)
time.sleep(5)
driver.quit()