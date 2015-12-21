# -*- coding:utf-8 -*-
from _elementtree import Element
__author__ = 'lina'

import re
import sys
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from public import BasePage


class Actionkeywords(BasePage.Action):
	"""定义关键字方法"""

	def openBrowser(self):
		"""打开浏览器方法"""
		self.driver = webdriver.Firefox()
		# self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()
		self.accept_next_alert = True
		

	def navigate(self, url):
		"""
		跳转URL地址
		"""
		self.driver.get(url)
	
	def get_currentUrl(self):
		"""获取当前URL"""
		self.driver.current_url
	
			
	def closeBrowser(self):
		"""关闭浏览器"""
		self.driver.quit()

	# 调用send_keys
	def input_Text(self, loc, text):
		"""文本框输入内容"""
		print (loc, text)
		self.send_keys(loc, text)
	#
	def Submit(self, submit_loc):
		"""提交表单"""
		# self.saveScreenshot("submit")
		time.sleep(5)
		self.save_img("submit")
		self.find_element(*submit_loc).click()
		

	def clickButton(self, button_loc):
		"""点击按钮"""
		#print(self.find_element(*button_loc))
		self.find_element(*button_loc).click()
	
	def save_pic(self, name):
		"""保存切图"""
		self.saveScreenshot(name)
		
		
	def wait_for_sec(self):
		"""等待N秒"""
		time.sleep(5)
		
	def key_tab(self):
		# 模拟tab键的输入
		ActionChains(self.driver).key_down(Keys.TAB).perform()
	def get_text(self,*element_loc):
		
		self.find_element(*element_loc).text
		 
	def move_to_element(self):
		# 定位悬浮元素
		#loc1 = self.driver.find_element(element_loc1)
		
		loc1 = self.driver.find_element_by_xpath("//*[@id='navigation']/div/div[1]/div[2]/ul/li[1]/a")
		time.sleep(3)
		ActionChains(self.driver).move_to_element(loc1).perform() 
		time.sleep(3)
		print("定位全部商品")
