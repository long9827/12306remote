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
		self.train_date = "2018-04-16"
		self.back = "2018-04-16"
