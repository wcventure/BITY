#-*-coding:utf-8-*-

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

#导入训练集
path = 'TrainData_x86'
#path = 'TrainData_x64'

#获取path目录下的所有子目录，此处自动将path路径下的训练集加入训练
for i in os.walk(path):
    if i[0]==path:
        continue
    else:
        #每一个目录相当于一个项目的训练集
        for home, dirs, files in os.walk(i[0]):

            File_To_Vector = FileToVector('SaveData/Type_List.txt', 'SaveData/Instructions_List.txt')

            #先找一下有没有dwarf.txt, 有没有类型信息文件
            flag=2 #0表示有类型信息文件，1表示没有但有dwarf.txt，2表示都没有
            dwarfFilePath=''
            for filename in files:
                # 目录下的文件分为类型信息文件和汇编代码文件
                # 文件最近一层目录名就是项目名
                head, homeName = home.split('\\', 1)
                typefile = homeName + '.txt'
                if filename==typefile:
                    flag=0
                    break
                elif re.search('[Dd][Ww][Aa][Rr][Ff]\.[tT][xX][tT]', filename):
                    dwarfFilePath = home.replace("\\", "/")+'/'+filename
                    flag=1

            #把dwarf文件转换成为类型信息文件
            if flag==0:
                pass
            elif flag==1:
                if not dwarfFilePath == '':
                    afterTransformPath =home.replace("\\", "/") + '/' + homeName + '.txt'
                    TransformDwarfFile(dwarfFilePath , afterTransformPath)
            elif flag==2:
                print (home.replace("\\", "/")+'/'+" : missing debug information")
                break

            #开始添加训练数据
            for filename in files:
                #目录下的文件分为类型信息文件和汇编代码文件
                #文件最近一层目录名就是项目名
                head,homeName=home.split('\\',1)
                typefile=homeName+'.txt'

                # 只要.txt文件
                if re.search('.+\.[tT][xX][tT]', filename):
                    if filename!=typefile:
                        if not re.search('[Dd][Ww][Aa][Rr][Ff]\.[tT][xX][tT]', filename):#不要包含dwarf.txt
                            trianfileFullName=home.replace("\\", "/")+'/'+filename
                            typefileFullName=home.replace("\\", "/")+'/'+typefile
                            NormatizeAssemblyfile(trianfileFullName)
                            File_To_Vector.File2Vector(trianfileFullName,typefileFullName )

            File_To_Vector.UpdateUDrelation()
            for each_vector, each_label in zip(File_To_Vector.Vector_list,File_To_Vector.Label_list):
                if not each_label==-1:
                    data.append(each_vector)
                    label.append(each_label)

            #data.extend(File_To_Vector.Vector_list)
            #label.extend(File_To_Vector.Label_list)


##print(File_To_Vector.Name_list)
##print(File_To_Vector.Label_list)
##print(File_To_Vector.Vector_list)
##print(len(File_To_Vector.Name_list))
##print(len(File_To_Vector.Label_list))
#print(len(File_To_Vector.Vector_list))

#FindMuSigma(data)#找各个维度平均值和标准差
#Z_ScoreNormalization(data,5)#向量zscore归一化处理
#FindMaxMin(data);#找各个维度最大值和最小值
#MaxMinNormalization(data,5)#向量-1~1归一化处理

FindIDF(data)
TFIDFNormalization(data,7)

"""
#看TF-IDF
for i in range(0,len(data[0])):
    for d,v in zip(data,label):
        if v==7:
            print(d[i],end='\t')
    print('')
"""

#model=svm_train(label,data, '-s 0 -t 1 -c 3 -d 4 -r 0 -e 0.00001 -h 0')
#model=svm_train(label,data, '-s 0 -t 2 -c 9999 -g 0.01 -e 0.00001 -h 0')

data_asm = np.zeros((len(data),len(data[0])))
Y = np.array([0]*len(label))

#将data和label中的数据放给data_asm和Y
for i in range(0,len(data)):
    for j in range(0,len(data[0])):
        data_asm[i][j]=data[i][j]
for i in range(0,len(label)):
    Y[i]=label[i]

#===data_asm = np.log(data_asm + 1)==#防止MemoryError
half=len(data_asm)/2
data_asm[:int(half)] = np.log(data_asm[:int(half)] + 1)
data_asm[int(half):] = np.log(data_asm[int(half):] + 1)

