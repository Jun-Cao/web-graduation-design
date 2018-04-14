# -*- coding:utf-8 -*-      
import cv2    
import tensorflow as tf    
import numpy as np 
from skimage import io,transform  
from sys import path

import os
import glob   

#读取图片及其标签函数
def read_image(path):
    images = []

    toReconArr = []
    toShowArr = []
    for item in os.listdir(path):
        toRecon = path + item
        toReconArr.append(toRecon)
        toShow = "../static/save/" + item
        toShowArr.append(toShow)

    for img in toReconArr:
        image = io.imread(img)
        image = transform.resize(image,(32,32,1))
        image = np.reshape(image , [-1,32,32,1])
        images.append(image)

    return np.asarray(images,dtype=np.float32), toShowArr

def recognition():    
    sess = tf.InteractiveSession()    
    #模型恢复  
    saver=tf.train.import_meta_graph(os.path.dirname(__file__) + "/model_data/model.meta")  
   
    saver.restore(sess, os.path.dirname(__file__) + "/model_data/model") 
    graph = tf.get_default_graph()  
      
    # 获取输入tensor,,获取输出tensor  
    x = sess.graph.get_tensor_by_name("x:0")  
    y_ = sess.graph.get_tensor_by_name("y_:0")  
    results = sess.graph.get_tensor_by_name("results:0") 
  

    path = os.path.dirname(__file__) + "/../static/save/"
    switch = {
        '[0]': '0',
        '[1]': '1',
        '[2]': '2',
        '[3]': '3',
        '[4]': '4',
        '[5]': '5',
        '[6]': '6',
        '[7]': '7',
        '[8]': '8',
        '[9]': 'A',
        '[10]': 'B',
        '[11]': 'C',
        '[12]': 'D',
        '[13]': 'E',
        '[14]': 'F',
        '[15]': 'G',
        '[16]': 'H',
        '[17]': 'P',
        '[18]': 'S',
        '[19]': 'T',
        '[21]': 'Y',
    }

    showArr = [] #存储路径的数组
    resArr = [] #存储结果的数组

    dataArr, showArr = read_image(path)
    for data in dataArr:    #将结果添加到数组
        res = sess.run(results, feed_dict={x:data,y_:[]})
        res = str(res)
        resArr.append(switch[res])


    both = [showArr, resArr]
    print('识别结果为：', both)
    #关闭会话    
    sess.close()
    return both
