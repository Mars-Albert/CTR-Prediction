
__author__ = 'mars'

from datetime import datetime
from csv import DictReader
import sys,subprocess,os

if len(sys.argv) != 3:
    print('wrong arg')
    exit(1)
NR_THREAD=8
#=2时，cat有错误！！

data_path=sys.argv[1]
save_path=sys.argv[2]


'''

对特征进行标准化处理

数值属性，大于2的，v<-|_log(v)**2_|，变为分类属性
分类属性，出现次数少于10次的转为特殊值


pre-c


'''

#-----------------------------------normalize------------------------

cmd = 'feature_engineering/converters/add_dummy_label.py {data}test.csv {data}test.tmp.csv'.format(data=data_path)
subprocess.call(cmd, shell=True)
print('dummy label to test.csv added!\n')


#tr.csv原始特征，tr.gbdt.out增强（gbdt）特征
cmd = 'feature_engineering/converters/parallelizer-normalization2csv.py -s {nr_thread}  {data}train.csv {save}tr.normalized'.format(nr_thread=NR_THREAD,data=data_path,save=save_path)
subprocess.call(cmd, shell=True)

print('normalized features added to train dataSet\n')

cmd = 'feature_engineering/converters/parallelizer-normalization2csv.py -s {nr_thread} {data}test.tmp.csv {save}te.normalized'.format(nr_thread=NR_THREAD,data=data_path,save=save_path)
subprocess.call(cmd, shell=True)
print('normalized features added to test dataSet\n')



#-----------------------------------normalize------------------------

print('gbdt process completed!')


start = datetime.now()

with open(save_path+'train.vw','w') as outfile:
    for e, row in enumerate( DictReader(open(save_path+'tr.normalized')) ):
        categorical_features = []
        for k,v in row.items():
            if k not in ['Label','Id']:
                if len(str(v)) > 0 :
                    categorical_features.append('{0}.{1}'.format(k,v)) #这里连‘-’导致测试不通过，很奇怪，无视之

        if row['Label']=='1':
            label = 1
        else:
            label = -1


        outfile.write('{0} \'{1} |features {2}\n'.format (label,row['Id'],' '.join(['{0}'.format(val) for val in categorical_features])))

        if e % 10000 == 0:
            print('%s\t%s'%(e, str(datetime.now() - start)))



validation=open(data_path+'validation.csv')
validation.__next__()

with open(save_path+'test.vw','w') as outfile:
    for e, row in enumerate( DictReader(open(save_path+'te.normalized')) ):
        categorical_features = []
        for k,v in row.items():
            if k not in ['Label','Id']:
                if len(str(v)) > 0 :
                    categorical_features.append('{0}.{1}'.format(k,v)) #这里连‘-’导致测试不通过，很奇怪，无视之


        if validation.readline().strip().split(',')[1] =='1':
            label = 1
        else:
            label = -1

        outfile.write('{0} \'{1} |features {2}\n'.format (label,row['Id'],' '.join(['{0}'.format(val) for val in categorical_features])))

        if e % 10000 == 0:
            print('%s\t%s'%(e, str(datetime.now() - start)))






validation.close()


print('\n %s Task execution time:\n\t%s'%(e, str(datetime.now() - start)))

