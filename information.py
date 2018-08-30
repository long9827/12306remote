from selenium.common.exceptions import NoSuchElementException

class Passenger():
	def __init__(self):
		"""设置用户名和密码"""
		self.username = '17702729698'
		self.password = 'long9827'
		
		"""是否是单程"""
		self.isSingle = True
		
		"""出发地与目的地"""
		self.fromStation = '武汉'
		self.toStation = '北京'
		
		"""出发日与返程日"""
		self.train_date = "2018-09-01"
		self.back = "2018-04-16"

class TrainInfo():
	"""火车信息"""
	def __init__(self, tbody, trId):
		
		baseXpath = '//tr[' + str(trId) + ']'
		#print(baseXpath)
		
		#获取车次
		self.checi = tbody.find_element_by_xpath(baseXpath+'/td[1]/div/div[1]/div/a').get_attribute('innerHTML')
		#获取出发站
		self.cdz = tbody.find_element_by_xpath(baseXpath+'/td[1]/div/div[2]/strong[1]').get_attribute('innerHTML')
		#获取到达站
		self.cds = tbody.find_element_by_xpath(baseXpath+'/td[1]/div/div[2]/strong[2]').get_attribute('innerHTML')
		#获取出发时间
		self.start_t = tbody.find_element_by_xpath(baseXpath+'/td[1]/div/div[3]/strong[1]').get_attribute('innerHTML')
		#获取到达时间
		self.color999 = tbody.find_element_by_xpath(baseXpath+'/td[1]/div/div[3]/strong[2]').get_attribute('innerHTML')
		#获取历时
		self.ls = tbody.find_element_by_xpath(baseXpath+'/td[1]/div/div[4]/strong').get_attribute('innerHTML')
		
		#print(tbody.find_element_by_xpath(baseXpath+'/td[2]').get_attribute('innerHTML'))
		
		#/html/body/div[6]/div[7]/table/tbody/tr[19]/td[2]/div
		
		self.seat = []
		self.hasTicket = False
		for i in range(1, 11):
			try:
				num = tbody.find_element_by_xpath(baseXpath+'/td[2]/div').get_attribute('innerHTML')
				print(num, self.hasTicket, '\n')
				if (num != '无'):
					self.hasTicket = True
				print('end:',self.hasTicket, '\n')
			except NoSuchElementException:
				#空
				num = '0'
			self.seat.append(num)
		
		
		#获取预订按钮
		try:
			self.ydbtn = tbody.find_element_by_xpath(baseXpath + '/td[13]/a')
		except NoSuchElementException:
			self.ydbtn = None
			#print(trId, ' is none')

	def printInfo(self):
		print('车次', self.checi)
		print('出发站', self.cdz)
		print('到达站', self.cds)
		print('出发时间', self.start_t)
		print('到达时间', self.color999)
		print('历时', self.ls) 
		print('有票？', self.hasTicket)
	
	
	
	
	
	
	
	
