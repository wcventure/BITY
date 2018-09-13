#-*-coding:utf-8-*-
import sys,os
import re
import pickle

def FindMaxMin(mat):#查找某一维度上的最大值和最小值
    #暂时以mat中的第一个元素来作为最大最小值
    maxList=[]
    minList=[]
    for i in mat[0]:
        maxList.append(float(i))
        minList.append(float(i))
    #更新最大值与最小值
    for i in mat:
        for j in range(0,len(i)):
            if i[j]>maxList[j]:
                maxList[j]=float(i[j])
            if i[j]<minList[j]:
                minList[j]=float(i[j])
    try:
        with open('SaveData/Normalization/MaxNormalize.pickle','wb') as maxData,open('SaveData/Normalization/MinNormalize.pickle','wb') as minData:
            #将最大值和最小值保留下来，测试数据要用同样的规则归一化
            pickle.dump(maxList,maxData)
            pickle.dump(minList,minData)
    except IOError as err:
            print("File error:"+str(err))
    except pickle.PickleError as perr:
            print('Pickling error:'+str(perr))

def FindMuSigma(mat):#查找某一维度上的平均值和方差
    muList=[]
    sigmaList=[]
    for i in range(0,len(mat[0])):
        muList.append(0.0)
        sigmaList.append(0.0)
    #计算平均值
    for i in mat:
        for j in range(0,len(i)):
            muList[j]+=i[j]
    for i in range(0,len(muList)):
        muList[i]=float(muList[i]/len(mat))

    #求标准差
    for i in mat:
        for j in range(0,len(i)):
            sigmaList[j]+=(i[j]-muList[j]) ** 2
    for i in range(0,len(sigmaList)):
        sigmaList[i]=(sigmaList[i]/(len(mat)-1)) ** 0.5

    try:
        with open('SaveData/Normalization/MuNormalize.pickle','wb') as muData,open('SaveData/Normalization/SigmaNormalize.pickle','wb') as sigmaData:
            #将平均值和标准差保留下来，测试数据要用同样的规则归一化
            pickle.dump(muList,muData)
            pickle.dump(sigmaList,sigmaData)
    except IOError as err:
            print("File error:"+str(err))
    except pickle.PickleError as perr:
            print('Pickling error:'+str(perr))

def FindIDF(mat):
    IDFList=[]
    for i in range(0,len(mat[0])):
        IDFList.append(0.0)
    #计算idf值
    for i in mat:
        for j in range(0,len(i)):
            if i[j]!=0:
                IDFList[j]+=1
    for i in range(0,len(IDFList)):
        if IDFList[i]!=0:
            IDFList[i]=len(mat)/IDFList[i]
        #print(IDFList[i])

    try:
        with open('SaveData/Normalization/IDFNormalize.pickle','wb') as IDFData:
            pickle.dump(IDFList,IDFData)
    except IOError as err:
            print("File error:"+str(err))
    except pickle.PickleError as perr:
            print('Pickling error:'+str(perr))

def MaxMinNormalization(mat,start):#将向量归一化，最大最小值归一化
    try:
        with open('SaveData/Normalization/MaxNormalize.pickle','rb') as maxData,open('SaveDataNormalization/MinNormalize.pickle','rb') as minData:
            #从文件中读取最大最小值得列表
            maxList=pickle.load(maxData)
            minList=pickle.load(minData)
            for i in mat:
                for j in range(start,len(i)):
                    if maxList[j]-minList[j]!=0:
                        i[j] =float(i[j]-minList[j]) / float(maxList[j]-minList[j])
                    else:
                        i[j] = 0.0
    except IOError as err:
            print("File error:"+str(err))
    except pickle.PickleError as perr:
            print('Pickling error:'+str(perr))

def Z_ScoreNormalization(mat,start): #将向量归一化，Z-score标准化
    try:
        with open('SaveData/Normalization/MuNormalize.pickle','rb') as muData,open('SaveData/Normalization/SigmaNormalize.pickle','rb') as sigmaData:
            #从文件中读取均值和标准差的列表
            muList=pickle.load(muData)
            sigmaList=pickle.load(sigmaData)
            for i in mat:
                for j in range(start,len(i)):
                    if sigmaList[j] != 0:
                        i[j] = (i[j] - muList[j]) / sigmaList[j]
                    else:
                        i[j] = 0.0
    except IOError as err:
            print("File error:"+str(err))
    except pickle.PickleError as perr:
            print('Pickling error:'+str(perr))

def TFIDFNormalization(mat,start):
    try:
        with open('SaveData/Normalization/IDFNormalize.pickle', 'rb') as IDFData:
            IDFList=pickle.load(IDFData)
            for i in mat:
                #统计第一个网页词数N，计算第一个网页第一个词在该网页中出现的次数n，再找出该词在所有文档中出现的次数m。则该词的tf-idf 为：n/N * 1/(m/M)  （还有其它的归一化公式，这里是最基本最直观的公式）
                TotalValue=0
                for j in range(start,len(i)):
                    TotalValue+=i[j]

                for j in range(start, len(i)):
                    if not TotalValue==0:
                        i[j] = (i[j]/TotalValue) * IDFList[j]


                #最大也就30就好了
                for j in range(start,len(i)):
                    if i[j] > 30:
                        i[j] = 30


    except IOError as err:
        print("File error:" + str(err))
    except pickle.PickleError as perr:
        print('Pickling error:' + str(perr))

def NormatizeAssemblyfile(filename):
    try:
        with open(filename,encoding='utf-8') as assemblyfile:
            thisline = assemblyfile.readline()
            if '.text:' not in thisline or '.seg' not in thisline:
                return

        with open(filename,encoding='utf-8') as assemblyfile:
            fileContext = assemblyfile.readlines()
            assemblyfile.seek(0)
            ContextLen = len(fileContext)
            for lineNum in range(0, ContextLen - 1):
                if '.text:' in fileContext[lineNum]:
                    fileContext[lineNum], subn_num = re.subn("\.text:\w+", "",fileContext[lineNum])
                    #print(fileContext[lineNum],end='')
                if '.seg:' in fileContext[lineNum]:
                    fileContext[lineNum], subn_num = re.subn("\.seg:\w+", "", fileContext[lineNum])
                    # print(fileContext[lineNum],end='')
        with open(filename,'w+') as assemblyfile:
            assemblyfile.writelines(fileContext)

    except IOError as err:
        print("File error:" + str(err))