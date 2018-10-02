from selenium.common.exceptions import NoSuchElementException

import re

class Passenger():
	def __init__(self):
		"""设置用户名和密码"""
		self.username = '用户名'
		self.password = '密码'
		
		"""是否是单程"""
		self.isSingle = True
		
		"""出发地与目的地"""
		self.fromStation = '武汉'
		self.toStation = '北京'
		
		"""出发日与返程日"""
		self.train_date = "2018-10-10"
		self.back = "2018-04-16"
		self.checis = ['K968', 'Z78', 'K434']

class TrainInfo():
	"""火车信息"""
	def __init__(self, driver, tbodyXpath, trId):
		
		baseXpath = tbodyXpath + '/tr[' + str(trId) + ']'
		#print(baseXpath)
		
		#获取车次
		self.checi = driver.find_element_by_xpath(baseXpath+'/td[1]/div/div[1]/div/a').get_attribute('innerHTML')
		#获取出发站
		self.cdz = driver.find_element_by_xpath(baseXpath+'/td[1]/div/div[2]/strong[1]').get_attribute('innerHTML')
		#获取到达站
		self.cds = driver.find_element_by_xpath(baseXpath+'/td[1]/div/div[2]/strong[2]').get_attribute('innerHTML')
		#获取出发时间
		self.start_t = driver.find_element_by_xpath(baseXpath+'/td[1]/div/div[3]/strong[1]').get_attribute('innerHTML')
		#获取到达时间
		self.color999 = driver.find_element_by_xpath(baseXpath+'/td[1]/div/div[3]/strong[2]').get_attribute('innerHTML')
		#获取历时
		self.ls = driver.find_element_by_xpath(baseXpath+'/td[1]/div/div[4]/strong').get_attribute('innerHTML')
		
		
		self.seat = []
		self.hasTicket = False
		for i in range(2, 13):
			print(i)
			tmpXpath = baseXpath+'/td[' + str(i) + ']'
			print(tmpXpath)
			try:
				num = driver.find_element_by_xpath(tmpXpath).get_attribute('innerHTML')
				#print(num, self.hasTicket, '\n')
				"""去除'<div></div>'"""
				if (num.startswith('<div>')):				
					num = num.lstrip('<div>')
					num = num.rstrip('</div>')
				
				if (self.judge(num)):
					#有票
					self.hasTicket = True
				#print('end:',self.hasTicket, '\n')
			except NoSuchElementException:
				#error
				num = '0'
			self.seat.append(num)
		
		
		#获取预订按钮
		try:
			self.ydbtn = driver.find_element_by_xpath(baseXpath + '/td[13]/a')
		except NoSuchElementException:
			self.ydbtn = None
			#print(trId, ' is none')
			
	def judge(self, string):
		"""判断string是否为‘有’或非0数字"""
		pattern = re.compile('[1-9]+')
		match1 = pattern.findall(string)
		match2 = re.match('有', string)
		if (match1 or match2):
			#为非0数字或‘有’
			return True
		else:
			return False

	def printInfo(self):
		print('车次', self.checi)
		print('出发站', self.cdz)
		print('到达站', self.cds)
		print('出发时间', self.start_t)
		print('到达时间', self.color999)
		print('历时', self.ls) 
		print(self.seat)
		print('是否有票：', self.hasTicket)
	
	
	
	
	
	
	
	
