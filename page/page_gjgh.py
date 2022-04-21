import page
from base.base import Base

class PageLogin(Base):
    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    # 输入密码
    def page_input_password(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 输入验证码
    # def page_input_ver(self,ver):
    #     self.base_input(page.login_ver,ver)

    # 点击登录按钮
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    # 点击古建规划保护管理
    def page_click_gjgh(self):
        self.base_click(page.gjgh)

    # 点击勘察修缮管理
    def page_click_gjgh_kcxs(self):
        self.base_click(page.gjgh_kcxs)

    # 点击保护规划管理
    def page_click_gjgh_bhgh(self):
        self.base_click(page.gjgh_bhgh)

    # 点击专题调查管理
    def page_click_gjgh_ztdc(self):
        self.base_click(page.gjgh_ztdc)

    # 点击文物工程监理
    def page_click_gjgh_wwgc(self):
        self.base_click(page.gjgh_wwgc)

    # 点击新增按钮
    def page_click_add_btn(self):
        self.base_click(page.add_btn)

    # 点击搜索按钮
    def page_click_search_btn(self):
        self.base_click(page.search_btn)

    # 点击重置按钮
    def page_click_reset_btn(self):
        self.base_click(page.reset_btn)

    # 点击展开按钮
    def page_click_unfold_btn(self):
        self.base_click(page.unfold_btn)

    # 点击收起按钮
    def page_click_pack_up_btn(self):
        self.base_click(page.pack_up_btn)

    # 列表界面-输入项目编号
    def page_input_list_project_nub(self, nub):
        self.base_input(page.list_project_nub, nub)

    # 列表界面-输入项目名称
    def page_input_list_project_name(self, name):
        self.base_input(page.list_project_name,  name)

    # 列表界面-输入委托单位
    def page_input_list_entrusting_party(self, party1):
        self.base_input(page.list_entrusting_party, party1)

    # 列表界面-输入合作单位
    def page_input_list_cooperator_party(self, party2):
        self.base_input(page.list_cooperator_party, party2)

    # 列表界面-输入地点
    def page_input_list_site(self, site):
        self.base_input(page.list_site, site)

    # 新增界面-输入项目编号
    def page_input_project_nub(self, nub):
        self.base_input(page.project_nub, nub)

    # 新增界面-输入项目名称
    def page_input_project_name(self, name):
        self.base_input(page.project_name,  name)

    # 新增界面-输入委托单位
    def page_input_entrusting_party(self, party1):
        self.base_input(page.entrusting_party, party1)

    # 新增界面-输入合作单位
    def page_input_cooperator_party(self, party2):
        self.base_input(page.cooperator_party, party2)

    # 新增界面-输入负责人
    def page_input_project_leader(self, leader):
        self.base_input(page.project_leader, leader)

    # 新增界面-输入地点
    def page_input_site(self, site):
        self.base_input(page.site, site)

    # 新增界面-点击保存按钮
    def page_click_save_btn(self):
        self.base_click(page.save_btn)

    # 新增界面-获取异常提示信息
    def page_get_error_info(self):
        return self.base_get_text(page.err_info)

    # 新增界面-获取成功提示信息
    def page_get_success_info(self):
        return self.base_get_text(page.success_info)

    # 新增界面-点击xx管理链接
    def page_click_xxgl_link(self):
        self.base_click(page.xxgl_link)

    # 截图
    def page_get_img(self):
        self.base_get_image()

    # 点击第一个编辑按钮
    def page_click_first_edit_btn(self):
        self.base_click(page.first_edit_btn)

    # 点击全选按钮
    def page_click_check_all_btn(self):
        self.base_click(page.check_all_btn)

    # 点击删除按钮
    def page_click_delete_btn(self):
        self.base_click(page.delete_btn)

    # 点击取消按钮
    def page_click_cancel_btn(self):
        self.base_click(page.cancel_btn)

    # 新增-组合业务方法
    def page_list_add(self, nub, name):
        self.page_input_project_nub(nub)
        self.page_input_project_name(name)
        self.page_click_save_btn()

    # 搜索-组合业务方法
    def page_list_search(self, nub, name):
        self.page_input_list_project_nub(nub)
        self.page_input_list_project_name(name)
        self.page_click_search_btn()
        self.page_get_img()
        self.page_click_reset_btn()

    # 编辑-组合业务方法
    def page_list_edit(self, nub):
        self.page_click_first_edit_btn()
        self.page_input_project_nub(nub)
        self.page_click_save_btn()

    # 删除-组合业务方法
    def page_list_delete(self):
        self.page_click_check_all_btn()
        self.page_click_delete_btn()
        self.page_click_cancel_btn()
