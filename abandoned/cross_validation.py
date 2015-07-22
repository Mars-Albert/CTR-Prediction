__author__ = 'mars'


import sys,subprocess
from csv import DictReader,DictWriter
if len(sys.argv) != 3:
    print('wrong arg')
    exit(1)

fold=sys.argv[1:]

fold=int(fold)


solution='one'


rootpath='output/cross_validation_split/'

workers=[]


#online算法使用非阻塞多进程，batch方式使用阻塞方式
def validation():
    for i in range(fold):
        cmd='python vw_solution.py {path}'.format(path=rootpath+'split_{id}/'.format(id=i))
       # cmd='python simple_solution.py {path} train.csv test.csv'.format(path=rootpath+'split_{id}/'.format(id=i))
        p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
        p.communicate()

       # workers.append(p)
    #for p in workers:
    #    p.communicate()

print('start cross validation!')


validation()


#比较结果！！！！！！
workers=[]
for i in range(fold):
#   cmd='python validate.py {path}'.format(path=rootpath+'split_{0}/'.format(i))
    cmd='python utils/evaluate.py {path}'.format(path=rootpath+'split_{0}/'.format(i))
    p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    workers.append(p)
for p in workers:
    p.communicate()

result=open(rootpath+'result.txt','w')
logloss=0.
auc=0.
for i in range(fold):
    reader=DictReader(open(rootpath+'split_{0}/result.csv'.format(i)))
    for t,row in enumerate(reader):
        result.writelines('split{0} logloss:{1} auc:{2}\n'.format(i,float(row['Logloss']),float(row['AUC'])))
        logloss+=float(row['Logloss'])
        auc+=float(row['AUC'])

logloss/=fold
auc/=fold

result.writelines('Average Logloss: {0} Average AUC:{1}\n'.format(logloss,auc))
result.close()
