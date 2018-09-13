#-*-coding:utf-8-*-

import os
from FileToVector import *
from svmutil import *
from Normalization import *
from TransformDwarfFile import *

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
model=svm_train(label,data, '-s 0 -t 2 -c 9999 -g 0.01 -e 0.00001 -h 0')
if '86' in path:
    svm_save_model('SaveData/modelsave_x86', model)
elif '64' in path:
    svm_save_model('SaveData/modelsave_x64', model)
else:
    svm_save_model('SaveData/modelsave_x86', model)
print("train ending...")
print('')


"""
后面说一下参数输入的意义：
　　-s svm类型：SVM设置类型(默认0)
　　0 -- C-SVC
　　1 --v-SVC
　　2 – 一类SVM
　　3 -- e -SVR
　　4 -- v-SVR
　　-t 核函数类型：核函数设置类型(默认2)
　　0 – 线性：u'v
　　1 – 多项式：(r*u'v + coef0)^degree
　　2 – RBF函数：exp(-r|u-v|^2)
　　3 –sigmoid：tanh(r*u'v + coef0)

-g r(gama)：核函数中的gamma函数设置(针对多项式/rbf/sigmoid核函数)

-c cost：设置C-SVC，e -SVR和v-SVR的参数(损失函数)(默认1)


Chinese:
Options：可用的选项即表示的涵义如下
　　-s svm类型：SVM设置类型(默认0)
　　0 -- C-SVC
　　1 --v-SVC
　　2 – 一类SVM
　　3 -- e -SVR
　　4 -- v-SVR
　　-t 核函数类型：核函数设置类型(默认2)
　　0 – 线性：u'v
　　1 – 多项式：(r*u'v + coef0)^degree
　　2 – RBF函数：exp(-gamma|u-v|^2)
　　3 –sigmoid：tanh(r*u'v + coef0)
　　-d degree：核函数中的degree设置(针对多项式核函数)(默认3)
　　-g r(gama)：核函数中的gamma函数设置(针对多项式/rbf/sigmoid核函数)(默认

1/ k)
　　-r coef0：核函数中的coef0设置(针对多项式/sigmoid核函数)((默认0)
　　-c cost：设置C-SVC，e -SVR和v-SVR的参数(损失函数)(默认1)
　　-n nu：设置v-SVC，一类SVM和v- SVR的参数(默认0.5)
　　-p p：设置e -SVR 中损失函数p的值(默认0.1)
　　-m cachesize：设置cache内存大小，以MB为单位(默认40)
　　-e eps：设置允许的终止判据(默认0.001)
　　-h shrinking：是否使用启发式，0或1(默认1)
　　-wi weight：设置第几类的参数C为weight*C(C-SVC中的C)(默认1)
　　-v n: n-fold交互检验模式，n为fold的个数，必须大于等于2
　　其中-g选项中的k是指输入数据中的属性数。option -v 随机地将数据剖分为n部

分并计算交互检验准确度和均方根误差。以上这些参数设置可以按照SVM的类型和核函

数所支持的参数进行任意组合，如果设置的参数在函数或SVM类型中没有也不会产生影

响，程序不会接受该参数；如果应有的参数设置不正确，参数将采用默认值。

例子：
y, x = svm_read_problem('C:\Program Files (x86)\libsvm-3.21\heart_scale')
m = svm_train(y[:200], x[:200], '-c 4')
p_label, p_acc, p_val = svm_predict(y[200:], x[200:], m)
print('---------------------------------------------')

#data=[{1:176,2:70},{1:180,2:80},{1:161,2:45},{1:163,2:47}]
data=[[176,70],[180,80],[161,45],[163,47]]
label = [2,2,1,1]
model=svm_train(label,data)
svm_save_model('modelsave',model)
#model=svm_load_model('modelsave')
testdata=[{1:190,2:85},[160,43]]
testdatalabel = [2,1]
predictlabel,accuracy,value = svm_predict(testdatalabel,testdata,model)
print(predictlabel)
print('---------------------------------------------')


举个例子如下：
C:/libsvm-2.85/windows>svmtrain heart_scale
*
optimization finished, #iter = 162
nu = 0.431029
obj = -100.877288, rho = 0.424462
nSV = 132, nBSV = 107
Total nSV = 132
现简单对屏幕回显信息进行说明：
#iter为迭代次数，
nu 与前面的操作参数-n nu 相同，
obj为SVM文件转换为的二次规划求解得到的最小值，
rho 为判决函数的常数项b，
nSV 为支持向量个数，
nBSV为边界上的支持向量个数，
Total nSV为支持向量总个数。
训练后的模型保存为文件*.model，用记事本打开其内容如下：
svm_type c_svc % 训练所采用的svm类型，此处为C- SVC
kernel_type rbf %训练采用的核函数类型，此处为RBF核
gamma 0.0769231 %设置核函数中的g ，默认值为1/ k
nr_class 2 %分类时的类别数，此处为两分类问题
total_sv 132 %总共的支持向量个数
rho 0.424462 %决策函数中的常数项b
label 1 -1%类别标签
nr_sv 64 68 %各类别标签对应的支持向量个数
SV %以下为支持向量
"""
