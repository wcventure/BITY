# README #

IDA
http://pan.baidu.com/s/1bp7rOpp


BITY项目组成说明：
asmFile				从IDA中得到.asm文件，放到该文件夹中
TestData			执行SplitIDAasm.py后，经过分割的.asm文件即可用于分析（分析样本）
TrainData			一些训练样本
SaveData			无须理会，存放程序需要的一些中间文件
FileToVector.py			将一个汇编代码文件中的每个变量用一个向量的形式表示
Train_SVM_Model.py		训练SVM模型
SplitIDAasm.py			分割asmFile中的.asm文件
Predict_SVM_Model.py		分析TestData中的数据
Sketchy_Predict_SVM_Model.py	不用管
svm.py				LibSVM工具包
svmutil.py			LibSVM工具包
libsvm.dll			LibSVM动态库
libsvm.so.2			LibSVM动态库
Normalization.py		归一化程序
TransformDwarfFile.py		提取DwarfFile中的debug信息
TransformExplorerFile.py	可将https://gcc.godbolt.org/上经过x86 CL 19 RC编译的二进制码转为BITY可接受的文件
GUI_Predict.py			一个简单的图形界面的输入，保存代码，点击预测按钮进行预测
