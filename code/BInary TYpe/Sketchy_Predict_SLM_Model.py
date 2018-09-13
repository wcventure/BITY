#-*-coding:utf-8-*-

import sys
import os
from Train_SLM_Model import *
from FileToSequence import *
from Normalization import *
from TransformDwarfFile import *


#读取概率表
with open('SaveData/SLMProbabilityTable.pickle', 'rb') as ProbabilityData:
    ProbabilityTable = pickle.load(ProbabilityData)


data=[]
label=[]
name=[]

#导入测试数据集
#path ='TestData_x86'
path ='TrainData_x86'
#path ='TestData_x64'
#path = 'Microsoft Visual Studio 11.0-VC-crt-src_x86'

#获取path目录下的所有子目录，此处自动将path路径下的训练集加入训练
for i in os.walk(path):
    if i[0]==path:
        continue
    else:
        #每一个目录相当于一个项目的训练集
        for home, dirs, files in os.walk(i[0]):

            File_To_Sequence = FileToSequence('SaveData/Type_List.txt', 'SaveData/Instructions_List.txt')

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
                        File_To_Sequence.File2Sequence(fileFullName,typefileFullName )

            File_To_Sequence.UpdateUDrelation()
            #去掉标签是-1的项
            for each_vector, each_label, each_name in zip(File_To_Sequence.Sequence_list,File_To_Sequence.Label_list,File_To_Sequence.Name_list):
                if not each_label==-1:
                    data.append(each_vector)
                    label.append(each_label)
                    name.append(each_name)


for each in data:#插入表头
    each.insert(0,'start')


predictlabel_list = [0]
predictlabel_list = predictlabel_list*len(data)


#SLM模型预测
for k in range(0,len(data)):
    mostIndex = 999
    biggest = 0
    for i in range(0,len(ProbabilityTable)):
        if ComputingProbability(data[k],ProbabilityTable[i]) > biggest:
            biggest = ComputingProbability(data[k],ProbabilityTable[i])
            mostIndex = i
        else:
            pass
    predictlabel_list[k] = mostIndex


#输出结果
Type_list=File2List('SaveData/Type_List.txt')
print('')
print('********************************************************')
print('Format: FunctionName:VarName-----predictlabel/rightlabel')
print('********************************************************')
print('')

rightNum = 0
totalNum = len(label)

for each_var,each_predictlabel,each_rightlabel in zip(name , predictlabel_list , label):
    #if not Type_list[int(each_predictlabel)]==Type_list[each_rightlabel]:
        print(each_var,end="")
        print('-----',end="")
        print(Type_list[int(each_predictlabel)],end="")
        print('/',end="")
        print(Type_list[each_rightlabel])

        #统计正确率
        if each_predictlabel == each_rightlabel:
            rightNum = rightNum + 1

print('')
print('********************************************************')
print('accuracy = ',rightNum/totalNum)