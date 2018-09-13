#-*-coding:utf-8-*-

import os
import pickle
from FileToSequence import *
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

            File_To_Sequence = FileToSequence('SaveData/Type_List.txt', 'SaveData/Instructions_List.txt')

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
                            File_To_Sequence.File2Sequence(trianfileFullName,typefileFullName )

            File_To_Sequence.UpdateUDrelation()
            for each_sequence, each_label in zip(File_To_Sequence.Sequence_list,File_To_Sequence.Label_list):
                if not each_label==-1:
                    data.append(each_sequence)
                    label.append(each_label)

for each in data:#插入表头
    each.insert(0,'start')

def frequencyOfEachTerm(data):#c(wi-1)的计数结果
    InstructionList = File2List('SaveData/Instructions_List.txt')
    InstructionList.insert(0,'start')# 插入表头
    foet=[]
    for eacht in InstructionList:
        count=0
        for eachSequence in data:
            for eachIR in eachSequence:
                if eacht == eachIR:
                    count = count + 1
        foet.append(count)
    return foet

def frequencyOfSuccession(data): #计数c(wi-1，wi)
    InstructionList = File2List('SaveData/Instructions_List.txt')
    InstructionList.insert(0, 'start')  # 插入表头
    List = [ [0 for i in range(len(InstructionList))] for i in range(len(InstructionList))]

    for i in range(len(InstructionList)):
        for j in range(len(InstructionList)):
            count=0
            for each_sequence in data:
                for k in range(1,len(each_sequence)):
                    if InstructionList[i]==each_sequence[k-1] and InstructionList[j]==each_sequence[k]:
                        count = count + 1
            List[i][j]=count

    return List


def ConditionalProbability(listFist,matrixSecond): #计算条件概率,使用加一数据平滑
    for i in range(len(matrixSecond)):
        for j in range(len(listFist)):
            matrixSecond[i][j] = (matrixSecond[i][j]+1)/(listFist[j]+len(listFist))


def findIndex(IR): #找在矩阵中的ij位置
    InstructionList = File2List('SaveData/Instructions_List.txt')
    InstructionList.insert(0, 'start')  # 插入表头
    for i in range(0,len(InstructionList)):
        if InstructionList[i]==IR:
            return i

def ComputingProbability(sequence,matrix): #计算一个序列的概率
    Probability = 1
    for i in range(1,len(sequence)):
        first = findIndex(sequence[i-1])
        second = findIndex(sequence[i])
        Probability = Probability * matrix[first][second]
    return Probability


dataSplit = [[],[],[],[],[],[],[],[]] #label 0~7
for d,l in zip(data,label):
    for i in range(0,7):
        if l==i:
            dataSplit[i].append(d)

"""有噪音，暂时找不到"""
waitingToRemove=[]
for each in dataSplit[5]:
    if '[address]' in each or '[?+address+?]' in each:
        dataSplit[7].append(each)
    if each[1] == 'dword':
        waitingToRemove.append(each)
for each in waitingToRemove:
    dataSplit[5].remove(each)
"""人为去噪音"""

ProbabilityTable = []
for each in dataSplit:
    list1 = frequencyOfEachTerm(each)
    list2 = frequencyOfSuccession(each)
    ConditionalProbability(list1, list2)
    ProbabilityTable.append(list2)

try:
    with open('SaveData/SLMProbabilityTable.pickle', 'wb') as table:
        pickle.dump(ProbabilityTable, table)
except IOError as err:
    print("File error:" + str(err))
except pickle.PickleError as perr:
    print('Pickling error:' + str(perr))

"""
s = ['start', 'dword', '[address]', 'mov reg', '[address]', 'mov reg', '[address]', 'mov reg']

mostIndex = 999
biggest = 0
for i in range(0,len(ProbabilityTable)):
    print(ComputingProbability(s, ProbabilityTable[i]))
    if ComputingProbability(s,ProbabilityTable[i]) > biggest:
        biggest = ComputingProbability(s,ProbabilityTable[i])
        mostIndex = i
    else:
        pass

TypeList = File2List('SaveData/Type_List.txt')
print(TypeList[mostIndex])
"""
