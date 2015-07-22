__author__ = 'mars'

import sys
from csv import DictReader
from sklearn.metrics import roc_auc_score
from sklearn.metrics import log_loss
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix


if len(sys.argv) != 3:
    print('wrong arg')
    exit(1)

data_path=sys.argv[1]
result_path=sys.argv[2]

label_path=data_path+'validation.csv'
predict_path=result_path+'submission.csv'
result_path=result_path+'details.txt'



label_reader=DictReader(open(label_path))
predict_reader=DictReader(open(predict_path))


count=0

actual=0.0
predicted=0.0

y_true=[]
y_scores=[]
y_pred=[]
AUC=0.0

for t,row in enumerate(label_reader):
        predict=predict_reader.__next__()
        actual=float(row['Label'])
        predicted=float(predict['Predicted'])

        y_true.append(actual)
        y_scores.append(predicted)
        if(predicted>0.5):
            y_pred.append(1)
        else:
            y_pred.append(0)
        count+=1

#已发现异常：ValueError: Only one class present in y_true. ROC AUC score is not defined in that case.
# 当数据量太小只有一种类标号时会报此错误

AUC=roc_auc_score(y_true,y_scores)
logloss=log_loss(y_true,y_scores)
accuracy=accuracy_score(y_true,y_pred)
precision=precision_score(y_true,y_pred)
recall=recall_score(y_true,y_pred)
f1=f1_score(y_true,y_pred)
confusion_matrix=confusion_matrix(y_true,y_pred)


result=open(result_path, 'w')

result.write('------------------------------------------------------\n')
result.write('Total instances: {count}\nValidation File: {vafile} Prediction File: {prefile}\n'.format(count=count,vafile=label_path,prefile=predict_path))
##result.write('confusion matrix:\n')


result.write('Accuracy: {0} Precision: {1} Recall: {2} F1-Measure: {3}\n'.format(accuracy,precision,recall,f1))
result.write('logloss: {0} auc: {1}\n'.format(logloss,AUC))
result.write('------------------------------------------------------')
result.close()
print('logloss: {0} auc: {1}'.format(logloss,AUC))



'''
statistics=open(result_path+'result.csv','w')
statistics.writelines('Accuracy,Precision,Recall,F1-Measure,Logloss,AUC\n')
statistics.writelines('{0},{1},{2},{3},{4},{5}'.format(accuracy,precision,recall,f1,logloss,AUC))
statistics.close()
'''

