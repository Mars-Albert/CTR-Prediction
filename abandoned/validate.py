__author__ = 'mars'
import os, sys
import scipy as sp
from csv import DictReader,DictWriter
from sklearn.metrics import roc_auc_score
from sklearn.metrics import log_loss
if len(sys.argv) != 2:
    print('wrong arg')
    exit(1)

path=sys.argv[1]
label_path=path+'validation.csv'
predict_path=path+'submission.csv'
result_path=path+'detail.txt'

def llfun(act, pred):
    epsilon = 1e-15
    pred = sp.maximum(epsilon, pred)
    pred = sp.minimum(1-epsilon, pred)
    ll =act*sp.log(pred) + sp.subtract(1,act)*sp.log(sp.subtract(1,pred))
#    ll = ll * -1.0/len(act)
    return ll





label_reader=DictReader(open(label_path))
predict_reader=DictReader(open(predict_path))
result=open(result_path, 'w')

count=0

label={}
predict={}
total=0.0
tmp=0.0

positive=0
negative=0
true_positive=0
false_positive=0
true=0

actual=0.0
predicted=0.0

y_true=[]
y_scores=[]
AUC=0.0

for t,row in enumerate(label_reader):
#    if(count<10):
        label=row
        predict=predict_reader.__next__()
        actual=float(label['Label'])
        predicted=float(predict['Predicted'])
        y_true.append(actual)
        y_scores.append(predicted)

        if(predicted>=0.5):
            if(actual==0):
                false_positive+=1
                negative+=1
 #               print('FP')
            else:
                true_positive+=1
                true+=1
                positive+=1
  #              print('TP')
        else:
            if(actual==0):
                true+=1
                negative+=1
      #          print('TN')
            else:
    #           print('FN')
               positive+=1


        tmp=llfun(actual,predicted)

        total+=tmp
#        print('actual: ',label['Label'],' predicted: ',predict['Predicted'],' loss: ',tmp)
#        if(count%10000==0):print(count,' compared!')

        count+=1


AUC=roc_auc_score(y_true,y_scores)
log_loss2=log_loss(y_true,y_scores)



result.write('------------------------------------------------------\n')
result.write('Total instances: {count} Validation File: {vafile} Prediction File: {prefile}\n'.format(count=count,vafile=label_path,prefile=predict_path))
result.write('Confusion Matrix:\n')
result.write('\  1     0       <---predicted\n')
result.write('1 {tp} {fn}\n'.format(tp=true_positive,fn=positive-true_positive))
result.write('0 {fp} {tn}\n'.format(fp=false_positive,tn=true-true_positive))
result.write('^-----------------------actual                 \n')

precision=float(true_positive)/(true_positive+false_positive)
recall=float(true_positive)/(positive)
result.write('Correctness: {0} Precision: {1} Recall: {2} F1-Measure: {3}\n'.format(float(true)/count,precision,recall,2*precision*recall/(precision+recall)))
result.write('logloss: {0} log_loss2 {1} AUC: {2}\n'.format(total* -1.0/float(count),log_loss2,AUC))
result.write('------------------------------------------------------')
result.close()

statistics=open(path+'result.csv','w')
statistics.writelines('Correctness,Precision,Recall,F1-Measure,Logloss,AUC\n')
statistics.writelines('{0},{1},{2},{3},{4},{5}'.format(float(true)/count,precision,recall,2*precision*recall/(precision+recall),total* -1.0/float(count),AUC))
statistics.close()