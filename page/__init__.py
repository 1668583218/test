from selenium.webdriver.common.by import By
"""项目配置地址"""
url = "https://wbtest.okaygis.com/dxb/CQwyy/"


"""以下为登录界面元素配置信息"""
# 用户名
# login_username = By.XPATH, "//*[@id='app']/div/form/div[2]/div[2]/div/div/input"
login_username = By.XPATH, "//input[contains(@placeholder, '请输入用户名')]"
# 密码
# login_pwd = By.XPATH, "//*[@id='app']/div/form/div[3]/div[2]/div/div/input"
login_pwd = By.XPATH, "//input[contains(@placeholder, '请输入密码')]"
# 验证码
# login_ver = By.XPATH, "//*[@id='app']/div/form/div[5]/div/div/div[1]/div/input"
# 登录按钮
# login_btn = By.XPATH, "//*[@id='app']/div/form/button"
login_btn = By.XPATH, "//span[contains(text(), '登录')]"
"""以下为首页界面元素配置信息"""
# 古建规划保护管理
# gjgh = By.XPATH, "//*[@id='app']/div/div[2]/div/ul/li[2]/div/span"
gjgh = By.XPATH, "//span[text()='古建规划保护管理']"
"""以下为古建规划保护管理元素配置信息"""
# 勘察修缮管理
# gjgh_kcxs = By.XPATH, "//*[@id='app']/div/div[2]/div/ul/li[2]/ul/li[1]/span"
gjgh_kcxs = By.XPATH, "//span[contains(text(), '勘察修缮管理')]"
# 保护规划管理
gjgh_bhgh = By.XPATH, "//span[contains(text(), '保护规划管理')]"
# 专题调查管理
gjgh_ztdc = By.XPATH, "//span[contains(text(), '专题调查管理')]"
# 文物工程监理
gjgh_wwgc = By.XPATH, "//span[contains(text(), '文物工程监理')]"

"""以下为列表界面元素配置信息"""
# 新增按钮
# add_btn = By.XPATH, "//*[@id='app']/div/div[3]/div[2]/div/div/div[2]/button[1]"
add_btn = By.XPATH, "//span[text()='新增']"
# 搜索按钮
# search_btn = By.XPATH, "//*[@id='app']/div/div[3]/div[2]/div/div/div[1]/form/div[7]/div/button[1]"
search_btn = By.XPATH, "//span[text()='搜索']"
# 重置按钮
# reset_btn = By.XPATH, "//*[@id='app']/div/div[3]/div[2]/div/div/div[1]/form/div[7]/div/button[2]"
reset_btn = By.XPATH, "//span[text()='重置']"
# 展开按钮
# unfold_btn = By.XPATH, "//*[@id='app']/div/div[3]/div[2]/div/div/div[1]/form/div[3]/div/button[3]"
unfold_btn = By.XPATH, "//span[contains(text(), '展开')]"
# 收起按钮
# pack_up_btn = By.XPATH, "//*[@id='app']/div/div[3]/div[2]/div/div/div[1]/form/div[7]/div/button[3]"
pack_up_btn = By.XPATH, "//span[contains(text(), '收起')]"
# 清单界面编号输入框
# list_project_nub = By.XPATH, "//*[@id='app']/div/div[3]/div[2]/div/div/div[1]/form/div[1]/div/div/input"
list_project_nub = By.XPATH, "//label[contains(text(), '项目编号')]/following-sibling::div[1]/div/input"
# 清单界面名称输入框
# list_project_name = By.XPATH, "//*[@id='app']/div/div[3]/div[2]/div/div/div[1]/form/div[2]/div/div/input"
list_project_name = By.XPATH, "//label[contains(text(), '项目名称')]/following-sibling::div[1]/div/input"
# 清单界面委托单位输入框
# list_entrusting_party = By.XPATH, "//*[@id='app']/div/div[3]/div[2]/div/div/div[1]/form/div[3]/div/div/input"
list_entrusting_party = By.XPATH, "//label[contains(text(), '委托单位')]/following-sibling::div[1]/div/input"
# 清单界面合作单位输入框
# list_cooperator_party = By.XPATH, "//*[@id='app']/div/div[3]/div[2]/div/div/div[1]/form/div[4]/div/div/input"
list_cooperator_party = By.XPATH, "//label[contains(text(), '委托单位')]/following-sibling::div[1]/div/input"
# 清单界面地点输入框
list_site = By.XPATH, "//label[contains(text(), '地点')]/following-sibling::div[1]/div/input"
# 第一个编辑按钮
# first_edit_btn = By.XPATH, "//*[@id='app']/div/div[3]/div[2]/div/div/div[3]/div/div[4]/div[2]/table/tbody/tr/td[8]/div/button"
first_edit_btn = By.XPATH, "//div[2]/table/tbody/tr[1]/td[8]/div/button"
# 全选按钮
check_all_btn = By.XPATH, "//*[@id='app']/div/div[3]/div[2]/div/div/div[3]/div/div[2]/table/thead/tr/th[1]/div/label/span/span"
"""以下为新增界面元素配置信息"""
# 删除按钮
delete_btn = By.XPATH, "//span[text()='删除']"
# 取消按钮
cancel_btn = By.XPATH, "//span[contains(text(), '取消')]"
# 项目编号
# project_nub = By.XPATH, "//*[@id='app']/div/div[3]/div[2]/div/div/div/form/div[1]/div[1]/div/div/div/input"
project_nub = By.XPATH, "//input[contains(@placeholder, '请输入项目编号')]"
# 项目名称
# project_name = By.XPATH, "//*[@id='app']/div/div[3]/div[2]/div/div/div/form/div[1]/div[2]/div/div/div/input"
project_name = By.XPATH, "//input[contains(@placeholder, '请输入项目名称')]"
# 委托单位
# entrusting_party = By.XPATH, "//*[@id='app']/div/div[3]/div[2]/div/div/div/form/div[1]/div[3]/div/div/div/input"
entrusting_party = By.XPATH, "//input[contains(@placeholder, '请输入委托单位')]"
# 合作单位
# cooperator_party = By.XPATH, "//*[@id='app']/div/div[3]/div[2]/div/div/div/form/div[1]/div[4]/div/div/div/input"
cooperator_party = By.XPATH, "//input[contains(@placeholder, '请输入合作单位')]"
# 项目负责人
project_leader = By.XPATH, "//input[contains(@placeholder, '请输入项目负责人')]"
# 地点
site = By.XPATH, "//input[contains(@placeholder, '请输入地点')]"
# 开始时间
# start_time = By.XPATH, "//*[@id='app']/div/div[3]/div[2]/div/div/div/form/div[1]/div[5]/div/div/div/input"
start_time = By.XPATH, "//input[contains(@placeholder, '请输入项目开始时间')]"
# 结束时间
# end_time = By.XPATH, "//*[@id='app']/div/div[3]/div[2]/div/div/div/form/div[1]/div[6]/div/div/div/input"
end_time = By.XPATH, "//input[contains(@placeholder, '请输入项目结束时间')]"
# 保存按钮
# save_btn = By.XPATH, "//*[@id='app']/div/div[3]/div[2]/div/div/div/form/div[4]/button/span"
save_btn = By.XPATH, "//span[contains(text(), '保存')]"
# 异常信息
err_info = By.XPATH, "/html/body/div[2]/p"
# 成功信息
success_info = By.XPATH, "/html/body/div[3]/p"
# xx管理-链接
xxgl_link = By.XPATH, "//div[1]/div[2]/span[2]/span"
