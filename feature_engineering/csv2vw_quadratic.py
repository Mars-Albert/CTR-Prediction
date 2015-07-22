__author__ = 'mars'
from csv import DictReader
import sys
if len(sys.argv) != 4:
    print('wrong arg')
    exit(1)


data_path=sys.argv[1]
save_path=sys.argv[2]
type=sys.argv[3]

if(type!='-train' and type!='-test'):
    print('wrong arg')
    exit(1)


if(type=='-train'):
    input=data_path+'train.csv'
    output=save_path+'train.vw'
else:
    input=data_path+'test.csv'
    output=save_path+'test.vw'
    validation=open(data_path+'validation.csv')
    validation.__next__()


with open(output,'w') as outfile:
    for e, row in enumerate(DictReader(open(input)) ):
        categorical_features = []
        numerical_features = []
        for k,v in row.items():
            if k not in ['Label','Id']:
                if 'C' in k:
                    if len(str(v)) > 0 :
                        offset=int(str(k).split('C')[1])+15
                        categorical_features.append('|{namespace} {v}'.format(namespace=chr(ord('1')+offset),v=v)) #这里连‘-’导致测试不通过，很奇怪，无视之
                        #命名空间映射到大写字母 A-Z
                if 'I' in k:
                    if len(str(v)) >0:
                        offset=int(str(k).split('I')[1])+47
                        numerical_features.append('|{namespace} {v}'.format(namespace=chr(ord('1')+offset),v=v))
                        #命名空间映射到小写写字母 a-m
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


        outfile.write('{0} \'{1} {2} {3}\n'.format (label,row['Id'],' '.join(['{0}'.format(val) for val in numerical_features]),' '.join(['{0}'.format(val) for val in categorical_features])))


if(type=='-test'):
    validation.close()
