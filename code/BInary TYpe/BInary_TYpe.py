import os
import time

#os.system("TransformDwarfFile.py")
#start = time.clock()  # 计算时间
#os.system("SplitIDAasm.py")
#end = time.clock()  # 计算时间
#totalTime = end - start
#print('split time:', end - start)
####################################################################
#os.system("Train_SVM_Model.py")
#os.system("Train_SLM_Model.py")
#os.system("Train_Sklearn_Model.py")
#os.system("Sketchy_Predict_SVM_Model.py")
#os.system("Sketchy_Predict_SLM_Model.py")
#os.system("Sketchy_Predict_Sklearn_Model.py")
#os.system("Predict_SVM_Model.py")
#os.system("Predict_SLM_Model.py")
#os.system("Predict_RF_Model.py")
####################################################################
#os.system("malwareDetect.py")
#os.system("Display_F1score.py")
os.system("GUI_Predict.py")

"""
#获取某文件夹下各个文件名的列表
path = 'D:/'
for i in os.walk(path):
    for each in i[2]:
        print('@' + each + '&')
"""


