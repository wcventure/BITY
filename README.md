# README #

[Xu Z, Wen C, Qin S. Learning Types for Binaries[C]. International Conference on Formal Engineering Methods. Springer, Cham, 2017:430-446.](http://csse.szu.edu.cn/staff/xuzw/paper/icfem2017.pdf)

## What is this repository for? ###

* Recover the type information from Binary via machine learning

## Abstract

Recovering type information in binary code is a great challenging problem due partly to the fact that much type-related information has been lost during the compilation from high-level source code. However, recovering type information in binary code helps a lot in comprehension and analysis of binary code. And it is required, or significantly benefits, many applications, such as decompilation, reverse engineering, vulnerabilities analysis and malware detection. Therefore, the research of the binary code type recovery has great practical significance.

Currently, most of the existing research on binary code type recovery tend to resort to program analysis techniques, which can be too conservative to infer types with high accuracy or too heavyweight to be viable in practice. In this paper, we propose a new approach to recovering type information for recovered variables in binary code, which is more precise and more efficient.

First, we present our approach to recovering type information in binary code. The idea is motivated by “duck typing”, where the type of a variable is determined by its features and properties. Our approach uses a combination of machine learning and program analysis. In detail, we first extract critical information form instruction-flow and data-flow, namely behaviors and features of variables in binary code. According to these behaviors and features, we learn a classifier with basic types as levels, using various machine learning methods, and then use this classifier to predict types for new, unseen binaries. For composite types, such as pointer and struct, we perform a point-to analysis to recover the target variables and use the classifier to recover the base type for these target variables, base on which, composite types are recovered.

Second, we also apply the type recovery technology of binary code to malware detection. Our malware detecting approach is based on classifier. Different from most existing work, we take into account not only the behavior information but also the data information. As far as we know, our approach is the first one to consider data types as features for malware detection.

At last, we have implemented our approach in a tool called BITY and used it to conduct a series of experiments to evaluate our approach. The results show that (1) our approach can precisely recover the type information in binary code; (2) our tool is more precise than the commercial tool Hey-Rays and the open source tool Snowman, both in terms of correct types and compatible types; (3) our prototype BITY is efficient and scalable, which is suitable in practice; (4) the type information we recover is capable of detecting malware.

## How do I get set up? ###

* Git clone this repository
* Configuration. (If you are in Windows platfrom, please copy the "libsvm.dll" into the folder "C://Windows")
* Unpack all compressed packets
* Explain the usage of each document.
  
    - asmFile:				        从IDA中得到.asm文件，放到该文件夹中
    - TestData:			            执行SplitIDAasm.py后，经过分割的.asm文件即可用于分析（分析样本）
    - TrainData:			        一些训练样本
    - SaveData：			        无须理会，存放程序需要的一些中间文件
    - FileToVector.py：		        将一个汇编代码文件中的每个变量用一个向量的形式表示
    - Train_SVM_Model.py：	        训练SVM模型
    - SplitIDAasm.py：		        分割asmFile中的.asm文件
    - Predict_SVM_Model.py：		分析TestData中的数据
    - Sketchy_Predict_SVM_Model.py：不用管
    - svm.py：				        LibSVM工具包
    - svmutil.py：			        LibSVM工具包
    - libsvm.dll：			        LibSVM动态库
    - libsvm.so.2：			        LibSVM动态库
    - Normalization.py：		    归一化程序
    - TransformDwarfFile.py：		提取DwarfFile中的debug信息
    - GUI_Predict.py：			    一个简单的图形界面的输入，保存代码，点击预测按钮进行预测
    - TransformExplorerFile.py：	可将https://gcc.godbolt.org/上经过x86 CL 19 RC编译的二进制码转为BITY可接受的文件
    
## Contribution guidelines ###

* An approach to learning types for binary code, using a combination of machine learning and program analysis, is proposed.
* A series of experiments are conducted to evaluate our approach, which demonstrated that our approach is able to learn more precise types, with reasonable performance, and can help detect malware.

## Who do I talk to? ###

* wcventure@126.com