# 		loc2 = self.driver.find_element(element_loc2)
# 		ActionChains(self.driver).double_click(loc2).click()    
# 		self.clickButton(element_loc2).click() 
# 		print("定位首饰") 
# 		time.sleep(3)    		 
	
	def add_shoppingcart(self,element1,element2,element3,element4,element5,element6,element7):
		"""点击某一商品跳转到商品详情，并加入购物车结算"""
		now_window=self.driver.current_window_handle
		self.clickButton(element1)
		time.sleep(4)
		all_handles = self.driver.window_handles
		for handle in all_handles:
		    if handle != now_window:
		        self.driver.switch_to.window(handle)
		        #driver.switch_to_window(handle)
		        self.clickButton(element2)
		        self.clickButton(element3)
		        time.sleep(3)
		        self.clickButton(element4)
		        self.clickButton(element5)
		        self.driver.close()
		        time.sleep(3) 
		#self.switch_to.window(now_window)
		self.driver.switch_to.window(now_window)
		time.sleep(3)
		self.clickButton(element6)
		time.sleep(3)
		self.driver.refresh()
		time.sleep(3)
		assert "立即支付"  in self.get_text(element7)     
		
	def error_message(self, *element_loc):
		# 获取错误信息
		return self.find_element(*element_loc).text.strip()
	
	def register_alert(self):
		'''处理弹出框中的信息'''
		text = "注册成功"
		assert  text in self.close_alert_and_get_its_text()
	
	def active_alert(self):
		'''处理弹出框中的信息'''
		text = "激活成功"
		assert  text in self.close_alert_and_get_its_text()
	
	def add_shoppingcart_alert(self):
		'''处理弹出框中的信息'''
		text = "购物车加入成功"
		assert  text in self.close_alert_and_get_its_text()
	
	def verify_order_Url(self):
		"""验提交订单成功"""
		text = "/orderManage/tempOrderProductController/"
		self.save_img("create_order_success")
		time.sleep(3)
		assert text in self.get_currentUrl()	
	
			
	def verifyUrl(self, text):
		"""验证注册成功"""
		text = "shoppingCart/quickLoginController/turnLogin.html"
		self.save_img("register_success")
		time.sleep(3)
		assert text in self.get_currentUrl()	
		
	def verify_LoginUrl(self, *submit_loc):
		"""验证登录成功"""
		text = "欢迎您"
		assert text in self.find_element(*submit_loc).text
		
	def verify_add_cart_Url(self):
		""""验证添加购物车是否成功"""
		text = "estore-portal/category"
		print(self.get_currentUrl())
		self.save_img("add_cart_success")
		assert text in self.get_currentUrl()	
		
	def close_alert_and_get_its_text(self):
		'''处理弹出框'''
		try:
			alert = self.driver.switch_to_alert()
			alert_text = alert.text
			print("Alert text:" + alert.text)
			if self.accept_next_alert:	
				# self.save_img("alert_msg")
				alert.accept()
			else:
			    alert.dismiss()
			return alert_text
		finally: self.accept_next_alert = True
		
		
	def find_frame(self):
		"""定位邮件主窗口"""
		self.driver.switch_to_frame("mainFrame")
		# print("switch_frame:%s:" % self.driver.switch_to_frame("mainFrame"))
		
	# 使用正则获取邮箱中的超链接
	def get_re(self):
	    active_url = '<a .*?href="(.*?)".*?>'
	    return active_url
	# 拼接url   
	def content_append(self, content_text, activeuser, activeurl):
	    content_text.append(activeuser)
	    content_text.append(activeurl)
	# 把URL存放到列表中
	def get_content_from_editEmail(self, grep):
	    active_url = self.get_re()
	    content_text = []
	    activeuser = "".join(re.findall(active_url, grep)[0])
	    activeurl = "".join(re.findall(active_url, grep)[1])
	    print("激活账户:%s" % activeuser)
	    self.content_append(content_text, activeuser, activeurl)
	    return content_text
	def mailContent(self):
		time.sleep(3)
		content = self.driver.find_element_by_xpath("//*[@id='mailContentContainer']/div/div[1]/div[2]").get_attribute("innerHTML")
		print("content---%s" % content)
		return content
	# 获取到邮箱html中URL的超链接
	def get_content_from_email(self):
		"""获取邮件内容"""
		grep = self.mailContent()
		time.sleep(3)
		print("grep:%s" % grep)
		content = self.get_content_from_editEmail(grep)
		print("content:%s" % content)
		return content
	
	def get_active_with_url(self):
	    """点击邮件中的超链接"""
	    context_text = self.get_content_from_email()
	    print(context_text)
	    active_url = context_text[1]
	    print(active_url)
	    self.driver.get(active_url) 
	    time.sleep(3)  
	    
    # 链接数据库
	def mysqlQuery(self, host, user, pwd, testdb, sql):
		'''查询/修改数据'''
		import pymysql
		conn = pymysql.connect(host=host, user=user, passwd=pwd, db=testdb, charset='utf8')
		cur = conn.cursor(sql)
		# 执行SQL
		cur.execute(sql)
		conn.commit()
		cur.close()
		conn.close()
		  	
	def clickElement_i(self, index, *element_loc):
		"""点击元素"""
		# print self.find_elements_i(i, *element_loc)
		self.find_elements_i(*element_loc, index=index).click()
	
	def verifyLogin(self, span_loc, userid_loc):
		"""登录校验"""
		spanTF = True
		try:
			# 通过捕获异常，判断是否显示的出了Tip文本，显示为 True 否则为False
			self.find_element(*span_loc).text
			spanTF = True
		except:
			spanTF = False
		if spanTF:
			print(self.find_element(*span_loc).text)
		else:
			print(self.driver.title)
			self.checkTrue(self.driver.find_element(*userid_loc).text, u"登录失败")
