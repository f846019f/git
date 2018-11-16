#!/usr/bin/env python

import numpy as np
import sys
import os
import caffe
import cv2 as cv

#ɾ�������ֹ�
VALUE_NUM = '1'
MODEL_NAME = 'china_lenet'

MODEL_FILE = '../../' + MODEL_NAME  + '_deploy.prototxt'
PRETRAINED = '../../weights/' + MODEL_NAME + '/' + MODEL_NAME + '_value' + VALUE_NUM + '_iter_15000.caffemodel'
IMAGE_FILE = '/home/higaki/china_data/image_0/test/alp/A/0202_SN1_3.png'

if not os.path.isfile(MODEL_FILE):
    print("error: caffe model load...")

if not os.path.isfile(PRETRAINED):
    print("error: pre-trained caffe model...")

if not os.path.isfile(IMAGE_FILE):
    print("error: image_file not open.")

print ' '
print MODEL_FILE
print PRETRAINED

print ' '


#�ƥ��ȥǡ�����numpy�ե��������##

#width, height, test_class���
width = 14
height = 20
test_class = 36

#dir_list��PATH�Υե����������Ƥ���
PATH = '/home/higaki/china_data/image_' + VALUE_NUM + '/test/'
tmp = os.listdir(PATH)
tmp = sorted([x for x in tmp if os.path.isdir(PATH + x)])
dir_list = tmp 
#print(dir_list)

X_test = []
Y_test = []
image_name = []
label = 0

# alp or num �����
for alp_num in dir_list:
    if str(alp_num) == 'num':
        label = 0
    if str(alp_num) == 'alp':
        label = 10
    
    tmp = os.listdir(PATH + str(alp_num) + '/')
    #print tmp
    tmp = sorted([x for x in tmp if os.path.isdir(PATH + '/' + str(alp_num) + '/' + x)])
    #print tmp
    alp_num_list = tmp 
    
    # A~Z or 0~9 ����� 
    for dir_name in alp_num_list :
        file_list = os.listdir(PATH + str(alp_num) + '/' + str(dir_name))
        #print dir_name
        #print len(file_list)
        
        # ���줾��β��������
        for file_name in file_list:
            if file_name.endswith('.png'):
                #image = cv.imread(PATH + str(alp_num) + '/' + str(dir_name) + '/' + file_name, 0)
                #image = cv.resize(image, (width, height))
                #cv.normalize(image, image, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
                #image = image / 255.
                #X_test.append(image)
                Y_test.append(label)
                image_name.append(PATH + str(alp_num) + '/' + str(dir_name) + '/' + file_name)
        
        label = label + 1
        
        #'V'������ʾ�ˤʤ��Τǥ��󥯥���Ȥ��롣
        if label == 31:
            label = label + 1
        
#print len(Y_test)
#print len(image_name)

X_test = np.asarray(X_test)
Y_test = np.asarray(Y_test) 
image_name.sort()

#print(X_test.shape)
#print(Y_test.shape)
#print(len(image_name))


## �ƥ��ȥǡ����Τɤ����ְ㤨�Ƥ��뤫���ǧ ##

caffe.set_mode_cpu()

net = caffe.Classifier(MODEL_FILE, PRETRAINED, image_dims=(20, 14))

for (Y, name) in zip(Y_test, image_name):
    
    if Y == 18:
        Y = 1
        
    if Y == 24:
        Y = 0
    
    input_image = caffe.io.load_image(name, color=False)
    prediction = net.predict([input_image], False)

    #print("prediction shape: {}".format(prediction[0].shape))
    #print("predicted class: {}".format(prediction[0].argmax()) + ' ' + str(Y))
    
    if str(Y) != format(prediction[0].argmax()):
        print name + ' ' + format(prediction[0].argmax())
        #print("predicted class: {}".format(prediction[0].argmax()) + ' ' + str(Y))
    


