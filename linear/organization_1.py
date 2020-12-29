# -*- coding: utf-8 -*-
# @Time : 2020/12/28 15:50
# @Author : nichao
# @Email : 530504026@qq.com
# @File : organization_1.py
# @Project : crm2
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://192.168.1.213/crm')
username_locator = (By.NAME, "name")
password_locator = (By.NAME, 'password')
submit_locator = (By.NAME, 'submit')
socialavatar_locator = (By.CSS_SELECTOR, '/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/a/img')
origanization_locator = (By.LINK_TEXT, '组织架构')  # 组织架构的定位器
"""添加部门相关定位器"""
adddepartment_locator = (By.ID, 'add_department')  # 添加部门的定位器
departmentname_locator = (By.ID, 'name')  # 岗位名称定位器
uperiordepartment_locator = (By.NAME, 'parent_id')  # 上级部门的选择定位器
departmentnamedescription_locator = (By.CSS_SELECTOR, '#department_add > div:nth-child(3) > div > textarea')  # 部门描述定位器
confirm_locator = (By.XPATH, '/html/body/div[8]/div[3]/div/button[1]/span')  # 确定按钮
"""添加岗位定位器"""
addrole_locator = (By.ID, 'add_role')  # 添加岗位定位器
rolename_locator = (By.NAME, 'name')  # 部门名称定位器
fordepartment_locator = (By.NAME, 'department_id')  # 所属部门定位器
parent_locator = (By.NAME, 'parent_id')  # 上级部门定位器
roledescription_locator = (By.CSS_SELECTOR, '#role_add > div:nth-child(4) > div > textarea')  # 部门描述定位器
roleconfirm_locator = (By.XPATH, '/html/body/div[9]/div[3]/div/button[1]/span')  # 添加岗位确定按钮定位器
""""添加员工定位器"""
adduser_locator=(By.XPATH,'//*[@id="user_form"]/div[1]/div/a[3]')#添加员工定位器
addusername_locator=(By.ID,'name')#添加员工用户名定位器
userpassword_locator=(By.ID,'password')#添加员工密码定位器
categoryid_locator=(By.XPATH,'//*[@id="add"]/table/tbody/tr[3]/td[2]/select')#用户类别
userdepartment_locator=(By.ID,'department2')#所属部门
rolename2_locator=(By.ID,'role2')#员工岗位名称
savebotton_locator=(By.CSS_SELECTOR,"[value='添加']")#添加按钮

driver.find_element(*username_locator).send_keys("admin")
driver.find_element(*password_locator).send_keys('123456')
driver.find_element(*submit_locator).click()
sleep(3)
driver.find_element_by_css_selector("[class='avatar']").click()  # 点击头像
sleep(3)
driver.find_element(*origanization_locator).click()  # 点击组织架构
sleep(3)
"""添加部门"""
driver.find_element(*adddepartment_locator).click()  # 点击添加部门
sleep(3)
driver.find_element(*departmentname_locator).send_keys('人事部')  # 输入部门名称
sleep(2)
locatot = driver.find_element(*uperiordepartment_locator)
select = Select(locatot)
select.select_by_visible_text('--卡卡罗特分公司（深圳）')
sleep(3)
driver.find_element(*departmentnamedescription_locator).send_keys('负责人事方面工作')
sleep(2)
driver.find_element(*confirm_locator).click()#点击确定按钮
""""添加岗位"""
sleep(3)
driver.find_element(*addrole_locator).click()  # 点击添加岗位
sleep(3)
driver.find_element(*rolename_locator).send_keys('测试工程师组长')  # 添加岗位名称
sleep(3)
locator_element = Select(driver.find_element(*fordepartment_locator)).select_by_visible_text('----技术研发部')  # 选择所属部门
sleep(3)
parent_element = Select(driver.find_element(*parent_locator)).select_by_visible_text(' --  -- 技术研发部 | 高级工程师')  # 选择上级岗位
sleep(3)
driver.find_element(*roledescription_locator).send_keys('负责软件质量')  # 填写岗位描述
sleep(3)
driver.find_element(*roleconfirm_locator).click()  # 点击添加岗位确定按钮
sleep(3)
"""查看和编辑员工信息"""
wuser_locator=(By.CSS_SELECTOR,'#tab1 > table > thead > tr > td > p > a:nth-child(3)')#查看中的编辑定位器
wemail_locator=(By.NAME,'email')#邮箱的定位器
wphone_locator=(By.NAME,'telephone')#电话的定位器
wuserconfirm_locator=(By.CSS_SELECTOR,'body > div.container > div.row > div:nth-child(2) >'
    ' form > table > tfoot > tr > td:nth-child(2) > input.btn.btn-primary')#编辑员工信息保存按钮
usertable_locator=(By.CSS_SELECTOR,'#user_form > div:nth-child(2) > table > tbody')#用户列表tbody
tr_locator=(By.TAG_NAME,'tr')
td_locator=(By.TAG_NAME,'td')
userdepartment_element=driver.find_element(*usertable_locator)
tr_list=userdepartment_element.find_elements(*tr_locator)
for tr in tr_list:
    td_list=tr.find_elements(*td_locator)
    print(td_list[1].text)
    if td_list[1].text.strip()=="小杨":
        print(td_list[1].text)
        sleep(1)
        td_list[7].find_elements_by_tag_name('a')[0].click()
        sleep(4)
        driver.find_element(*wuser_locator).click()
        sleep(1)
        driver.find_element(*wemail_locator).clear()
        driver.find_element(*wemail_locator).send_keys('1234567@qq.com')
        sleep(1)
        driver.find_element(*wphone_locator).clear()
        driver.find_element(*wphone_locator).send_keys('18782968888')
        sleep(1)
        driver.find_element(*wuserconfirm_locator).click()
        sleep(1)
        break




