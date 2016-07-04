#coding=utf-8
import numpy as np
import pickle
import os
import time
import sys
import shutil
import skimage 

caffe_root = '/home/cscl/caffe-master/' 
sys.path.insert(0, caffe_root + 'python')
import caffe

net_file = 'googlenet_deploy.prototxt'
caffe_model = 'models/googlenet_hccr.caffemodel' 
mean_file = 'meanfiles/CASIA1.0_1.1_1.2_mean_112.npy'
unicode_index = np.loadtxt('util/unicode_index.txt', delimiter = ',',dtype = np.int) #7534
net = caffe.Net(net_file,caffe_model,caffe.TEST)


def get_crop_image(imagepath, img_name):	
	img=skimage.io.imread(imagepath + img_name,as_grey=True)
	black_index = np.where(img < 255 )
	min_x = min(black_index[0])
	max_x = max(black_index[0])
	min_y = min(black_index[1])
	max_y = max(black_index[1])
	#print(min_x,max_x,min_y,max_y)
	image = caffe.io.load_image(imagepath+"//"+img_name)
	return image[min_x:max_x, min_y:max_y,:]


def evaluate(imagepath, top_k):
	transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
	transformer.set_transpose('data', (2,0,1))
	transformer.set_raw_scale('data', 255) 

	rightcount=0
	allcount=0

	allimage=os.listdir(imagepath)

	for img_name in allimage:
	   allcount = allcount + 1
	   label_truth = img_name.split('.')[0]


	   print "----------------------"
	   image = get_crop_image(imagepath,img_name)
	   net.blobs['data'].data[...] = transformer.preprocess('data',image)
	   out = net.forward()
	   label_index = net.blobs['loss'].data[0].flatten().argsort()[-1:-top_k-1:-1]
	   labels = unicode_index[label_index.astype(np.int)]  # output unicode

	   #print 'Index: ',label_index 
	   print 'Top-' + str(top_k) + ' Label: ',labels
	   print 'label_truth: ',label_truth

	   for i in range(0,top_k):
			if  labels[i] == int(label_truth):
				rightcount=rightcount+1
				break
	print(rightcount,allcount,(float)(rightcount)/(float)(allcount))   

if __name__=='__main__':
	imagepath='images/'
	top_k = 1;
	evaluate(imagepath,top_k)







                            
