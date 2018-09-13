import os
from sklearn import metrics
from sklearn.metrics import roc_curve, auc
from sklearn.externals import joblib
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

print("\n")

### CV Report ###
# 分类报告：precision/recall/fi-score/均值/分类个数

##  1  ##
Y = joblib.load("SaveData/D_CVML_result/KNN1_Y.save")
KNN1pred = joblib.load("SaveData/D_CVML_result/KNN1_pred.save")
KNN1prob = joblib.load("SaveData/D_CVML_result/KNN1_prob.save")

y_true = Y
y_pred = KNN1pred
print('******************** KNN1 ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('Precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('Recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print('\n')

##  2  ##
Y = joblib.load("SaveData/D_CVML_result/KNN3_Y.save")
KNN3pred = joblib.load("SaveData/D_CVML_result/KNN3_pred.save")
KNN3prob = joblib.load("SaveData/D_CVML_result/KNN3_prob.save")

y_true = Y
y_pred = KNN3pred
print('******************** KNN3 ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print('\n')

##  3  ##
Y = joblib.load("SaveData/D_CVML_result/KNN5_Y.save")
KNN5pred = joblib.load("SaveData/D_CVML_result/KNN5_pred.save")
KNN5prob = joblib.load("SaveData/D_CVML_result/KNN5_prob.save")

y_true = Y
y_pred = KNN5pred
print('******************** KNN5 ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print('\n')

##  4  ##
Y = joblib.load("SaveData/D_CVML_result/KNN7_Y.save")
KNN7pred = joblib.load("SaveData/D_CVML_result/KNN7_pred.save")
KNN7prob = joblib.load("SaveData/D_CVML_result/KNN7_prob.save")

y_true = Y
y_pred = KNN7pred
print('******************** KNN7 ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print('\n')

##  5  ##
Y = joblib.load("SaveData/D_CVML_result/DTgini_Y.save")
DTginipred = joblib.load("SaveData/D_CVML_result/DTgini_pred.save")
DTginiprob = joblib.load("SaveData/D_CVML_result/DTgini_prob.save")

y_true = Y
y_pred = DTginipred
print('******************** DTgini ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print('\n')

##  6  ##
Y = joblib.load("SaveData/D_CVML_result/DTentropy_Y.save")
DTentropypred = joblib.load("SaveData/D_CVML_result/DTentropy_pred.save")
DTentropyprob = joblib.load("SaveData/D_CVML_result/DTentropy_prob.save")

y_true = Y
y_pred = DTentropypred
print('******************** DTentropy ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print('\n')

##  7  ##
Y = joblib.load("SaveData/D_CVML_result/RFgini_Y.save")
RFginipred = joblib.load("SaveData/D_CVML_result/RFgini_pred.save")
RFginiprob = joblib.load("SaveData/D_CVML_result/RFgini_prob.save")

y_true = Y
y_pred = RFginipred
print('******************** RFgini ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print('\n')

##  8  ##
Y = joblib.load("SaveData/D_CVML_result/RFentropy_Y.save")
RFentropypred = joblib.load("SaveData/D_CVML_result/RFentropy_pred.save")
RFentropyprob = joblib.load("SaveData/D_CVML_result/RFentropy_prob.save")

y_true = Y
y_pred = RFentropypred
print('******************** RFentropy ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print('\n')

##  9  ##
Y = joblib.load("SaveData/D_CVML_result/SVMlinear_Y.save")
SVMlinearpred = joblib.load("SaveData/D_CVML_result/SVMlinear_pred.save")
SVMlinearprob = joblib.load("SaveData/D_CVML_result/SVMlinear_prob.save")

y_true = Y
y_pred = SVMlinearpred
print('******************** SVClinear ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print('\n')

##  10  ##
Y = joblib.load("SaveData/D_CVML_result/SVMrbf_Y.save")
SVMrbfpred = joblib.load("SaveData/D_CVML_result/SVMrbf_pred.save")
SVMrbfprob = joblib.load("SaveData/D_CVML_result/SVMrbf_prob.save")

y_true = Y
y_pred = SVMrbfpred
print('******************** SVCrbf ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print('\n')

##  11  ##
Y = joblib.load("SaveData/D_CVML_result/SVMsigmoid_Y.save")
SVMsigmoidpred = joblib.load("SaveData/D_CVML_result/SVMsigmoid_pred.save")
SVMsigmoidprob = joblib.load("SaveData/D_CVML_result/SVMsigmoid_prob.save")

y_true = Y
y_pred = SVMsigmoidpred
print('******************** SVCsigmoid ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print('\n')

##  12  ##
Y = joblib.load("SaveData/D_CVML_result/GaussianNB_Y.save")
GaussianNBpred = joblib.load("SaveData/D_CVML_result/GaussianNB_pred.save")
GaussianNBprob = joblib.load("SaveData/D_CVML_result/GaussianNB_prob.save")

y_true = Y
y_pred = GaussianNBpred
print('******************** GaussianNB ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print('\n')

##  13  ##
Y = joblib.load("SaveData/D_CVML_result/MultinomialNB_Y.save")
MultinomialNBpred = joblib.load("SaveData/D_CVML_result/MultinomialNB_pred.save")
MultinomialNBprob = joblib.load("SaveData/D_CVML_result/MultinomialNB_prob.save")

y_true = Y
y_pred = MultinomialNBpred
print('******************** MultinomialNB ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print('\n')

##  14  ##
Y = joblib.load("SaveData/D_CVML_result/BernoulliNB_Y.save")
BernoulliNBpred = joblib.load("SaveData/D_CVML_result/BernoulliNB_pred.save")
BernoulliNBprob = joblib.load("SaveData/D_CVML_result/BernoulliNB_prob.save")

y_true = Y
y_pred = BernoulliNBpred
print('******************** BernoulliNB ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print('\n')

##  15  ##
Y = joblib.load("SaveData/D_CVML_result/SGD_Y.save")
SGDpred = joblib.load("SaveData/D_CVML_result/SGD_pred.save")
SGDprob = joblib.load("SaveData/D_CVML_result/SGD_prob.save")

y_true = Y
y_pred = SGDpred
print('******************** SGD ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print("\n")


### Test Report ###
# 分类报告：precision/recall/fi-score/均值/分类个数
"""
##  1  ##
Y = joblib.load("SaveData/D_ML_result/KNN1_Y.save")
KNN1pred = joblib.load("SaveData/D_ML_result/KNN1_pred.save")
KNN1prob = joblib.load("SaveData/D_ML_result/KNN1_prob.save")

y_true = Y
y_pred = KNN1pred
print('******************** KNN1 ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('Precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('Recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print('\n')

##  2  ##
Y = joblib.load("SaveData/D_ML_result/KNN3_Y.save")
KNN3pred = joblib.load("SaveData/D_ML_result/KNN3_pred.save")
KNN3prob = joblib.load("SaveData/D_ML_result/KNN3_prob.save")

y_true = Y
y_pred = KNN3pred
print('******************** KNN3 ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print('\n')

##  3  ##
Y = joblib.load("SaveData/D_ML_result/KNN5_Y.save")
KNN5pred = joblib.load("SaveData/D_ML_result/KNN5_pred.save")
KNN5prob = joblib.load("SaveData/D_ML_result/KNN5_prob.save")

y_true = Y
y_pred = KNN5pred
print('******************** KNN5 ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print('\n')

##  4  ##
Y = joblib.load("SaveData/D_ML_result/KNN7_Y.save")
KNN7pred = joblib.load("SaveData/D_ML_result/KNN7_pred.save")
KNN7prob = joblib.load("SaveData/D_ML_result/KNN7_prob.save")

y_true = Y
y_pred = KNN7pred
print('******************** KNN7 ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print('\n')

##  5  ##
Y = joblib.load("SaveData/D_ML_result/DTgini_Y.save")
DTginipred = joblib.load("SaveData/D_ML_result/DTgini_pred.save")
DTginiprob = joblib.load("SaveData/D_ML_result/DTgini_prob.save")

y_true = Y
y_pred = DTginipred
print('******************** DTgini ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print('\n')

##  6  ##
Y = joblib.load("SaveData/D_ML_result/DTentropy_Y.save")
DTentropypred = joblib.load("SaveData/D_ML_result/DTentropy_pred.save")
DTentropyprob = joblib.load("SaveData/D_ML_result/DTentropy_prob.save")

y_true = Y
y_pred = DTentropypred
print('******************** DTentropy ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print('\n')

##  7  ##
Y = joblib.load("SaveData/D_ML_result/RFgini_Y.save")
RFginipred = joblib.load("SaveData/D_ML_result/RFgini_pred.save")
RFginiprob = joblib.load("SaveData/D_ML_result/RFgini_prob.save")

y_true = Y
y_pred = RFginipred
print('******************** RFgini ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print('\n')

##  8  ##
Y = joblib.load("SaveData/D_ML_result/RFentropy_Y.save")
RFentropypred = joblib.load("SaveData/D_ML_result/RFentropy_pred.save")
RFentropyprob = joblib.load("SaveData/D_ML_result/RFentropy_prob.save")

y_true = Y
y_pred = RFentropypred
print('******************** RFentropy ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print('\n')

##  9  ##
Y = joblib.load("SaveData/D_ML_result/SVMlinear_Y.save")
SVMlinearpred = joblib.load("SaveData/D_ML_result/SVMlinear_pred.save")
SVMlinearprob = joblib.load("SaveData/D_ML_result/SVMlinear_prob.save")

y_true = Y
y_pred = SVMlinearpred
print('******************** SVClinear ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print('\n')

##  10  ##
Y = joblib.load("SaveData/D_ML_result/SVMrbf_Y.save")
SVMrbfpred = joblib.load("SaveData/D_ML_result/SVMrbf_pred.save")
SVMrbfprob = joblib.load("SaveData/D_ML_result/SVMrbf_prob.save")

y_true = Y
y_pred = SVMrbfpred
print('******************** SVCrbf ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print('\n')

##  11  ##
Y = joblib.load("SaveData/D_ML_result/SVMsigmoid_Y.save")
SVMsigmoidpred = joblib.load("SaveData/D_ML_result/SVMsigmoid_pred.save")
SVMsigmoidprob = joblib.load("SaveData/D_ML_result/SVMsigmoid_prob.save")

y_true = Y
y_pred = SVMsigmoidpred
print('******************** SVCsigmoid ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print('\n')

##  12  ##
Y = joblib.load("SaveData/D_ML_result/GaussianNB_Y.save")
GaussianNBpred = joblib.load("SaveData/D_ML_result/GaussianNB_pred.save")
GaussianNBprob = joblib.load("SaveData/D_ML_result/GaussianNB_prob.save")

y_true = Y
y_pred = GaussianNBpred
print('******************** GaussianNB ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print('\n')

##  13  ##
Y = joblib.load("SaveData/D_ML_result/MultinomialNB_Y.save")
MultinomialNBpred = joblib.load("SaveData/D_ML_result/MultinomialNB_pred.save")
MultinomialNBprob = joblib.load("SaveData/D_ML_result/MultinomialNB_prob.save")

y_true = Y
y_pred = MultinomialNBpred
print('******************** MultinomialNB ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print('\n')

##  14  ##
Y = joblib.load("SaveData/D_ML_result/BernoulliNB_Y.save")
BernoulliNBpred = joblib.load("SaveData/D_ML_result/BernoulliNB_pred.save")
BernoulliNBprob = joblib.load("SaveData/D_ML_result/BernoulliNB_prob.save")

y_true = Y
y_pred = BernoulliNBpred
print('******************** BernoulliNB ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print('\n')

##  15  ##
Y = joblib.load("SaveData/D_ML_result/SGD_Y.save")
SGDpred = joblib.load("SaveData/D_ML_result/SGD_pred.save")
SGDprob = joblib.load("SaveData/D_ML_result/SGD_prob.save")

y_true = Y
y_pred = SGDpred
print('******************** SGD ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print("\n")

##  16  ##
Y = joblib.load("SaveData/D_ML_result/LIBSVM_Y.save")
LIBSVMpred = joblib.load("SaveData/D_ML_result/LIBSVM_pred.save")

y_true = Y
y_pred = LIBSVMpred
print('******************** SGD ********************')
print(classification_report(y_true, y_pred))
print('Accuracy =', accuracy_score(y_true, y_pred))
print('precision =', metrics.precision_score(y_true, y_pred, average='weighted'))
print('recall = ', metrics.recall_score(y_true, y_pred, average='weighted'))
print('F1 = ', metrics.f1_score(y_true, y_pred, average='weighted'))
print('**********************************************')
print("\n")
"""