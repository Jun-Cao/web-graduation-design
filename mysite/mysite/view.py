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
	imgPath = "D:\web\web-graduation-design\mysite\mysite\images"

	if request.method == "POST":
		myFile = request.FILES.get("img", None)

		if not myFile:
			return HttpResponse("上传内容为空")
		destination = open(os.path.join(imgPath, myFile.name), 'wb+')

		# for chunk in myFile.chunks():
		# 	destination.write(chunk) 
		# destination.close()
		chunk = myFile.read()
		destination.write(chunk)
		destination.close()

		print('上传成功')

		res = recognize.recognition()

		shutil.rmtree(imgPath)
		os.mkdir(imgPath)
		return HttpResponse("识别结果为：" + str(res))

def train(request):
	if request.POST:
		times = request.POST['trainTimes']	#训练次数
		res = build.main(times)
		# context = {}
		# context['times'] = times
		if res:
			return HttpResponse("训练次数为：" + times + "，训练成功")


