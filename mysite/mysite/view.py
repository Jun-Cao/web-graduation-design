from django.http import HttpResponse
from django.shortcuts import render
import os

from . import recognize
from . import build

import shutil 	#高级文件管理

def index(request):
	context = {}
	return render(request, 'index.html', context)

def postImg(request):
	imgPath = os.path.dirname(__file__) + "\..\static\save"

	#清空存储识别图片的文件夹
	shutil.rmtree(imgPath)
	os.mkdir(imgPath)

	if request.method == "POST":
		# myFile = request.FILES.get("img", None)

		myFiles = request.FILES.getlist('img')
		if myFiles == []:
			context = {
				'res': ["上传文件为空"]
			}
			return render(request, 'showResult.html', context)
		for myFile in myFiles:
			
			destination = open(os.path.join(imgPath, myFile.name), 'wb+')

			for chunk in myFile.chunks():
				destination.write(chunk) 
			destination.close()
			# chunk = myFile.read()
			# destination.write(chunk)
			# destination.close()
		res = recognize.recognition()		

		if len(res[0]) == len(res[1]):
			arr = []
			for i in range(len(res[0])):
				data = [res[0][i], res[1][i]]
				arr.append(data)
			context = {
				'arr': arr
			}
			print(context)
			return render(request, 'showRecon.html', context)
		else:
			context = {
				'res': ["识别错误"]
			}
			return render(request, 'showResult.html', context)


def train(request):
	if request.POST:
		times = request.POST['trainTimes']	#训练次数
		boolean, html = build.main(times)
		context = {
			'res': html
		}
		if boolean:
			return render(request, 'showResult.html', context)



