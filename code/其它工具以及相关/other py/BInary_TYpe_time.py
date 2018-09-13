import os
import time


def alocCount():
    #os.system("Train_SVM_Model.py")
    #os.system("Sketchy_Predict_SVM_Model.py")
    #os.system("Predict_SVM_Model.py")
    ####################################################################
    #os.system("TransformDwarfFile.py")
    #os.system("SplitIDAasm.py")
    #os.system("Predict_SVM_Model.py")
    #os.system("GUIPredict_SVM_Model.py")
    ####################################################################
    #os.system("GUI_Predict.py")
    pass

totalTime = 0
for i in range(0,5):
    start = time.clock()
    ###process
    alocCount()
    ###prosess
    end = time.clock()

    totalTime = totalTime + (end - start)
    print (str(i+1)+'th time:',end - start)
    
averageTime = totalTime/5
print('average time:',averageTime)


"""
#获取某文件夹下各个文件名的列表
path = 'D:/coreutils-o'
for i in os.walk(path):
    for each in i[2]:
        print(each,end='')
"""
