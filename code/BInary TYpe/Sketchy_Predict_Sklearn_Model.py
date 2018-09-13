#-*-coding:utf-8-*-

import sys
import os
from FileToVector import *
from svmutil import *
from Normalization import *
from TransformDwarfFile import *

from sklearn.metrics import log_loss, confusion_matrix
from sklearn.model_selection import cross_val_score, KFold
from sklearn.preprocessing import scale, MinMaxScaler
from sklearn.linear_model import SGDClassifier
from sklearn.externals import joblib
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from collections import Counter
from sklearn import tree
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB

import numpy as np
import os
import pickle
import re
import time

data=[]
label=[]
name=[]

#导入测试数据集
path ='TestData_x86-SK'
#path ='TrainData_x86'
#path ='TestData_x64'
#path = 'Microsoft Visual Studio 11.0-VC-crt-src_x86'

#获取path目录下的所有子目录，此处自动将path路径下的训练集加入训练
for i in os.walk(path):
    if i[0]==path:
        continue
    else:
        #每一个目录相当于一个项目的训练集
        for home, dirs, files in os.walk(i[0]):

            File_To_Vector = FileToVector('SaveData/Type_List.txt', 'SaveData/Instructions_List.txt')

            # 先找一下有没有dwarf.txt, 有没有类型信息文件
            flag = 2  # 0表示有类型信息文件，1表示没有但有dwarf.txt，2表示都没有
            dwarfFilePath = ''
            for filename in files:
                # 目录下的文件分为类型信息文件和汇编代码文件
                # 文件最近一层目录名就是项目名
                head, homeName = home.split('\\', 1)
                typefile = homeName + '.txt'
                if filename == typefile:
                    flag = 0
                    break
                elif re.search('[Dd][Ww][Aa][Rr][Ff]\.[tT][xX][tT]', filename):
                    dwarfFilePath = home.replace("\\", "/") + '/' + filename
                    flag = 1

            # 把dwarf文件转换成为类型信息文件
            if flag == 0:
                pass
            elif flag == 1:
                if not dwarfFilePath == '':
                    afterTransformPath = home.replace("\\", "/") + '/' + homeName + '.txt'
                    TransformDwarfFile(dwarfFilePath, afterTransformPath)
            elif flag == 2:
                print(home.replace("\\", "/") + '/' + " : missing debug information")
                break

            #开始添加数据
            for filename in files:
                #目录下的文件分为类型信息文件和汇编代码文件
                #文件最近一层目录名就是项目名
                homeName=''
                if sys.platform == 'win32':
                    head, homeName = home.split('\\', 1)
                else:
                    head, homeName = home.split('/', 1)
                typefile=homeName+'.txt'
                # 只要.txt文件
                if re.search('.+\.[tT][xX][tT]', filename):
                    if filename!=typefile:
                        if sys.platform == 'win32':
                            fileFullName=home.replace("\\", "/")+'/'+filename
                            typefileFullName=home.replace("\\", "/")+'/'+typefile
                        else:
                            fileFullName = home + '/' + filename
                            typefileFullName = home + '/' + typefile
                        NormatizeAssemblyfile(fileFullName)
                        File_To_Vector.File2Vector(fileFullName,typefileFullName )

            File_To_Vector.UpdateUDrelation()
            #去掉标签是-1的项
            for each_vector, each_label, each_name in zip(File_To_Vector.Vector_list,File_To_Vector.Label_list,File_To_Vector.Name_list):
                if not each_label==-1:
                    data.append(each_vector)
                    label.append(each_label)
                    name.append(each_name)

TFIDFNormalization(data,7)
#Z_ScoreNormalization(data,5)#向量-1~1归一化处理
#MaxMinNormalization(data,0)#向量zscore归一化处理

#print(File_To_Vector.Name_list)
#print(File_To_Vector.Label_list)
#print(File_To_Vector.Vector_list)
#print(File_To_Vector.UDrelation)
##print(len(File_To_Vector.Name_list))
##print(len(File_To_Vector.Label_list))
##print(len(File_To_Vector.Vector_list))

X_test = np.zeros((len(data),len(data[0])))
Y = np.array([0]*len(label))

#将data和label中的数据放给data_asm和Y
for i in range(0,len(data)):
    for j in range(0,len(data[0])):
        X_test[i][j]=data[i][j]
for i in range(0,len(label)):
    Y[i]=label[i]


clf = joblib.load("SaveData/clf_model.m")
min_max_scaler = joblib.load("SaveData/min_max_scaler.m")

#===data_asm = np.log(data_asm + 1)==
X_test = np.log(X_test + 1)
X_test = min_max_scaler.transform(X_test)

start = time.clock()  # 计算时间
result = clf.predict_proba(X_test)
label = clf.predict(X_test)
end = time.clock()  # 计算时间
print('\nTesting time:', end - start,end='\n\n\n')

"""
########################################
joblib.dump(result, "SaveData/D_ML_result/skTemp_prob.save")
joblib.dump(label, "SaveData/D_ML_result/skTemp_pred.save")
joblib.dump(Y, "SaveData/D_ML_result/skTemp_Y.save")
#joblib.dump(result, "SaveData/D_ML_result/KNN_prob.save")
#joblib.dump(label, "SaveData/D_ML_result/KNN_pred.save")
#joblib.dump(Y, "SaveData/D_ML_result/KNN_Y.save")
print("\n\nresult save\n\n\n")
##################################
"""

###输出混淆矩阵###
print('accuracy = ',end='')
print(accuracy_score(Y, label))

cm = confusion_matrix(Y, label)
print(classification_report(Y, label))
print(cm)