min_max_scaler = MinMaxScaler()
data_asm = min_max_scaler.fit_transform(data_asm)

#### Train ####
#clf = SGDClassifier(loss="log", max_iter=100, shuffle=True, n_jobs=2)
#clf = RandomForestClassifier(n_estimators=10, criterion='entropy')
#clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = RandomForestClassifier(n_estimators=10, criterion='gini')
#clf = tree.DecisionTreeClassifier(criterion='gini')
#clf = GaussianNB()
#clf = MultinomialNB()
#clf = BernoulliNB()
#clf = KNeighborsClassifier(n_neighbors=7)
#clf = SVC(kernel='sigmoid', probability=True)
#clf = SVC(kernel="linear", probability=True)
#clf = SVC(kernel="rbf", gamma=0.7, probability=True)


start = time.clock()  # 计算时间
clf.fit(data_asm, Y)
end = time.clock()  # 计算时间
print('\ntraining time:', end - start)

joblib.dump(clf, "SaveData/clf_model.m")
joblib.dump(min_max_scaler, "SaveData/min_max_scaler.m")
print('Saved',end='\n\n\n')

clf = joblib.load("SaveData/clf_model.m")
r = clf.predict(data_asm)
p = clf.predict_proba(data_asm)

print('loss = ',end='')
print ("%.3f" % log_loss(Y, p))
print('accuracy = ',end='')
print(accuracy_score(Y, r))

cm = confusion_matrix(Y, r)
print(classification_report(Y, r))
print(cm)
print('\n')
print('\n')




####################################
############### CV #################

def run_cv(X, y, clf):
    # Construct a kfolds object
    n_splits=5
    kf = KFold(n_splits=n_splits, shuffle=True)
    y_prob = np.zeros((len(y), 8))
    y_pred = np.zeros(len(y))

    # Iterate through folds
    training_time = 0
    testing_time = 0

    for train_index, test_index in kf.split(X):
        X_train, X_test = X[train_index], X[test_index]
        y_train = y[train_index]

        start = time.clock()  # 计算时间
        clf.fit(X_train, y_train)
        end = time.clock()  # 计算时间
        training_time = training_time + end - start

        start = time.clock()  # 计算时间
        y_prob[test_index] = clf.predict_proba(X_test)
        y_pred[test_index] = clf.predict(X_test)
        end = time.clock()  # 计算时间
        testing_time = training_time + end - start

    print('training time:',training_time / n_splits)
    print('testing time:', testing_time / n_splits)

    return y_prob, y_pred

#### See potential score on CV ####
#clf = SGDClassifier(loss="log", max_iter=100, shuffle=True, n_jobs=2)
clf = RandomForestClassifier(n_estimators=10, criterion='gini')
#clf = RandomForestClassifier(n_estimators=10, criterion='entropy')
#clf = tree.DecisionTreeClassifier(criterion='gini')
#clf = tree.DecisionTreeClassifier(criterion='entropy')
#clf = GaussianNB()
#clf = MultinomialNB()
#clf = BernoulliNB()
#clf = KNeighborsClassifier(n_neighbors=7)
#clf = SVC(kernel='sigmoid', probability=True)
#clf = SVC(kernel="linear", probability=True)
#clf = SVC(kernel="rbf", gamma=0.7, probability=True)

prob, pred = run_cv(data_asm, Y, clf)

"""
########################################
joblib.dump(prob, "SaveData/D_CVML_result/skTemp_prob.save")
joblib.dump(pred, "SaveData/D_CVML_result/skTemp_pred.save")
joblib.dump(Y, "SaveData/D_CVML_result/skTemp_Y.save")
#joblib.dump(prob, "SaveData/D_CVML_result/DTgini_prob.save")
#joblib.dump(pred, "SaveData/D_CVML_result/DTgini_pred.save")
#joblib.dump(Y, "SaveData/D_CVML_result/DTgini_Y.save")
print("\nresult save\n\n\n")
##################################
"""

print('loss = ',end='')
print ("%.3f" % log_loss(Y, prob))
print('accuracy = ',end='')
print(accuracy_score(Y, pred))

cm = confusion_matrix(Y, pred)
print(classification_report(Y, pred))
print(cm)