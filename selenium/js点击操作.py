import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://prodplus.okaygis.com:8880/#/login")
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[3]/div/div/input').send_keys('shuirr')
driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[4]/div/div/input').send_keys('ok111111')
driver.find_element(By.XPATH, '//*[@id="app"]/div/form/button').click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[text()='藏品管理']").click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/ul/div/li[3]/span').click()
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div/div[4]/div/div[2]/table/thead/tr/th[1]/div/label/span').click()
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div/div[3]/button[1]').click()
driver.find_element(By.XPATH, '(//input[@placeholder="请选择"])[2]').click()
driver.find_element(By.XPATH, '(//li[@class="el-cascader-node is-selectable"])[1]').click()
driver.find_element(By.XPATH, '(//label[@role="radio"])[1]').click()
# js = 'document.getElementsByClassName("el-radio")[1].click()'
# driver.execute_script(js)
time.sleep(10)
driver.quit()
