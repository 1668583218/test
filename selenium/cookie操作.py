import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.get("http://jira.okaygis.com:10025/login.jsp")
# driver.maximize_window()
# driver.find_element(By.XPATH, '//*[@id="login-form-username"]').send_keys('caojingwei')
# driver.find_element(By.XPATH, '//*[@id="login-form-password"]').send_keys('123456')
# driver.find_element(By.XPATH, '//*[@id="login-form-submit"]').click()
# print(driver.get_cookies())
# c1 = driver.get_cookies()[0]
# c2 = driver.get_cookies()[1]
# driver.quit()
c1 = {
    u'domain': u'jira.okaygis.com',
    u'httpOnly': False,
    u'name': u'atlassian.xsrf.token',
    u'path': u'/',
    u'secure': False,
    u'value': u'B4CV-1XT9-1KKA-BYB1|708418d74a6977d69a641a301494dae1f45d7916|lin'
}
c2 = {
    u'domain': u'jira.okaygis.com',
    u'httpOnly': True,
    u'name': u'JSESSIONID',
    u'path': u'/',
    u'secure': False,
    u'value': u'E8B0A1024CF1B2127C86C7F3CF7B92FF'
}
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://jira.okaygis.com:10025/secure/Dashboard.jspa")
driver.maximize_window()
driver.add_cookie(c1)
driver.add_cookie(c2)
time.sleep(5)
driver.refresh()