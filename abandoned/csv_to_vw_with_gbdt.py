__author__ = 'mars'

from datetime import datetime
from csv import DictReader
import sys,subprocess,os

if len(sys.argv) != 3:
    print('wrong arg')
    exit(1)

path,type=sys.argv[1:]

if(type!='-train' and type!='-test'):
    print('wrong arg')
    exit(1)

path=str(path)
NR_THREAD=2





cmd = 'feature_engineering/converters/add_dummy_label.py {path}test.csv {path}te.csv'.format(path=path)
subprocess.call(cmd, shell=True)
print('dummy label to test.csv added!\n')


cmd = 'feature_engineering/converters/parallelizer-a.py -s {nr_thread} feature_engineering/converters/pre-a.py {path}train.csv {path}tr.gbdt.dense {path}tr.gbdt.sparse'.format(nr_thread=NR_THREAD,path=path)
subprocess.call(cmd, shell=True)
print('train set to dense and sparse format completed!\n')

cmd = 'feature_engineering/converters/parallelizer-a.py -s {nr_thread} feature_engineering/converters/pre-a.py {path}te.csv {path}te.gbdt.dense {path}te.gbdt.sparse'.format(nr_thread=NR_THREAD,path=path)
subprocess.call(cmd, shell=True)
print('test set to dense and sparse format completed!\n')

cmd = 'feature_engineering/converters/gbdt -t 30 -s {nr_thread} {path}te.gbdt.dense {path}te.gbdt.sparse {path}tr.gbdt.dense {path}tr.gbdt.sparse {path}te.gbdt.out {path}tr.gbdt.out'.format(nr_thread=NR_THREAD,path=path)
subprocess.call(cmd, shell=True)
print('gbdt features generated!\n')

cmd = 'rm -f {path}te.gbdt.dense {path}te.gbdt.sparse {path}tr.gbdt.dense {path}tr.gbdt.sparse'.format(path=path)
subprocess.call(cmd, shell=True)

#tr.csv原始特征，tr.gbdt.out增强（gbdt）特征
cmd = 'feature_engineering/converters/parallelizer-b.py -s {nr_thread} feature_engineering/converters/pre-b.py {path}train.csv {path}tr.gbdt.out {path}tr.sp {path}tr.addition'.format(nr_thread=NR_THREAD,path=path)
subprocess.call(cmd, shell=True)

print('gbdt features added to train dataSet\n')

cmd = 'feature_engineering/converters/parallelizer-b.py -s {nr_thread} feature_engineering/converters/pre-b.py {path}te.csv {path}te.gbdt.out {path}te.sp {path}te.addition'.format(nr_thread=NR_THREAD,path=path)
subprocess.call(cmd, shell=True)
print('gbdt features added to test dataSet\n')









if(type=='-train'):
    input=path+'tr.addition'
    output=path+'train.vw'
else:
    input=path+'te.addition'
    output=path+'test.vw'
    validation=open(path+'validation.csv')
    validation.__next__()


start = datetime.now()

with open(output,'w') as outfile:
    for e, row in enumerate( DictReader(open(input)) ):
        categorical_features = []
        for k,v in row.items():
            if k not in ['Label','Id']:
                if len(str(v)) > 0 :
                    categorical_features.append('{0}.{1}'.format(k,v)) #这里连‘-’导致测试不通过，很奇怪，无视之

        if(type=='-train'):
            if row['Label']=='1':
                label = 1
            else:
                label = -1
        else:
            if validation.readline().strip().split(',')[1] =='1':
                label = 1
            else:
                label =-1


        outfile.write('{0} \'{1} |features {2}\n'.format (label,row['Id'],' '.join(['{0}'.format(val) for val in categorical_features])))

        if e % 10000 == 0:
            sys.stdout.write('%s\t%s'%(e, str(datetime.now() - start)))

    sys.stdout.write('\n %s Task execution time:\n\t%s'%(e, str(datetime.now() - start)))


