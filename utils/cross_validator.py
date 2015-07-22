#!/usr/bin/env python3
__author__ = 'mars'

import sys,subprocess,os,re
from csv import DictReader

if len(sys.argv) != 3:
    print('wrong arg in cross_validator')
    exit(1)

FOLD,SOLUTION=sys.argv[1:]
FOLD=int(FOLD)
results_path='output/results/batch/'+SOLUTION+'/'
data_path='output/cross_validation_split/'



#建立目录

if not os.path.exists(results_path):
    for i in range(FOLD):
        os.makedirs(results_path+'split_{0}/'.format(i))



#测试
for i in range(FOLD):
    print('running '+SOLUTION+', round: '+str(i))
    cmd='python {solution} {data} {results}'.format(solution=SOLUTION,data=data_path+'split_{0}/'.format(i),results=results_path+'split_{0}/'.format(i))
    p=subprocess.call(cmd,shell=True,stdout=subprocess.PIPE)
    cmd='python utils/evaluate.py {data} {result}'.format(data=data_path+'split_{0}/'.format(i),result=results_path+'split_{0}/'.format(i))
    p=subprocess.call(cmd,shell=True,stdout=sys.stderr)




#分折结果汇总输出
logloss=0.
auc=0.

auc_pattern='auc: ([0-9.e]+)'
logloss_pattern='logloss: ([0-9.e]+)'

for i in range(FOLD):
    info=''
    read=open(results_path+'split_{0}/details.txt'.format(i))
    for line in read.readlines():
        info+=line
    auc+=float(re.search(auc_pattern,info).group(1))
    logloss+=float(re.search(logloss_pattern,info).group(1))
    read.close()

logloss/=FOLD
auc/=FOLD

result=open(results_path+'{0}.txt'.format(SOLUTION.split('/')),'w')
result.write('Average logloss:{0}\nAverage AUC:{1}'.format(logloss,auc))
result.close()