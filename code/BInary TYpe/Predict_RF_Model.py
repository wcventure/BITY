#-*-coding:utf-8-*-

import sys
import os
import time
import copy
from FileToVector import *
from svmutil import *
from Normalization import *
from sklearn.externals import joblib
import numpy as np
import os
import pickle
import re
import time


#导入测试数据集
#path = 'Microsoft Visual Studio 11.0-VC-crt-src_x86'
#path = 'SaveData\\tempCode\\predict'
path = 'TestData_x86'


if sys.platform == 'win32':
    pass
else:
    path = path.replace('\\', '/')

mode='x86'


#获取path目录下的所有子目录，此处自动将path路径下的训练集加入训练
for i in os.walk(path):
    if i[0]==path:
        continue
    else:
        #每一个目录相当于一个项目的训练集
        for home, dirs, files in os.walk(i[0]):

            #totalTime = 0#计算时间
            #start = time.clock()#计算时间

            File_To_Vector = OnlyFileToVector('SaveData/Type_List.txt', 'SaveData/Instructions_List.txt')
            #空文件夹的提示
            if files==[]:
                print("\t" + "{:<35}".format(home) + ' is an empty folder')
                break

            # 有一些函数原型的信息保存在“function_prototype”中
            for filename in files:
                if filename == 'function_prototype':
                    File_To_Vector.addFunctionPrototype(home + '/' + filename)

            #正式开始
            for filename in files:
                #目录下的文件分为类型信息文件和汇编代码文件
                #文件最近一层目录名就是项目名
                homeName = ''
                if sys.platform == 'win32':
                    head, homeName = home.split('\\', 1)
                else:
                    head, homeName = home.split('/', 1)
                typefile=homeName+'.txt'

                # 只要.txt文件
                if re.search('.+\.[tT][xX][tT]$', filename):
                    if filename!=typefile:
                        if sys.platform == 'win32':
                            fileFullName=home.replace("\\", "/")+'/'+filename
                        else:
                            fileFullName = home + '/' + filename
                        NormatizeAssemblyfile(fileFullName)
                        File_To_Vector.File2Vector(fileFullName)

                        #此处做一个小测试，简单判断mode是否为x64
                        with open(fileFullName,encoding='utf-8') as whatmode:
                            for i in range(3,20):
                                line = whatmode.readline()
                                if 'rbp' in line and 'rsp' in line:
                                    mode = 'x64'
                                    print('This is a x64 program')
                        #简单地判断就是只找mov rbp , rsp。为了效率只看前20行



            #++++++++++++++++++++++++++#

            File_To_Vector.UpdateUDrelation()

            #for each in data:
                #print(each)
            #print(File_To_Vector.pointer_vector_list)

            clf = joblib.load("SaveData/clf_model.m")
            min_max_scaler = joblib.load("SaveData/min_max_scaler.m")

            Type_list=File2List('SaveData/Type_List.txt')
            Instructions_List=File2List('SaveData/Instructions_List.txt')
            adbaisindex=0
            for i in range(0,len(Instructions_List)):
                if Instructions_List[i]=='[?+address+?]':
                    adbaisindex=i
                    break

            structTypeOutput = []
            #############################################定义一个预测函数，用于迭代
            def Predict(File_To_Vector,data,label,printre=0):

                varPredictResult = []  # 用来存放预测的变量信息
                varPointerResult = []  # 用来存放二次预测的指针指向的变量的信息
                PointerDetail=[]#用于保存后面预测的PointerDetail

                if data == []:
                    return

                # 将data中的数据放给X_test
                X_test = np.zeros((len(data), len(data[0])))
                for i in range(0, len(data)):
                    for j in range(0, len(data[0])):
                        X_test[i][j] = data[i][j]
                X_test = np.log(X_test + 1)
                X_test = min_max_scaler.transform(X_test)
                predictlabel_list_np = clf.predict(X_test)

                # 将clf.predict(X_test)之后的数据存回列表的形式
                predictlabel_list = []
                for i in range(0,len(predictlabel_list_np)):
                    predictlabel_list.append(predictlabel_list_np[i])

                #predictlabel_list, accuracy, value = svm_predict(label, data, model,'-q')


                AreThereAnyPointer=0#标记有没有指针指向的变量可以预测
                if not File_To_Vector.pointer_label_list==[]:
                    AreThereAnyPointer=1

                    # 将File_To_Vector.pointer_vector_list中的数据放给X_test
                    X_test_p = np.zeros((len(File_To_Vector.pointer_vector_list), len(File_To_Vector.pointer_vector_list[0])))
                    for i in range(0, len(File_To_Vector.pointer_vector_list)):
                        for j in range(0, len(File_To_Vector.pointer_vector_list[0])):
                            X_test_p[i][j] = File_To_Vector.pointer_vector_list[i][j]
                    X_test_p = np.log(X_test_p + 1)
                    X_test_p = min_max_scaler.transform(X_test_p)
                    predictlabel_list_pointer_np = clf.predict(X_test_p)

                    # 将clf.predict(X_test)之后的数据存回列表的形式
                    predictlabel_list_pointer = []
                    for i in range(0, len(predictlabel_list_pointer_np)):
                        predictlabel_list_pointer.append(predictlabel_list_pointer_np[i])

                    #predictlabel_list_pointer, accuracy_pointer, value_pointer = svm_predict(File_To_Vector.pointer_label_list,File_To_Vector.pointer_vector_list, model, '-q')

                for each_var, each_predictlabel,each_offset in zip(File_To_Vector.Name_list,predictlabel_list,File_To_Vector.Offset_list):
                    varPredictResult.append( {'varName':each_var,'varOffset':each_offset,'varType':Type_list[int(each_predictlabel)]} )

                if AreThereAnyPointer==1:
                    for each_var, each_predictlabel in zip(File_To_Vector.pointer_name_list,predictlabel_list_pointer):
                        varPointerResult.append({'pointerName':each_var,'pointerType':Type_list[int(each_predictlabel)]+'*'})


                #输出
                #print(varPredictResult)
                #print(varPointerResult)
                """
                if not varPredictResult == []:
                    for each in varPredictResult:
                        print("{:<45}".format(each['varName']), end="")
                        print("{:<10}".format(each['varOffset']), end="")
                        print('--- ', end="")
                        print(each['varType'])
                    print('')"""

                if varPointerResult != [] or File_To_Vector.FP_Pointer_rel!=[]:#此处确定过才改的 or, 后面if语句那个是and
                    #print('Pointer Detail:')
                    FPset=set(File_To_Vector.FP_Pointer_rel)#集合去重复
                    for each in FPset:
                        left, right = each.split('---')
                        for eachPR in varPredictResult:
                            if left == eachPR['varName']:
                                isappend=0
                                for e in varPointerResult:
                                    if e['pointerName']==left:
                                        if right!='void*' and right!=e['pointerType']:
                                            e['pointerType'] = right #+ ' or ' + e['pointerType']#第一次从FUNCPARAlist中读取的是可信的，取代
                                        isappend=1
                                        break
                                if isappend==0:
                                    varPointerResult.append({'pointerName':left , 'pointerType':right})

                    for each in varPointerResult:
                        #print("{:<25}".format(each['pointerName']), end="")
                        #print(' ====== ', end="")
                        #print(each['pointerType'], end='\n')
                        PointerDetail.append({'Name':each['pointerName'], 'Type':each['pointerType']})

                if File_To_Vector.UDrelation != [] and varPointerResult != []:
                    #print('Same pointerType:')#后来发现不行了，有可能这两个列表都不空，但是没有交集
                    for each in File_To_Vector.UDrelation:
                        left, right = each.split('---')
                        for each_p in varPointerResult:
                            if left == each_p['pointerName'] :
                                #print('Same pointerType:\t'+each)
                                #print("{:<25}".format(right), end = "")
                                #print(' ====== ', end="")
                                #print(each_p['pointerType'],end='\n')
                                PointerDetail.append({'Name': right, 'Type':each_p['pointerType']})
                            elif right==each_p['pointerName']:
                                #print('Same pointerType:\t' + each)
                                #print("{:<25}".format(left), end="")
                                #print(' ====== ', end="")
                                #print(each_p['pointerType'], end='\n')
                                PointerDetail.append({'Name': left, 'Type':each_p['pointerType']})

                #print('@ @ @ end @ @ @')
                #print('**********************************************************************')
                #print('')

                # 剩下的再做整合 之结构体
                structPointerList = []
                arrayPointerList = []

                isStructPointerChange = 0
                LaststructPointer = ''
                for each in PointerDetail:
                    if '+' in each['Name']:
                        structPointer, offset = each['Name'].split('+',1)
                        if LaststructPointer == structPointer:
                            isStructPointerChange = 1
                        else:
                            LaststructPointer = structPointer
                            isStructPointerChange = 0

                        if '*' in each['Name']:
                            arrayPointerList.append(structPointer)  ###指向数组的指针变量名先存其阿里
                            offset = '+' + offset
                            if printre != 0 and isStructPointerChange == 0:
                                structTypeOutput.append('array Pointer: '+ structPointer + '\n')
                                #print('array Pointer:', structPointer)
                            for e in PointerDetail:
                                if structPointer == e['Name']:
                                    if printre != 0 and isStructPointerChange == 0:
                                        isStructPointerChange = 1
                                        structTypeOutput.append('\toffset: ' + "{:<15}".format('+0') + '\t\t' + e['Type'][0:len(e['Type']) - 1] + '\n')
                                        #print('\toffset:', "{:<15}".format('+0'), '\t\t', e['Type'][0:len(e['Type']) - 1])
                            if printre != 0:
                                structTypeOutput.append('\toffset: ' + "{:<15}".format(offset) + '\t\t' + each['Type'][0:len(each['Type']) - 1] + '\n')
                                #print('\toffset:', "{:<15}".format(offset), '\t\t', each['Type'][0:len(each['Type']) - 1])

                        else:
                            structPointerList.append(structPointer)  ###指向结构体的指针变量名先存其阿里
                            offset ='+' + offset
                            if printre!=0 and isStructPointerChange == 0:
                                structTypeOutput.append('struct Pointer: ' + structPointer + '\n')
                                #print('struct Pointer:', structPointer)
                            for e in PointerDetail:
                                if structPointer == e['Name']:
                                    if printre != 0 and isStructPointerChange == 0:
                                        isStructPointerChange = 1
                                        structTypeOutput.append('\toffset: ' + "{:<15}".format('+0') + '\t\t' + e['Type'][0:len(e['Type']) - 1] + '\n')
                                        #print('\toffset:', "{:<15}".format('+0'), '\t\t', e['Type'][0:len(e['Type']) - 1])
                            if printre != 0:
                                structTypeOutput.append('\toffset: ' + "{:<15}".format(offset) + '\t\t' + each['Type'][0:len(each['Type']) - 1] + '\n')
                                #print('\toffset:', "{:<15}".format(offset), '\t\t', each['Type'][0:len(each['Type']) - 1])

                #整合PointerDetail和structPointerList
                i=0
                for each in varPredictResult:
                    for eachP in PointerDetail:#先整合PointerDeta，再整合struct，顺序不能反
                        if each['varName'] == eachP['Name']:
                            each['varType'] = eachP['Type']
                            break

                    for eachS in structPointerList:
                        if eachS == each['varName']:
                            each['varType'] = 'struct*'
                            break

                    if each['varType'] == 'ptr':
                        each['varType']='*'
                    i=i+1

                # 添加指向关系
                #print(File_To_Vector.LEArelation)
                if not File_To_Vector.LEArelation == []:
                    for eachRelation in File_To_Vector.LEArelation:
                        Left, Right = eachRelation.split('->', 1)
                        Left = Left.strip()
                        Right = Right.strip()
                        for each_predictResult in varPredictResult:
                            if Left == each_predictResult['varName'] and (each_predictResult['varType'] == 'ptr' or '*' == each_predictResult['varType']):
                                for eachIsInPredict in varPredictResult:
                                    if eachIsInPredict['varName'] == Right:
                                        each_predictResult['varType'] = eachIsInPredict['varType'] + '*'

                            elif Left == each_predictResult['varName'] and '*' in each_predictResult['varType']:
                                isfind = 0
                                for eachIsInPredict in varPredictResult:
                                    if eachIsInPredict['varName'] == Right:
                                        isfind = 1
                                        if eachIsInPredict['varType'] == each_predictResult['varType'][0:len(each_predictResult['varType'])-1]:
                                            break
                                        else:
                                            if eachIsInPredict['varType'] == 'char' or 'bool':
                                                eachIsInPredict['varType'] = each_predictResult['varType'][0:len(each_predictResult['varType'])-1]
                                            else:
                                                eachIsInPredict['varType'] = eachIsInPredict['varType'] + ' or ' + each_predictResult['varType'][0:len(each_predictResult['varType'])-1]

                                        #print(eachIsInPredict['varType'] + '*')
                                if isfind == 0:
                                    varPredictResult.append({'varName': Right,
                                                             'varType': each_predictResult['varType'][0:len(each_predictResult['varType']) - 1],
                                                             'varOffset': ''})
                            for eachA in arrayPointerList:  # 整合数组
                                if eachA == Left and Right==each_predictResult['varName']:
                                        if '*' not in each_predictResult['varType']:
                                            each_predictResult['varType'] =each_predictResult['varType']+'[]'

                #最后再整合varPredictresult中的数组,顺便去掉void*改成*，同时argc和argv强定义
                for each in varPredictResult:
                    if '+' not in each['varName']:
                        isprint = 0
                        for e in varPredictResult:
                            if re.search(each['varName']+'\+[a-z]+' , e['varName']):#如果a+reg*4这种明显的寄存器乘法，直接改数组
                                if '[]' not in each['varType']:
                                     each['varType'] = e['varType']+'[]'
                                else:
                                    if each['varType'] == e['varType']+'[]':
                                        pass
                                    else:
                                        each['varType'] == each['varType'] + ' or ' + e['varType'] + '[]'
                            elif re.search(each['varName'] + '\+\d+', e['varName']):  # 如果a+4这种如果类型一样就改成数组，此处先统一该成结构
                                if each['varType'] == 'bool':
                                    each['varType'] = 'char'
                                if isprint == 0:
                                    if printre != 0:
                                        structTypeOutput.append('struct: ' + each['varName']+'\n')
                                        structTypeOutput.append('\toffset: ' + "{:<15}".format(each['varOffset']) + '\t\t' + each['varType'] + '\n')
                                        #print('struct:',each['varName'])
                                        #print('\toffset:', "{:<15}".format(each['varOffset']), '\t\t', each['varType'])
                                    isprint = 1
                                    if '[]' not in each['varType']:
                                        each['varType'] = each['varType'] + ' (struct)'
                                if printre != 0:
                                    structTypeOutput.append('\toffset: ' + "{:<15}".format(e['varOffset']) + '\t\t' + e['varType'] + '\n')
                                    #print('\toffset:', "{:<15}".format(e['varOffset']), '\t\t', e['varType'])
                    if 'void' in each['varType']:
                        each['varType'] = each['varType'].replace('void','')
                    if re.search('\w:(argv|envp)$',each['varName']):
                        each['varType'] = 'char**'
                    elif re.search('\w:argc$',each['varName']):
                        each['varType'] = 'int'

                File_To_Vector.PredictResult = []
                File_To_Vector.PointerResult = []
                File_To_Vector.PredictResult = copy.deepcopy(varPredictResult)
                File_To_Vector.PointerResult = copy.deepcopy(varPointerResult)
            #######################################以上为predict函数定义

            #预测完后，有新的信息要整合
            def flashNewInfo(File_To_Vector , PredictResult):
                newFPList = []
                for eachFAP in File_To_Vector.FuncAndPara:
                    for eachvar in PredictResult:
                        if eachFAP['Name'] == eachvar['varName'] and 'or' not in eachvar['varType']:
                            newFPList.append({'funcPara': eachFAP['ParaNum'], 'paraType': eachvar['varType']})

                ParaTypeSave = []  # 参数一致性，后面对于正确预测的指针，直接用，具体到更详细的类型

                for eachC in File_To_Vector.CallParaSet:
                    left, right = eachC.split('---', 1)
                    for each in newFPList:
                        if right == each['funcPara'] or right == '_' + each['funcPara']:
                            #print(left,each['paraType'])
                            if '*' in each['paraType']:
                                File_To_Vector.updateVector(left, 'FPptr', 0.45)
                                if '*' == each['paraType']:
                                    break
                            File_To_Vector.updateVector(left, 'FP' + re.sub('[^a-zA-Z]', '', each['paraType']), 0.08)
                            ParaTypeSave.append({'Para': left, 'Type': each['paraType']})  # 下一个for要用

                # 参数于压栈变量的相同性，这里只作用于第二次预测之后，预测成*的变量，详细的指针类型根据这个一致性，对PointerDetai中已经预测的是没有影响的
                for each in PredictResult:
                    if each['varType'] == '*':
                        for eachPT in ParaTypeSave:
                            if eachPT['Para'] == each['varName'] and '*' in eachPT['Type']:
                                each['varType'] = eachPT['Type']
                for each in PredictResult:
                    if each['varType'] == '*':
                        for vector,name in zip(File_To_Vector.Vector_list,File_To_Vector.Name_list):
                            if name == each['varName']:
                                saveweight = 0
                                saveT = ''
                                for eachweight,eachinstruction in zip(vector,File_To_Vector.Instructions_list):
                                    if 'FP' in eachinstruction and eachweight > saveweight and eachinstruction!='FPptr':
                                        saveT = eachinstruction.replace('FP' , '')
                                        saveweight = eachweight
                                    elif eachweight!=0 and eachinstruction =='FPptr':
                                        each['varType'] = saveT + '*'
                    each['varType'] = each['varType'].replace('FILE','')
                File_To_Vector.UpdateUDrelation()


            # 输出函数
            def printPredict(PredictResult, globalPredictResult, solve=0):
                print('**********************************************************************')
                print(home, end=':\n')
                print('')
                for each in PredictResult:
                    if solve == 0:
                        print("{:<45}".format(each['varName']), end="")
                        print("{:<10}".format(each['varOffset']), end="")
                        print('\t\t', end="")
                        print(each['varType'])
                    else:
                        if '+' not in each['varName']:
                            print("{:<45}".format(each['varName']), end="")
                            print("{:<10}".format(each['varOffset']), end="")
                            print('\t\t', end="")
                            print(each['varType'])

                if File_To_Vector != []:
                    print('\nPoint to analysis:')
                    for each in File_To_Vector.LEArelation:
                        print('\t' + each)

                if globalPredictResult != []:
                    print("\nglobal variables:")
                    for each in globalPredictResult:
                        print("{:<45}".format("\t" + each['varName']), end="")
                        print('\t\t', end="")
                        print(each['varType'])

                print('')
                print('@ @ @ end @ @ @')
                print('**********************************************************************')
                print('')


            def outputFile(FileName,solve=0):
                outputList = []
                outputList.append('**********************************************************************\n')
                outputList.append(home + ':\n')
                outputList.append('\n')
                for each in PredictResult:
                    if solve == 0:
                        outputList.append("{:<45}".format(each['varName']) + '\t' + "{:<10}".format(each['varOffset']) + '\t\t' + each['varType'] + '\n')
                    else:
                        if '+' not in each['varName']:
                            outputList.append("{:<45}".format(each['varName']) + '\t' + "{:<10}".format(each['varOffset']) + '\t\t' + each['varType'] + '\n')

                if globalPredictResult != []:
                    outputList.append("\nglobal variables:\n")
                    for each in globalPredictResult:
                        outputList.append("{:<45}".format("\t" + each['varName']) + '\t\t' + each['varType'] + '\n')

                outputList.append('\n')
                outputList.append('@ @ @ end @ @ @\n')
                outputList.append('**********************************************************************\n')
                outputList.append('\n')

                with open(home + '/' + str(FileName), 'w', encoding='utf-8') as output:
                    for each in structTypeOutput:
                        output.write(each)
                    for each in outputList:
                        output.write(each)

            def AddProgramTypeInfo(PredictResult, globalPredictResult, file):
                vector_ele = [0]*len(Type_list)
                for each in PredictResult:
                    if '*' in each['varType']:
                        varType = 'ptr'
                    else:
                        varType = each['varType']

                    for i in range(0,len(Type_list)):
                        if Type_list[i] == varType:
                            vector_ele[i] = vector_ele[i] + 1
                            continue

                with open(file,'a',encoding='utf-8') as programTypeInfoFile:
                    print("{:<35}".format(homeName),vector_ele,file=programTypeInfoFile)


            #end = time.clock()#计算时间
            #totalTime = totalTime + (end - start)
            #print('pre time:', end - start)

            #start2 = time.clock()  # 计算时间


            # -----------------------------------------------------
            # 全局变量的预测
            File_To_Vector.mergeGlobalVar()
            globaldata = copy.deepcopy(File_To_Vector.globalVarVector)
            globallabel = copy.deepcopy(File_To_Vector.globalVarLabel)
            TFIDFNormalization(globaldata, 7)

            globalPredictResult = []
            if globaldata != []:

                # 将globaldata中的数据放给X_test_g
                X_test_g = np.zeros((len(globaldata), len(globaldata[0])))
                for i in range(0, len(globaldata)):
                    for j in range(0, len(globaldata[0])):
                        X_test_g[i][j] = globaldata[i][j]
                X_test_g = np.log(X_test_g + 1)
                X_test_g = min_max_scaler.transform(X_test_g)
                globalPredictLabel_np = clf.predict(X_test_g)

                # 将clf.predict(X_test)之后的数据存回列表的形式
                globalPredictLabel = []
                for i in range(0, len(globalPredictLabel_np)):
                    globalPredictLabel.append(globalPredictLabel_np[i])

                #globalPredictLabel, accuracy, value = svm_predict(globallabel, globaldata, model, '-q')
                for each_var, each_predictlabel in zip(File_To_Vector.globalVarName, globalPredictLabel):
                    globalPredictResult.append({'varName': each_var,
                                                'varType': Type_list[int(each_predictlabel)],
                                                'varOffset': 'global'})

            # -----------------------------------------------------
            # 首次预测
            data = copy.deepcopy(File_To_Vector.Vector_list)
            label = copy.deepcopy(File_To_Vector.Label_list)
            TFIDFNormalization(data, 7)
            TFIDFNormalization(File_To_Vector.pointer_vector_list, 7)
            # Z_ScoreNormalization(data,5)#向量-1~1归一化处理
            # MaxMinNormalization(data,0)#向量zscore归一化处理

            Predict(File_To_Vector, data, label)
            flashNewInfo(File_To_Vector , File_To_Vector.PredictResult)
            File_To_Vector.UpdateUDrelation()
            PredictResult = File_To_Vector.PredictResult

            #printPredict(PredictResult, globalPredictResult)
            # -----------------------------------------------------


            # -----------------------------------------------------
            # 第二次预测
            data = copy.deepcopy(File_To_Vector.Vector_list)
            label = copy.deepcopy(File_To_Vector.Label_list)
            TFIDFNormalization(data, 7)
            # Z_ScoreNormalization(data,5)#向量-1~1归一化处理
            # MaxMinNormalization(data,0)#向量zscore归一化处理

            Predict(File_To_Vector, data, label,1)
            flashNewInfo(File_To_Vector, File_To_Vector.PredictResult)
            File_To_Vector.UpdateUDrelation()
            PredictResult = File_To_Vector.PredictResult

            #printPredict(PredictResult, globalPredictResult, 1)
            outputFile('BITY_output',1)
            # -----------------------------------------------------
            print("\t" + "{:<35}".format(home) + ' Finished')


            #end2 = time.clock()  # 计算时间
            #totalTime = totalTime + (end2 - start2)
            #print('predict time:', end2 - start2)

            #AddProgramTypeInfo(PredictResult, globalPredictResult ,'SaveData/benign_TYPE_info.txt')
            #AddProgramTypeInfo(PredictResult, globalPredictResult, 'SaveData/malware_TYPE_info.txt')


print('\t(All finish)\t')
