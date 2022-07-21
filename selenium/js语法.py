from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# js学习

driver = webdriver.Chrome()
# 最大化
driver.maximize_window()
driver.implicitly_wait(10)

# 打开浏览器
driver.get("http://prodplus.okaygis.com:8880/#/login")
password = driver.find_element(By.XPATH, "//label[contains(text(), '密码')]/following-sibling::div/div/input")
# 改变某个属性的值
js = """
var pass = arguments[0];
pass.type = 'text'
pass.value = 123456
return [pass.value]
"""
driver.execute_script(js, password)


driver.get("https://www.baidu.com/")
driver.find_element(By.XPATH, "//*[@id='kw']").send_keys("微博")
sleep(1)
driver.find_element(By.XPATH, "//*[@id='su']").click()
sleep(2)
weibo = driver.find_element(By.XPATH, "//*[@id='1']/div/div[1]/h3/a[1]")
# 删除某个属性
js = """
var weibo = arguments[0];
weibo.removeAttribute('target')
return [weibo.value]
"""
driver.execute_script(js, weibo)
# 拖动滚动条
driver.execute_script("window.scrollTo(0,500)")
weibo.click()