__author__ = 'mars'

import re,subprocess,sys



'''
def get_loss( output ):
    pattern = re.compile('logloss: ([0-9.e]+)')
    m = re.search( pattern, output)
    loss = m.group( 1 )
    return loss


read=open('/home/mars/wenjian')
info=''
for line in read.readlines():
    info+=line







print(info)

print(float(get_loss(info)))

read=open('/home/mars/wenjian')


write=open('/home/mars/wenjian123123213','w')
for i,line in enumerate(read,start=1):
    write.write(line)

write.close()
read=open('/home/mars/wenjian')
read1=open('/home/mars/wenjian123123213')
for a,b in zip(read,read1):
    print(a)


abc='C123'

print(abc.split('C')[1])




a='1'


print(chr(ord(a)+1+16))
'''


import xgboost as xgb
import numpy as np
data =np.random.rand(20,10)
label=np.random.randint(2,size=20)
dtrain= xgb.DMatrix(data,label)


#print(data)
#print(label)

param = {'bst:max_depth':5, 'bst:eta':1, 'silent':0, 'objective':'binary:logistic','eval_metric':'logloss' }
param['nthread'] = 4
plst = param.items()
print(plst)


dtest = xgb.DMatrix(np.random.rand(10,10),np.random.randint(2,size=10))

evallist  = [(dtrain,'train'),(dtest,'test'),]


num_round = 10
bst = xgb.train( plst, dtrain, num_round, evallist )
preds=bst.predict(dtest)

for pr in preds:
    print(pr)



test=[['a',0,1],['b',2,5],['c',2,9],['d',7,3]]


for (a,b,c) in sorted(test,key=lambda x: x[1]):
    print(a,b,c)


import collections


table = collections.defaultdict(int)

for i in range(1,14):
    key='I{0}'.format(i)
    table[key]=len(table)


def getIndices(key):
    indices=table.get(key)
    if indices==None:
        indices=len(table)
        table[key]=indices

    return indices


print(getIndices('fuck you'))
print(getIndices('haha you'))
print(getIndices('fuck you'))


for i,e in table.items():
    print(i)
    print(e)



