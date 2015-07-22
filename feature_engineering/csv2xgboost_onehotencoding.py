__author__ = 'mars'

from csv import DictReader
import sys,collections
if len(sys.argv) != 3:
    print('wrong arg')
    exit(1)

data_path=sys.argv[1]
save_path=sys.argv[2]

THRESHOLD=10

#[positave][total][indice]
table = collections.defaultdict(int)

#建立整数值的编号
for i in range(1,14):
    key='I{0}'.format(i)
    table[key]=len(table)

def getIndices(key):
    indices=table.get(key)
    if indices==None:
        indices=len(table)
        table[key]=indices

    return indices



#一个是计算某个特征值的点击率（出现该特征值被点击/特征值出现的总次数）



with open(save_path+'train.sparse','w') as outfile:
    for e, row in enumerate(DictReader(open(data_path+'train.csv'))):
        features = []
        for k,v in row.items():
            if k not in ['Label','Id']:
                if 'I' in k: # numerical feature, example: I5
                    if len(str(v)) > 0 :
                        features.append('{0}:{1}'.format(getIndices(k),v))
                if 'C' in k:
                    if len(str(v)) > 0 :
                        key=k+'-'+v
                        key=v
                        features.append('{0}:1'.format(getIndices(key)))

        outfile.write('{0} {1}\n'.format(row['Label'],' '.join('{0}'.format(val) for val in features)))



validation=open(data_path+'validation.csv')
validation.__next__()
with open(save_path+'test.sparse','w') as outfile:
    for e, row in enumerate(DictReader(open(data_path+'test.csv'))):
        features = []
        for k,v in row.items():
            if k not in ['Label','Id']:
                if 'I' in k: # numerical feature, example: I5
                    if len(str(v)) > 0 :
                        features.append('{0}:{1}'.format(getIndices(k),v))
                if 'C' in k:
                    if len(str(v)) > 0 :
                        key=k+'-'+v
                        key=v
                        features.append('{0}:1'.format(getIndices(key)))

        if validation.readline().strip().split(',')[1] =='1':
            label = 1
        else:
            label = 0


        outfile.write('{0} {1}\n'.format(label,' '.join('{0}'.format(val) for val in features)))

validation.close()