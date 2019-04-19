from aip import AipImageClassify
from aip import AipOcr
from PIL import Image
from selenium.webdriver.common.action_chains import ActionChains

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
       return fp.read()

"""获取子图"""
def get_sub_img(im, x, y):
    assert 0 <= x <= 3
    assert 0 <= y <= 1
    left = 5 + (67 + 5) * x
    top = 41 + (67 + 5) * y
    right = left + 67
    bottom = top + 67
    return im.crop((left, top, right, bottom))

""" 截图，获取验证码并保存 """
def savecode(driver):
	driver.get_screenshot_as_file('CrawlResult/screenshot.png')
	element = driver.find_element_by_xpath('/html/body/div[6]/div/form/div/ul[2]/li[4]/div/div/div[3]/img')
	left = int(element.location['x'])
	top = int(element.location['y'])
	right = int(element.location['x'] + element.size['width'])
	bottom = int(element.location['y'] + element.size['height'])
	
	im = Image.open('CrawlResult/screenshot.png')
	im = im.crop((left, top, right, bottom))
	im.save('CrawlResult/code.png')

""" 利用百度API识别验证码 """
def identifyCode(filePath):
	""" APPID AK SK """
	APP_ID = '14380088'
	API_KEY = 'Zi9FxqGL5kUw0d2IeQ98XxVb'
	SECRET_KEY = 'Ud5qEiqawZf15qez8SLK6lAEqDrFZ8r1'

	client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
	keyclient = AipOcr(APP_ID, API_KEY, SECRET_KEY)
	
	image = Image.open(filePath)
	
	image.crop((117, 0, 212, 30)).save('CrawlResult/sub/key.jpg', 'jpeg')
	key = get_file_content('CrawlResult/sub/key.jpg')
	words_result = keyclient.basicAccurate(key)['words_result']
	keyword = []
	for word_result in words_result:
		keyword.append(word_result['words'])
	
	image_words = []	
	for y in range(0, 2):
		for x in range(0, 4):
			tmpResult = []
			get_sub_img(image, x, y).save('CrawlResult/sub/'+str(x)+str(y)+'.jpg', 'jpeg')
			#print('调用通用物体识别: ', client.advancedGeneral(get_file_content('sub/'+str(x)+str(y)+'.jpg')), '\n')
			tmp = client.advancedGeneral(get_file_content('CrawlResult/sub/'+str(x)+str(y)+'.jpg'))['result']
			for item in tmp:
				#print(item['keyword'])
				tmpResult.append(item['keyword'])
			#print('\n')
			image_words.append(tmpResult)
	
	results = {}
	results['keyword'] = keyword
	results['image_words'] = image_words
	return results
	
"""判断两个字符串是否相同或相似"""
def strEqual(str1, str2):
	lens = len(str1) + len(str2)
	sameNum = 0
	for c in str1:
		if c in str2:
			sameNum = sameNum + 1
	#print(str1, str2, 'sameNum: ', sameNum, 'len: ', lens)
	if 2*sameNum/lens > 0.2:
		return True
	else:
		return False
	
"""判断imagewords和keywords是否有共同元素"""
def arrEqual(imagewords, keywords):
	for keyword in keywords:
		for imageword in imagewords:
			if strEqual(keyword, imageword):
				return True
	return False

"""参数为字典，有两项，分别是keyword、image_words"""
def strmatch(strdict):
	keywords = strdict['keyword']
	image_words = strdict['image_words']
	mIndex = []	#返回结果
	for i in range(0, 8):
		#print(image_words[i])
		if arrEqual(image_words[i], keywords):
			mIndex.append(i)
	return mIndex

'''
strdict = identifyCode('10.jpg')
print(strdict)
print(strmatch(strdict))
'''
def getCode(driver):
	savecode(driver)
	filePath = 'CrawlResult/code.png'
	strdict = identifyCode(filePath)
	print(strdict)
	#print(strmatch(strdict))
	return strmatch(strdict)


def clickCode(index, driver):
	yIndex = index//4
	xIndex = index%4
	xoffset = 38 + xIndex*72
	yoffset = 74 + yIndex*72
	print('x: ', xIndex, 'y: ', yIndex)
	#print('x: ', xoffset, 'y: ', yoffset,'\n')
	codeImage = driver.find_element_by_xpath('/html/body/div[6]/div/form/div/ul[2]/li[4]/div/div/div[3]/img')
	ActionChains(driver).move_to_element_with_offset(codeImage, xoffset, yoffset).click().perform()


def clickCodes(indexs, driver):
	if len(indexs)==0:
		indexs = [0]
	for index in indexs:
		clickCode(index, driver)



