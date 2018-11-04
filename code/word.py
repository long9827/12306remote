from aip import AipOcr
from PIL import Image

""" 你的 APPID AK SK """
APP_ID = '14380088'
API_KEY = 'Zi9FxqGL5kUw0d2IeQ98XxVb'
SECRET_KEY = 'Ud5qEiqawZf15qez8SLK6lAEqDrFZ8r1'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

for i in range(1, 11):
	filePath = str(i) + '.jpg'
	Image.open(filePath).crop((117, 0, 212, 30)).save('sub/'+str(i)+'.jpg', 'jpeg')
	image = get_file_content('sub/'+str(i)+'.jpg')

	""" 调用通用文字识别（高精度版） """
	print(client.basicAccurate(image))
