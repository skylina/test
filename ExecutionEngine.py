#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Created on 2015年11月25日
Function:执行所有测试用例并且发送测试报告
@author: lina
To me :Believe yourself!
'''

from selenium import webdriver
import unittest
import time
import sys
from public import BasePage
from config import actionKeyword
from test import test_support

class ExecutionEngin(unittest.TestCase):
	"""脚本的入口引擎"""
	# 脚本初始化
	@classmethod
	def setUpClass(cls):
		# cls.driver = webdriver.Firefox()
		# cls.driver.implicitly_wait(30)
		cls.filepath = "dataEngine\\data.xls"

	# 测试用例
	def action(self, *txt):
		"""
		测试Demo
		"""
		exeKeyword = actionKeyword.Actionkeywords()
		base = BasePage.Action()
		
		case_id = txt[1]
		username = txt[4]
		password = txt[5]
		summary = txt[3]
		print("summary:%s" % summary)
		print("[" + summary + "]")
		# casedata = base.getTabledata(self.filepath, "Test Cases")
		
		k = 4
		stepdata = base.getTabledata(self.filepath, "Test Steps")
		for j in stepdata:
			if txt[0] == j[0]:
				# print j[3]
				if j[3] == "openBrowser":
					print (j[2])
					exeKeyword.openBrowser()
				elif j[3] == "InInput":
					print (j[2])
					loc = base.locate(j[4])
					exeKeyword.input_Text(loc, txt[k])
					k += 1
				elif j[3] == "click":
					print (j[2])
					loc = base.locate(j[4])
					exeKeyword.clickButton(loc)
				elif j[3] == "verifyLogin":
					print (j[2])
					loc_1 = base.locate(j[4])
					loc_2 = base.locate(j[5])
					exeKeyword.verifyLogin(loc_1, loc_2)
				elif j[3] == "verifyRegister":
					print (j[2])
					exeKeyword.verifyUrl()
				elif j[3] == "sleep":
					print (j[2])
					# loc_4 = base.locate(j[4])
					exeKeyword.wait_for_sec()
				elif j[3] == "submit":
					print (j[2])
					loc = base.locate(j[4])
					exeKeyword.Submit(loc)
				elif j[3] == "tab":
					print (j[2])
					exeKeyword.key_tab()
				elif j[3] == "register_alert":
					print (j[2])					
					exeKeyword.register_alert()
				elif j[3] == "email_alert":
					print (j[2])					
					exeKeyword.active_alert()
				elif j[3] == "add_shop_alert":
					print (j[2])		
					exeKeyword.add_shoppingcart_alert()
				elif j[3] == "submit_order":
					print (j[2])					
					loc1 = base.locate(j[4])
					loc2 = base.locate(j[5])
					loc3 = base.locate(j[6])
					loc4 = base.locate(j[7])
					loc5 = base.locate(j[8])
					loc6 = base.locate(j[9])
					loc7 = base.locate(j[10])
					exeKeyword.add_shoppingcart(loc1,loc2,loc3,loc4,loc5,loc6,loc7)
				elif j[3] == "savepic":
					print (j[2])
					loc = base.locate(j[4])
					exeKeyword.save_pic(loc)
				elif j[3] == "switch_frame":
					print (j[2])
					exeKeyword.find_frame()
				elif j[3] == "active_url":
					print (j[2])
					exeKeyword.get_active_with_url()		
				elif j[3] == "move_to_element":
					print (j[2])
					#loc = base.locate(j[4])	
					exeKeyword.move_to_element()	
				elif j[3] == "verifyAddCartUrl":
					print (j[2])
					exeKeyword.verify_add_cart_Url()	
				elif j[3] == "verify_order_url":
					print (j[2])	
					exeKeyword.verify_order_Url()				
				elif j[3] == "verifyLoginUrl":
					print (j[2])
					loc = base.locate(j[4])		
					exeKeyword.verify_LoginUrl(loc)
				elif j[3] == "closeBrowser":
					print (j[2])
					time.sleep(5)
					exeKeyword.closeBrowser()
				elif j[3] == "navigate":
					print (j[2])
					url = j[4]
					exeKeyword.navigate(url)
				elif j[3] == "clickelement":
					print (j[2])
					loc = base.locate(j[4])
					exeKeyword.clickElement_i(2, loc)
	@staticmethod
	def getTestFunc(*txt):
		def func(self):
			self.action(*txt)
		return func

	# 脚本退出
	@classmethod
	def tearDownClass(cls):
		print ("End")
		# cls.driver.quit()

def __generateTestCases():
	login_page = BasePage.Action()
	casedata = login_page.getTabledata("dataEngine\\data.xls", "Test Cases")
	for i in casedata:
		TCid = i[0]
		if i[3] == "Y":
			print ("【Run】" + i[1] + ":")
			print (" + -"*8)
			table = login_page.getTabledata("dataEngine\\data.xls", "case data")
			for txt in table:
				if (txt[2] == "Y") & (txt[0] == TCid):
					print (txt)
					setattr(ExecutionEngin, 'test_%s_%s' % (txt[0], txt[1]), ExecutionEngin.getTestFunc(*txt))
__generateTestCases()

def test_main():
	# test_support.run_unittest(ExecutionEngin)
	test_support.support.run_unittest(ExecutionEngin)

if __name__ == "__main__":
	test_main()